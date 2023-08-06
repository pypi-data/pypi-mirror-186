SecureDrop
==========

`SecureDrop <https://securedrop.org/>`__ is only available via Tor.
The administrative user, its password and TOTP can be set
as documented in `this file
<https://lab.enough.community/main/infrastructure/blob/master/playbooks/securedrop/roles/securedrop/defaults/main.yml>`__
and can be modified in the
`~/.enough/example.com/inventory/group_vars/securedrop-service-group.yml`
file.

The service is created on the host specified by the `--host` argument:

.. code::

    $ enough --domain example.com service create --host website-host securedrop

URLs
----

The URL of the source and journalist interfaces can be retrieved with:

.. code::

   $ enough --domain example.com ssh securedrop-host cat /var/lib/tor/services/source/hostname /var/lib/tor/services/journalist/hostname

The URL of the journalist interface requires an authentication token
and must be copied in the torrc file.
