Backups
=======

Persistent data is placed in :ref:`encrypted volumes
<attached_volumes>` otherwise it may be deleted at any moment, when
the host fails.

Performing backups
------------------

A daily backup of all volumes is done on the host
designated to host backups (for instance `bind-host`) when the service
is created as follows:

.. code::

    $ enough --domain example.com service create --host bind-host backup

The number of backups is defined with the `backup_retention_days` variable
as documented `in this file <https://lab.enough.community/main/infrastructure/blob/master/playbooks/backup/roles/backup/defaults/main.yml>`__ and can be set in `~/.enough/example.com/inventory/group_vars/backup-service-group.yml` like so:

.. code:: yaml

    ---
    backup_retention_days: 7

.. note::

   If the quota for volume snapshots displayed by `enough --domain
   example.com quota show` is too low, a support ticket should be
   opened with the cloud provider to increase it.

A volume backup can be used to :ref:`restore a service
<restore_service_from_backup>` in the state it was at the time of the
backup.

The volumes are replicated three times and their data cannot be lost
because of a hardware failure.

Downloading backups
-------------------

It may be useful to download the latest backup from the cloud to a
local machine, as a last resort, in case the backups are unavailable
at the same time the host is unavailable.

The following command can be run manually or as a cron job:

.. code::

   $ enough --domain example.com backup download \
	    --volumes cloud-volume --volumes wekan-volume \
	    --hosts cloud-host --hosts wekan-host

The backups are stored in the `$HOME/.enough/backups` directory.
