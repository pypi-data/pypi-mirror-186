Hostea
======

`Hostea <https://hostea.org/>`__ is a Forgejo hosting service backend. It creates OpenStack virtual machines and installs Forgejo on them, as instructed by an Ansible inventory. It runs from a CI, every time a commit is pushed to the repository containing the Ansible inventory.

In a nutshell it goes like this:

.. code::

    $ git clone git@forgejo.hostea.org:/hostea/fleet
    $ # edit files in fleet
    $ git commit -m 'Created the Forgejo instance foobar'
    $ git push

And go to the CI dashboard at https://woodpecker.hostea.org to check that it actually does what is expected. In the following it is assumed that Hostea is configured to run from the content of the https://forgejo.hostea.org/hostea/fleet repository and manage Forgejo fleet under the domain name d.hostea.org.

Configuration
-------------

`Hostea <https://hostea.org/>`__ is configured as as documented in `this file
<https://lab.enough.community/main/infrastructure/-/blob/master/playbooks/hostea/roles/hostea/defaults/main.yml>`__
and the values can be modified in the
`~/.enough/example.com/inventory/group_vars/hostea-service-group.yml`
file.

* Clone the repository `git clone git@forgejo.hostea.org:/hostea/fleet`
* Add the `inventory/group_vars/all/domain.yml` file to be something like:

..code::

   domain: example.com

* Add the `inventory/group_vars/all/clouds.yml` with a dedicated OpenStack tenant
* Commit and push


Setting the DNS glue record
---------------------------

Once `Enough` finished installing Hostea, the DNS server is up and ready to answer requests. But the registrar of `example.com` does not know about it and it must be told by creating a Glue Record. See, for instance, how that [can be done for Gandi.net](https://docs.gandi.net/en/domain_names/advanced_users/glue_records.html).

Assuming `git@forgejo.hostea.org:/hostea/fleet` is checked out in `~/.enough/example.com`, it is possible to display the IP of the DNS with:

..code::

    $ enough --domain example.com info
    bind-host ip=51.99.145.50 port=2222

Once this IP is set to be the Glue Record of the `example.com`, all DNS requests will be delegated to it and Hostea will take over.

..note::

    It may take a few hours for the Glue Record to propagate.

Creating a new Forgejo instance
-------------------------------

* pick unique name for the host, for instance hostea001-host
* git clone git@forgejo.hostea.org:/hostea/fleet
* cd hostea
* add the `hosts-scripts/hostea001-host.sh` script with the following:

.. code::

    enough --domain d.hostea.org host create hostea001-host
    enough --domain d.hostea.org service create --host hostea001-host forgejo

* add the `inventory/host_vars/hostea001-host/forgejo.yml` file using `this example <https://lab.enough.community/main/infrastructure/-/blob/master/playbooks/forgejo/roles/forgejo/defaults/main.yml>`__.
* add the `inventory/host_vars/hostea001-host/provision.yml` file to contain one of the following:
  * `openstack_flavor: '{{ openstack_flavor_small }}'` (default)
  * `openstack_flavor: '{{ openstack_flavor_medium }}'`
  * `openstack_flavor: '{{ openstack_flavor_large }}'`
* add the `inventory/hostea001-backup.yml` file with the following:

.. code::

    pets:
      hosts:
        hostea001-host:

* add the `inventory/hostea001-service.yml` file with the following:

.. code::

    forgejo-service-group:
      hosts:
        hosta001-host:
        ansible_port: 2222

* git add .
* git commit -m 'Created hostea001-host`
* git push

Deleting a Forgejo instance
---------------------------

* git clone git@forgejo.hostea.org:/hostea/fleet
* cd hostea
* remove the directory `inventory/host_vars/hostea001-host`
* remove the file `inventory/hostea001-backup.yml`
* remove the file `inventory/hostea001-service.yml`
* edit the `hosts-scripts/hostea001-host.sh` script with the following:

.. code::

    enough --domain d.hostea.org host delete hostea001-host

* git add .
* git commit -m 'Deleted hostea001-host`
* git push
