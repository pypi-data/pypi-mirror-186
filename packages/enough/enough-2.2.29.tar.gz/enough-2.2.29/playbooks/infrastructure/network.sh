#!/bin/bash

#
# Prefer IPv4 because IPv6 is not supported
#
sed -i -e 's|^#precedence ::ffff:0:0/96  100|precedence ::ffff:0:0/96  100|' /etc/gai.conf
echo 'Acquire::ForceIPv4 "true";' > /etc/apt/apt.conf.d/99force-ipv4

if [ "$PORT" -ne "22" ]; then
  # Reload SSH
  sed -i -e '/^#Port/s/^.*$/Port '$PORT'/' /etc/ssh/sshd_config
  systemctl reload ssh
fi

PRODUCT_NAME="$(cat /sys/devices/virtual/dmi/id/product_name)"

if test -f /etc/network/interfaces.d/50-cloud-init ; then
  if [[ "${PRODUCT_NAME}" == "Fuga Cloud" && "$NOT_ROUTED" != "noname" ]]; then
      # The Fuga public interface uses static configuration, when not_routed isn't used, both public and private interfaces are used
      grep -Pzo "(?s)auto $ROUTED.*?(auto|\Z)" /etc/network/interfaces.d/50-cloud-init > /etc/network/interfaces.d/interface-$ROUTED.cfg
  fi
  if ! test -f /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg ; then
    echo 'network: {config: disabled}' > /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg
    rm -f /etc/network/interfaces.d/50-cloud-init
  fi
fi

for i in $ROUTED $NOT_ROUTED $UNCONFIGURED ; do
   if test "$i" != "noname" ; then
     ip link set "$i" up
     for _ in $(seq 500) ; do
        if test "$(cat /sys/class/net/$i/operstate)" = "up" ; then
          break
        fi
        sleep 1
     done
     if test "$(cat /sys/class/net/$i/operstate)" != "up" ; then
        echo "the $i interface is not up, giving up"
     fi
   fi
done

ifdown --force $ROUTED
if test $NOT_ROUTED != noname ; then
   ifdown --force $NOT_ROUTED
fi
if test $UNCONFIGURED != noname ; then
   ifdown --force $UNCONFIGURED
fi
#
# This may be necessary when a given interface is specified multiple
# times in /etc/network/interfaces* at boot time, resulting in multiple
# dhclient running. When bringing down the interface (see above) only
# one dhclient will be killed and the other will remain until the next
# reboot, interfering with other dhclient in unpredictible ways.
#
pkill -f dhclient
#
# Whatever resolvconf has cached for a given interface so far is
# discarded. In some weird cases /var/run/resolvconf/interface/lo.inet
# is set to a nameserver that will stick around until the next reboot
# and cannot be discarded.
#
rm -f /var/run/resolvconf/interface/*

cat > /etc/dhcp/dhclient-enter-hooks.d/ignore_unrequested_options <<'EOF'
# some DHCP servers send unrequested options: ignore these options
RUN="yes"

if [ "$RUN" = "yes" ]; then
    if [ "$interface" = "$NOT_ROUTED" ]; then
        # loop over some DHCP variables passed to dhclient-script
        for var in new_domain_name new_domain_search new_domain_name_servers \
                   new_routers new_rfc3442_classless_static_routes; do
            unset $var
        done
    fi
fi
EOF

echo 'source /etc/network/interfaces.d/*' > /etc/network/interfaces
( echo 'auto lo' ; echo 'iface lo inet loopback' )  > /etc/network/interfaces.d/interface-lo.cfg

cp /etc/dhcp/dhclient.conf /etc/dhcp/dhclient_routers.conf
if [[ "${PRODUCT_NAME}" != "Fuga Cloud" || "$NOT_ROUTED" == "noname" ]]; then
    # The Fuga public interface uses static configuration, when not_routed isn't used, both public and private interfaces are used
    ( echo "auto $ROUTED" ; echo "iface $ROUTED inet manual" ; echo '    mtu 1500' ; echo "    up /sbin/dhclient -4 -v -pf /run/dhclient.$ROUTED.pid -lf /var/lib/dhcp/dhclient.$ROUTED.leases -I -cf /etc/dhcp/dhclient_routers.conf $ROUTED" ; echo "    down /sbin/dhclient -4 -v -r -pf /run/dhclient.$ROUTED.pid -lf /var/lib/dhcp/dhclient.$ROUTED.leases -I -cf /etc/dhcp/dhclient_routers.conf $ROUTED" ) > /etc/network/interfaces.d/interface-$ROUTED.cfg
fi

cp /etc/dhcp/dhclient.conf /etc/dhcp/dhclient_no_routers.conf
sed -i -e 's/routers,//' -e 's/rfc3442-classless-static-routes,//' -e 's/domain-name, domain-name-servers, domain-search,//' /etc/dhcp/dhclient_no_routers.conf

if test $NOT_ROUTED != noname ; then
  ( echo "allow-hotplug $NOT_ROUTED" ; echo "auto $NOT_ROUTED" ; echo "iface $NOT_ROUTED inet manual" ; echo '    mtu 1500' ; echo "    up /sbin/dhclient -4 -v -pf /run/dhclient.$NOT_ROUTED.pid -lf /var/lib/dhcp/dhclient.$NOT_ROUTED.leases -I -cf /etc/dhcp/dhclient_no_routers.conf $NOT_ROUTED" ; echo "    down /sbin/dhclient -4 -v -r -pf /run/dhclient.$NOT_ROUTED.pid -lf /var/lib/dhcp/dhclient.$NOT_ROUTED.leases -I -cf /etc/dhcp/dhclient_no_routers.conf $NOT_ROUTED" ) > /etc/network/interfaces.d/interface-$NOT_ROUTED.cfg
fi

if test $UNCONFIGURED != noname ; then
  ( echo "auto $UNCONFIGURED" ; echo "iface $UNCONFIGURED inet manual" ) > /etc/network/interfaces.d/interface-$UNCONFIGURED.cfg
fi

ifup $ROUTED
if test $NOT_ROUTED != noname ; then
   ifup $NOT_ROUTED
fi
