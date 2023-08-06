.. _monitoring:

Monitoring
==========

The `Icinga <https://icinga.com/>`_ Monitoring System watches over all
hosts (disk space, load average, security updates, etc.). In addition
services may add specific monitoring probes such as loading a web page
and verifying its content is valid.

The service is created on the host specified by the `--host` argument:

.. code::

    $ enough --domain example.com service create --host icinga-host icinga

The Icinga web interface is at `icinga.example.com`. The user name
and password with administrator rights must be defined in
`~/.enough/example.com/inventory/host_vars/icinga-host/icinga-secrets.yml`
with variables documented in `this file
<https://lab.enough.community/main/infrastructure/blob/master/playbooks/icinga/roles/icinga2/defaults/main.yml>`__

Problems found by Icinga will be notified via email to the address defined in
`~/.enough/example.com/inventory/host_vars/icinga-host/mail.yml` with
a variable doumented in `this file <https://lab.enough.community/main/infrastructure/blob/master/inventory/group_vars/all/monitoring.yml>`__.

The Icinga master pings the icinga client using `icinga_client_address` as found in
`this file <https://lab.enough.community/main/infrastructure/-/tree/master/playbooks/icinga/roles/icinga2_client/defaults/main.yml>`__.
