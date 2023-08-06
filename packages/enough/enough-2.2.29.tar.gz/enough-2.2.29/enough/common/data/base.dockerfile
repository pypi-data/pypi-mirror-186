FROM debian:bullseye
ARG USER_NAME
ENV USER_NAME ${USER_NAME:-root}
ARG DOCKER_GID
ENV DOCKER_GID ${DOCKER_GID:-999}
ARG LIBVIRT_GID
ENV LIBVIRT_GID ${LIBVIRT_GID:-136}
ARG KVM_GID
ENV KVM_GID ${KVM_GID:-108}
ARG USER_ID
ENV USER_ID ${USER_ID:-0}

#
# The intention is to reduce the chances of conflict between the host libvirt & kvm system groups
# ids and the container system group ids.
#
RUN sed -i.backup -e 's/FIRST_SYSTEM_GID=.*/FIRST_SYSTEM_GID=500/' -e 's/FIRST_SYSTEM_UID=.*/FIRST_SYSTEM_UID=500/' /etc/adduser.conf
RUN apt-get update && \
    apt-get install --no-install-recommends --quiet -y \
         curl virtualenv python3 gcc libffi-dev libssl-dev python3-dev make git rsync \
	 sudo openvpn
#
# Install docker client & docker compose
# https://docs.docker.com/engine/install/debian/
#
RUN groupadd --gid $DOCKER_GID docker
RUN apt-get install --quiet -y ca-certificates curl gnupg lsb-release
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
RUN apt-get update && apt-get install --quiet -y docker-ce-cli
RUN curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose

RUN groupadd --gid $LIBVIRT_GID libvirt
RUN groupadd --gid $KVM_GID kvm
#
# Go back to where system group ids start because sanity checks may be made on
# the kvm & libvirt groups and fail if they are not in the system range. For
# instance if the host has kvm == 106 and FIRST_SYSTEM_GID == 500 in the container,
# kvm will not be considered to be a system group.
#
RUN mv /etc/adduser.conf.backup /etc/adduser.conf
RUN apt-get install --no-install-recommends --quiet -y libguestfs-tools linux-image-cloud-amd64 python3-lxml pkg-config
RUN echo deb http://deb.debian.org/debian bullseye-backports main | tee /etc/apt/sources.list.d/backports.list
RUN apt-get update && apt-get install --no-install-recommends --quiet -y -t bullseye-backports python3-libvirt libvirt-dev virtinst libvirt-clients

RUN if test $USER_NAME != root ; then useradd --no-create-home --home-dir /tmp --uid $USER_ID --groups $DOCKER_GID,$LIBVIRT_GID,$KVM_GID $USER_NAME && echo "$USER_NAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers ; fi
ENV REQUESTS_CA_BUNDLE /etc/ssl/certs

RUN ( echo "Host *" ; echo " StrictHostKeyChecking=no" ; echo " UserKnownHostsFile=/dev/null" ) | tee /etc/ssh/ssh_config

WORKDIR /opt
RUN virtualenv --python=python3 venv
ENV PATH="/opt/venv/bin:${PATH}"
RUN pip3 install pipenv
