.. _domain:

Domain
======

The `enough.community` domain name is registered at `Gandi
<https://gandi.net>`_ under the user ieNua8ja.

After the `bind-host` virtual machine is created, click on `Glue record management` in the Gandi web
interface and set ns1 to the IP, i.e. 51.68.79.8 and wait a few
minutes. Click on `Update DNS` and set the `DNS1` server to
ns1.enough.community and click on `Add Gandi's secondary nameserver`
which should add a new entry in DNS2: it will automatically act as a
secondary DNS.

The `bind-host` virtual machine should be initialized before any other
because everything depends on it.

Mail
----

The `admin mail <admin@enough.community>`_ is
hosted at Gandi and is used as the primary contact for all
`enough.community` resources (hosting etc.). In case a password is lost
this is the mail receiving the link to reset the password etc.

Zones
-----

enough.community
````````````````
The `enough.community` zone is managed on a dedicated virtual machine
`ns1.enough.community`. It is generated via `the bind playbook
<http://lab.enough.community/main/enough-community/blob/master/playbooks/bind/bind-playbook.yml>`_.


* The port udp/53 is open to all but recursion is only allowed for IPs
  of the enough.community VMs
* An **A** record is created for all existing VM names
* A **CNAME** record is created for all VM names without the `-host` suffix
* The `SPF` **TXT** record help :doc:`send mail <../services/postfix>` successfully.

test.enough.community and d.enough.community
````````````````````````````````````````````

They can be updated locally by the `debian` user via ``nsupdate``. Example:

::

  - E - debian@bind-host:~$ nsupdate <<EOF
  server localhost
  zone test.enough.community
  update add bling.test.enough.community. 1800 TXT "Updated by nsupdate"
  show
  send
  quit
  EOF
