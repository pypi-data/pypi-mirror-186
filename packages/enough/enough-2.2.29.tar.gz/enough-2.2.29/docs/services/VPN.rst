.. _vpn:

VPN
===

Enough hosts can be connected to a public network (with public IP
addresses) and an internal network (with private IP addresses. When a
host is not connected to the public network, it can only be accessed
in two ways:

* By connecting to a host connected to both the public network and the
  internal network.
* By connecting to the VPN (which is running on a host connected to
  both the public network and the internal network).

The service is created on the host specified by the `--host` argument:

.. code::

    $ enough --domain example.com service create --host bind-host openvpn

VPN Server configuration
------------------------

The `OpenVPN <https://openvpn.net/>`__ server is configured with
variables (see `the documentation
<https://lab.enough.community/main/infrastructure/blob/master/playbooks/openvpn/roles/openvpn/defaults/main.yml>`__).

VPN subnet
----------

The default subnet used by the internal network and routed by the VPN
on the client machine is defined `in a configuration file
<https://lab.enough.community/main/infrastructure/blob/master/inventory/group_vars/all/internal_network.yml>`__
that may be modified in case it conflicts with an already used subnet.

VPN Clients creation
--------------------

The certificates for clients to connect to the VPN will be created
from the list in the `openvpn_active_clients` variable in
`~/.enough/example.com/inventory/group_vars/all/openvpn.yml`,
using `this example
<https://lab.enough.community/main/infrastructure/blob/master/inventory/group_vars/all/openvpn.yml>`__.

For each name in the `openvpn_active_clients` list, a `.tar.gz` file will be created in the
`~/.enough/example.com/openvpn/` directory. For instance, for

.. code::

   ---
   openvpn_active_clients:
    - loic
    - glen

After running `enough --domain example.com playbook`, the files
`~/.enough/example.com/openvpn/loic.tar.gz` and
`~/.enough/example.com/openvpn/glen.tar.gz` will be created and
will contain the credentials.

On Debian GNU/Linux the `.tar.gz` can be extracted in a `vpn`
directory and the `.conf` file it contains imported using the `Network
=> VPN` system settings.

VPN Clients retirement
----------------------

When a client should no longer be allowed in the VPN, it must be added
in the `openvpn_retired_clients` list, using `this example
<https://lab.enough.community/main/infrastructure/blob/master/inventory/group_vars/all/openvpn.yml>`__.
