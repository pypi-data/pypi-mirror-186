Wekan
=====

`Wekan <https://wekan.github.io/>`__ is available at `wekan.example.com`.
The user with administrative rights is `admin`. Its password can be set
as documented in `this file
<https://lab.enough.community/main/infrastructure/blob/master/playbooks/wekan/roles/wekan/defaults/main.yml>`__
and can be modified in the
`~/.enough/example.com/inventory/group_vars/wekan-service-group.yml`
file.

The service is created on the host specified by the `--host` argument:

.. code::

    $ enough --domain example.com service create --host website-host wekan
