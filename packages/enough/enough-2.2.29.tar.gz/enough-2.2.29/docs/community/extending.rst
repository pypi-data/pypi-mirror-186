Extending `enough.community`
============================

After :ref:`getting started <getting_started>`, you may want to add some
host/service in `enough.community` :ref:`infrastructure <infrastructure>`.

Overview
--------

The `enough.community` infrastructure is developed and deployed using ansible.
The main playbook is `enough-community-playbook.yml`.

Each playbook (for instance `playbooks/weblate/weblate-playbook.yml`) is
a `scenario`, i.e. a set of hosts and a test
playbook to get a minimal infrastructure setup allowing to validate
the service playbook. As an example, the weblate scenario found in
`playbooks/weblate/` defines the following hosts:

- a postfix master
- a bind server
- an icinga server
- the weblate host

With these, the `weblate` scenario is able to test the weblate
deployment, its monitoring, its ability to send emails, etc.

Some generally useful playbooks are grouped in the `misc` scenario.

The presence of a `bind-host` in most scenarios allows to spoof all records
from `enough.community` domain during the tests (and could spoof
any other domain). This disallow external requests like e.g. ACME
challenge for TLS Certificates. To overcome this limitation, the
domain of the scenario is defined in a one-time testing subdomain when a
`bind-host` is used by the scenario and the variable `letsencrypt_staging` has been
defined (meaning that we should use the "fake Let's Encrypt unlimited testing
infrastructure").

The `preprod` scenario aggregates all `enough.community` playbooks and
should be used to very they fit together as expected.

Adding a scenario
-----------------

Let's start with a `dummy` scenario.

Copying from an existing scenario
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is recommended to copy an existing scenario that ressembles the one
to be created.

::

 cp -a playbooks/website playbooks/dummy

Add `dummy` on the same line as `weblate` in `tox.ini`

Scenario definition
^^^^^^^^^^^^^^^^^^^

Edit `playbooks/dummy/conftest.py` to:

- update the list of hosts
- update the name of the new scenario


Adding playbooks
^^^^^^^^^^^^^^^^

The playbook is `playbooks/dummy/playbook.yml`. It should
include all playbooks used for the scenario, i.e.:

- others scenarios playbooks, like `playbooks/icinga/icinga-playbook.yml` or
  `playbooks/postfix/postfix-playbook.yml`
- the playbook specific to this scenario, here `playbooks/icinga/dummy-playbook.yml`. This
  playbook may include other playbooks.
- tests specific playbooks, starting with `test`, e.g.
  `playbooks/icinga/test-dummy-playbook.yml`.

Once the playbooks are added to run them with:

- tox -e weblate


Adding tests
^^^^^^^^^^^^

The purpose of the tests is mainly to detect that Ansible has deployed
a functional service. See them as `functionnal and non-regression
testing` to maintaining our Ansible base.

`testinfra <http://testinfra.readthedocs.io>`_ is used for this purpose. The
easiest way to get started with it is to look at some existing tests. For simple
testing see `playbooks/bind/tests/test_external_bind.py`. For a
`request <http://docs.python-requests.org>`_
based test, see e.g. `playbooks/weblate/tests/test_icingaweb.py`.

Since the tests run with virtual machines provisionned exclusively for
the test, you can do whatever you want (i.e. even some destructive
action).

Testing is not monitoring. You are kindly invited to setup monitoring
for your services and to test via testinfra that monitoring has been
setup as you wish.

Interaction with others scenarios
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Most services rely on :ref:`bind`, :ref:`emails <postfix>` and :ref:`monitoring
<monitoring>`. To enable them you have to add the corresponding hosts in your
scenario and include their playbook in your scenario's playbook.

You will also be interested by:

- `playbooks/misc/sexy-debian-playbook.yml` for getting usefull tools,
- `playbooks/authorized_keys/authorized-keys-playbook.yml` for installing
  ssh keys,
- `playbooks/misc/commit_etc-playbook.yml` for committing changes to
  `/etc/` at the end of your playbook.

Documentation
^^^^^^^^^^^^^

You are kindly invited to document your scenario in the `docs`
directory where this documentation lives.
