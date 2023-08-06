Introduction
============

Enough is a self-hostable infrastructure based on libvirt, OpenStack and Ansible. It provides the
following services:

* `Nextcloud <https://nextcloud.com/>`__, a suite of client-server
  software for creating and using file hosting services.
* `Discourse <https://www.discourse.org/>`__, a discussion platform
  built for the next decade of the Internet. Use it as a mailing list,
  discussion forum, long-form chat room, and more!
* `Mattermost <https://mattermost.com/>`__, a flexible messaging
  platform that enables secure team collaboration.
* `Hugo <https://gohugo.io/>`__, a static web site generator.
* `Weblate <https://weblate.org/>`__, a libre web-based translation
  tool with tight version control integration. It provides two user
  interfaces, propagation of translations across components, quality
  checks and automatic linking to source files.
* `Wekan <https://wekan.github.io/>`__, a kanban board which allows a
  card-based task and to-do management.
* `Etherpad <https://etherpad.org/>`__, a highly customizable online
  editor providing collaborative editing in really real-time.
* `GitLab <https://gitlab.com/>`__, a web-based DevOps lifecycle tool
  that provides a Git-repository manager providing wiki,
  issue-tracking and continuous integration/continuous deployment
  pipeline features.
* `OpenVPN <https://openvpn.net/>`__, that implements virtual private
  network (VPN) techniques to create secure point-to-point or
  site-to-site connections in routed or bridged configurations and
  remote access facilities

The `enough` CLI controls an OpenStack based infrastructure and the
services that run on top of it, with Ansible.

Requirements
------------

* An account on a supported OpenStack provider:

  * A ``Public cloud`` project at `OVH <https://www.ovh.com/manager/public-cloud/>`__.
    A `Private network <https://www.ovh.com/world/solutions/vrack/>`__ must be created for
    the project.
  * A `Fuga <https://fuga.cloud>`__ account.

* The `clouds.yml` credentials for:

   * OVH, found `in horizon <https://horizon.cloud.ovh.net/project/api_access/clouds.yaml>`__
   * Fuga, found `in the Team Credentials tab <https://my.fuga.cloud/account/team-credentials>`__
     Note that the OpenVPN service requires to use the ``AMS2`` rather the ``AMS`` OpenStack region.

Quick start
-----------

* `Install Docker <http://docs.docker.com/engine/installation/>`__.

* Copy `clouds.yml` in `~/.enough/myname.d.enough.community/inventory/group_vars/all/clouds.yml` and edit
  to add `password:` next to `auth_url:`, under the `production:` name. For instance:

  ::

    ---
    openstack_provider: fuga
    clouds:
      production:
        auth:
          auth_url: "https://identity.api.ams.fuga.cloud:443/v3"
          user_id: "ef5cae1b61b8424594a6ddf94a28381c"
          password: "lDk9vOLIXFW09oWcuQEiq0sjB4cV"
          user_domain_id: "b919e18e477a889bf89f89e9d9"
          project_domain_id: "b919e186cb07a889bf89f89e9d9"
          project_id: "25481e67871b4de39ae63fa2008029"
        region_name: "ams"
        interface: "public"
        identity_api_version: 3


* Add the ``enough`` CLI to ``~/.bashrc``:

  ::

     eval "$(docker run --rm enoughcommunity/enough:latest install)"

* Create the ``Nextcloud`` service with:

  ::

     $ enough --domain myname.d.enough.community service create cloud

..  note::
    If the command fails, because of a network failure or any other reason,
    it is safe to run it again. It is idempotent.

* Login ``https://cloud.myname.d.enough.community`` with user ``admin`` password ``mynextcloud``

* Display the hosts that were created and the services they run:

  ::

     $ enough --domain myname.d.enough.community info
     bind-host ip=51.168.48.253 port=22
	bind
     cloud-host ip=51.68.77.181 port=22
	cloud	https://cloud.myname.d.enough.community
	        nextcloud_admin_user=admin
		enough_nextcloud_version=23
		nextcloud_admin_pass=*****
