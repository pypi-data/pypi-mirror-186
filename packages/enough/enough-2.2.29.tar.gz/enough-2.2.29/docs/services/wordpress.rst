WordPress
=========

`WordPress <https://wordpress.org/>`__ is available at
`wordpress.example.com`. The user with administrative rights and the
contact email are defined as documented in `this file
<https://lab.enough.community/main/infrastructure/blob/master/playbooks/wordpress/roles/wordpress/defaults/main.yml>`__
and can be modified in the
`~/.enough/example.com/inventory/group_vars/wordpress-service-group.yml`
file.

The service is created on the host specified by the `--host` argument:

.. code::

    $ enough --domain example.com service create --host wordpress-host wordpress
