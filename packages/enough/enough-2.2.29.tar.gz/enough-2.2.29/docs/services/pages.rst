Pages
=====

A static website is available at `www.example.com` and `example.com`. It is documented in `this file
<https://lab.enough.community/main/infrastructure/blob/master/playbooks/pages/roles/pages/defaults/main.yml>`__
and can be modified in the
`~/.enough/example.com/inventory/group_vars/pages-service-group.yml`
file.

The service is created on the host specified by the `--host` argument:

.. code::

    $ enough --domain example.com service create --host pages-host pages
