Website
=======

A `Hugo <https://gohugo.io/>`__ static website is available at `www.example.com` and is documented in `this file
<https://lab.enough.community/main/infrastructure/blob/master/playbooks/website/roles/website/defaults/main.yml>`__
and can be modified in the
`~/.enough/example.com/inventory/group_vars/website-service-group.yml`
file.

The service is created on the host specified by the `--host` argument:

.. code::

    $ enough --domain example.com service create --host website-host website

Reverse proxy
-------------

The nginx based website can be configured as a reverse proxy with a
playbook like the following:

.. code::

    - name: reverse proxy for website
      hosts: proxy-service-group
      become: true

      roles:
	- role: proxy
	  vars:
	    website_proxy_name: "public"
	    website_proxy_pass: "https://behind.proxy.other.com"
	    website_proxy_monitor_string: "Behind"
