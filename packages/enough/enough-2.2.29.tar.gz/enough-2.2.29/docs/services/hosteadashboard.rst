Hostea Dashboard
================

The Hostea dashboard available at `hosteadashboard.example.com`. It is documented in `this file
<https://lab.enough.community/main/infrastructure/blob/master/playbooks/hosteadashboard/roles/hosteadashboard/defaults/main.yml>`__
and can be modified in the
`~/.enough/example.com/inventory/group_vars/hosteadashboard-service-group.yml`
file.

The service is created on the host specified by the `--host` argument:

.. code::

    $ enough --domain example.com service create --host hosteadashboard-host hosteadashboard
