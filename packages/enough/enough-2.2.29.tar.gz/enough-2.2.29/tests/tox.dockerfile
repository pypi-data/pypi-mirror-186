RUN pip3 install python-openstackclient python-heatclient python-glanceclient # this is not necessary to run tests but to cleanup leftovers when tests fail
RUN pip install tox
# BEGIN dependencies playbooks/infrastructure/test-pipelining.yml
RUN apt-get install -y python
# END dependencies playbooks/infrastructure/test-pipelining.yml
# BEGIN dependencies of test/ssh
RUN apt-get install -y jq
RUN pip install tox yq
RUN apt-get install -y python3-apt python3-lxml # required because python3 is used not python2
# END dependencies of test/ssh
# BEGIN dependencies of playbooks/hostea/tests/test_hostea.py
RUN apt-get install -y bind9-dnsutils
# END dependencies of playbooks/hostea/tests/test_hostea.py

RUN echo deb http://deb.debian.org/debian bullseye-backports main | tee /etc/apt/sources.list.d/backports.list
RUN apt-get update && apt-get install --no-install-recommends --quiet -y -t bullseye-backports python3-libvirt libvirt-dev

# Cache Python environment creations
COPY requirements.txt requirements-dev.txt tox.ini /opt/
RUN mkdir /opt/docs
COPY docs/requirements.txt /opt/docs/
RUN tox --notest -e py3_cache,flake8,docs

# BEGIN dependencies enabling .test resolution in the test container
RUN apt-get install -y bind9
COPY tests/named.conf.local /etc/bind
COPY tests/named.conf.options /etc/bind
COPY tests/entrypoint.sh /opt
# COPY --chmod requires BuildKit and docker 20.10
RUN chmod 0777 /opt/entrypoint.sh
ENTRYPOINT ["/opt/entrypoint.sh"]
# END dependencies enabling .test resolution in the test container
