.. _bind:

DNS
===

Records
-------

When a new host is created (for instance with `enough --domain
example.com host create cloud-host`) the names
`cloud-host.example.com` and `cloud.example.com` are added to the DNS.

The `bind_zone_records` variable is inserted in the `example.com` zone
declaration verbatim (see the `BIND documentation for information <https://bind9.readthedocs.io/en/latest/reference.html#zone-file>`__).
It can be set in `~/.enough/example.com/inventory/host_vars/bind-host/zone.yml` like so:

.. code:: yaml

    bind_zone_records: |
         imap 1800 IN CNAME access.mail.gandi.net.
         pop 1800 IN CNAME access.mail.gandi.net.
         smtp 1800 IN CNAME relay.mail.gandi.net.
    
         @ 1800 IN MX 50 fb.mail.gandi.net.
         @ 1800 IN MX 10 spool.mail.gandi.net.


Host Resolver
-------------

The resolver of all hosts (in `/etc/resolv.conf`) is set with the IP
of the DNS server that was :ref:`created to bootstrap Enough
<bind_create>`.  It is used to resolve the host names in the Enough
domain (for instance `example.com` or `cloud.example.com`) and all
other domain names (for instance `gnu.org` or `fsf.org`).

VPN Resolver
------------

When a client connects to the :doc:`VPN <VPN>`, its resolver is set to the
Enough DNS server.

.. note::

   Using the Enough DNS instead of the DNS of an internet service
   provider bypasses rewrites of DNS entries (imposed by by `the state
   <https://www.legifrance.gouv.fr/affichTexte.do?cidTexte=JORFTEXT000030195477&dateTexte=&categorieLien=id>`__
   in some cases).
