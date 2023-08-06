Release Notes
=============

2.2.29
------

* forgejo: add forgejo_image & woodpecker_image_prefix

2.2.28
------

* hosteadashboard: upgrade to the latest

2.2.26
------

* gitea is replaced with forgejo and upgraded to 1.18.0-1

2.2.24
------

* gitlab: upgrade GitLab 15.6.2

2.2.23
------

* gitlab: upgrade GitLab 15.5.4

2.2.22
------

* wordpress: upgrade Wordpress 6.1.0
* gitlab: upgrade GitLab 15.4.3
* enough/libvirt: bug fixes related to remote libvirt hypervisors support

2.2.21
------

* gitea: upgrade Gitea 1.17.3 & Woodpecker 0.15.5

2.2.20
------

* libvirt: add the libvirt_ssh variable to run commands on the hypervisor
* gitea: upgrade Gitea 1.17.2 & Woodpecker 0.15.4
* gitlab: upgrade GitLab 15.3.4

2.2.19
------

* hosteadashboard: upgrade to the latest version, bug fixes and sanity checks only
* libvirt: libvirt_uri is added to specify an alternate connect URI to the libvirt daemon
* enough: add the libvirt network command to initialize it before provisioning a host

2.2.18
------

* vpn: automatically renew the CRL on a monthly basis
* hostea: upgrade the dashboard

2.2.17
------

* nginx: be resilient to DNS failure when VPN is not up
* gitlab: upgrade to 15.3.2
* bind: allow the definition of multiple zones
* pages: upgrade to version 0.1.0
* hostea: upgrade the dashboard

2.2.15
------

* hostea: fix permission of the deploy key

2.2.14
------

* hosteadashboard: add settings for configuration and deployment, with binding to gitea via OAuth2

2.2.12
------

* hostea: end to end testing

2.2.11
------

* certificates: web servers are configured with HSTS
* gitea: upgrade to Gitea 1.16.8 and Woodpecker 0.15.2
* hosteadashboard: first implementation of the Hostea dashboard playbook
* enough: bug fix the 'create test subdomain' subcommand

2.2.9
-----

* reduce the size of the enough docker image
* hostea: managed Gitea instances

2.2.8
-----

* gitea: activate email notifications and require email confirmation on account creation

2.2.7
-----

* pages: update static pages from a git repository

2.2.6
-----

* gitlab: upgrade to version 14.9.2

2.2.5
-----

* nextcloud: upgrade to version 23
* icinga: fix bullseye upgrade when grafana is on hold

2.2.4
-----

* woodpecker: open to all users with an account
* chat: fix bug preventing restart of the service
* tests: allow running tests when there is no cloud provider defined
* tests: fix libvirt broken test
* website: allow for FQDN to be reverse proxy, not just subdomains
* discourse: upgrade plugins & manager

2.2.3
-----

* discourse: upgrade to v2.8.2
* minor improvements to the bullseye migration playbook
* gitea: fix bug preventing the addition of woodpecker to the DNS

2.2.2
-----

* support https://woodpecker-ci.org with the `gitea` service

2.2.1
-----

* support https://gitea.io with the `gitea` service 
* minor changes to the Debian GNU/Linux bullseye upgrade playbook

2.2.0
-----

* upgrade to Debian GNU/Linux bullseye

2.1.40
------

* postfix: add the postfix_spf variable to override the default
* forum: https://github.com/discourse/discourse-calendar is added

2.1.39
------

* Upgrade discourse to version 2.7.9

2.1.37
------

* Upgrade discourse to version 2.7.8

2.1.35
------

* Bug fixes.

2.1.33
------

* Bug fixes.

2.1.32
------

* Bug fixes.

2.1.31
------

* Bug fixes.

2.1.30
------

* Upgrade GitLab from 13.8.4 to 13.12.1

2.1.29
------

* Bug fixes.

2.1.28
------

* Upgrade Open edX from version 11.0.2 to 11.2.11
* Add the `proxy` role to the `website` playbook to help define reverse proxies
  linking OpenStack and libvirt services.
* Add a cron job to the libvirt-hypervisor to upload backups to OpenStack

2.1.27
------

* Add a cron job to the libvirt host to download OpenStack backups.
* Add the `openvpnclient` service to connect the libvirt hosts to a VPN.
* Add `enough libvirt install --vpn` to connect the libvirt hypervisor to a VPN.

2.1.26
------

* Add `enough libvirt install` to setup a libvirt hypervisor.

2.1.25
------

* Add support for an upgrade to Nextcloud 20 (but the default still is Nextcloud 19).

2.1.24
------

* Bug fix only.

2.1.23
------

* Backups are more resilient to transient errors and do not repeat backups that are less than one day old
* The postfix mailname, banner and relay can be set with variables instead of being hardcoded

2.1.22
------

* Bug fix only.

2.1.21
------

* Add `backup download` to download the latest backup in `~/.enough/example.com/backups`.

2.1.18
------

website
~~~~~~~

* The ansible variable `website_domain` can be used to specify a domain other than `example.com`


2.1.17
------

* When using the libvirt infrastructure driver, the name of the host
  running the bind service is `bind-host` by default and can be
  changed. The following should be set in the
  `~/.enough/example.com/inventory/services.yml`::

       bind-service-group:
         hosts:
           bindother-host:

  This is useful when running more than one Enough instance from a single libvirt
  instance. When using the OpenStack infrastructure driver the bind service must
  run from a host named `bind-host`.

2.1.16
------

* Hosts can now be provisionned using libvirt instead of OpenStack. For instance::

    $ enough --domain example.com host create --driver libvirt bind
    bind: building image
    bind: preparing image
    bind: creating host
    bind: waiting for ipv4 to be allocated
    bind: waiting for 10.23.10.164:22 to come up
    Check if SSH is available on 10.23.10.164:22
    bind: host is ready
    +-------+--------------+
    | Field | Value        |
    +-------+--------------+
    | name  | bind         |
    | user  | debian       |
    | port  | 22           |
    | ip    | 10.23.10.164 |


2.1.15
------

website
~~~~~~~

* The ansible variable `website_repository` can be used to specify a repository other than `the default <https://lab.enough.community/main/website>`__.

certificates
~~~~~~~~~~~~

* Retry every minute during two hours if `no HTTPS certificate can be obtained <https://lab.enough.community/main/infrastructure/-/issues/314>`__. It is assumed that the cause for the failure is that DNS propagation can take a few hours.

nextcloud
~~~~~~~~~

* Reduce `memory requirements <https://lab.enough.community/main/infrastructure/-/issues/321>`__ when downloading files from Nextcloud. It can become a problem when the size of the file is large (i.e. greater than 1GB).

forum
~~~~~

* Pin the `discourse version and the plugins <https://lab.enough.community/main/infrastructure/-/issues/303>`__ to the latest stable release.

2.1.14
------

postfix
~~~~~~~

* `Fixes a bug <https://lab.enough.community/main/infrastructure/-/merge_requests/406>`__ blocking all outgoing mails on the relay.

2.1.13
------

gitlab
~~~~~~

* Add missing dependencies (debops.libvirt*) that would fail when trying
  to deploy a CI runner.

2.1.12
------

icinga
~~~~~~

The icinga client address was `hostvars[inventory_hostname]['ansible_host']` prior
to 2.1.12. It now is `icinga_client_address` which defaults to `hostvars[inventory_hostname]['ansible_host']`.
It can be used to resolve the following problem:

* The icinga master has a private IP and no public IP
* The icinga master goes through a router with a public IP
* The icinga client has a public IP which is the default for `icinga_client_address`
* The icinga master tries to ping the icinga client public IP but fails because the firewall of the client does not allow ICMP from the router public IP

The `icinga_client_address` of the client is set to the internal IP
instead of the public IP. The ping will succeed because the firewall
allows ICMP from any host connected to the internal network.

Development
~~~~~~~~~~~

* Added basic `support for running tests with libvirt <https://lab.enough.community/main/infrastructure/-/merge_requests/302>`__
  instead of OpenStack.
