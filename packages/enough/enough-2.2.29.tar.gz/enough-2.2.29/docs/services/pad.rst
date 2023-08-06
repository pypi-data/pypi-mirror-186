Etherpad
========

`Etherpad <https://etherpad.org/>`__ is available at `pad.example.com`.
The user with administrative rights is `admin`. Its password can be set
as documented in `this file
<https://lab.enough.community/main/infrastructure/blob/master/playbooks/pad/roles/pad/defaults/main.yml>`__
and can be modified in the
`~/.enough/example.com/inventory/group_vars/pad-service-group.yml`
file.

The service is created on the host specified by the `--host` argument:

.. code::

    $ enough --domain example.com service create --host pad-host pad
