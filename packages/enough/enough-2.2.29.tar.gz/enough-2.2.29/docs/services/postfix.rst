.. _postfix:

SMTP server
===========


The service is created on the host specified by the `--host` argument:

.. code::

    $ enough --domain example.com service create --host postfix-host postfix

A SMTP server is running on each host. A service running on
`some-host.example.com` can use the SMTP server as follows:

* Address: some-host.example.com
* Port: 25
* Authentication: No
* SSL/TLS: No

It is not possible (and it would not be secure) for services running
on another host (`other-host.example.com` for instance) to use this
SMTP server.

The `mailname` defaults to `example.com` but can be overridden with the `postfix_mailname` variable in
the `~/.enough/example.com/inventory/host_vars/postfix-host/postfix.yml`.

Encryption
----------

Outgoing mails are encrypted if the recipient has a known GPG public
key.  The list of GPG public keys must be provided in the
`~/.enough/example.com/inventory/host_vars/postfix-host/gpg.yml`
file like so:

.. code:: yaml

    ---
    postfix_gpg_keys:
     - "{{ '~/.enough/example.com/gpg/*.asc' | expanduser }}"
