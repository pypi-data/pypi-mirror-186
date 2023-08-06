# copied from securedrop/dockerfiles/xenial/python3/Dockerfile
# ubuntu 16.04 image from 2019-03-12
FROM ubuntu@sha256:58d0da8bc2f434983c6ca4713b08be00ff5586eb5cdff47bcde4b2e88fd40f88
ARG USER_NAME
ENV USER_NAME ${USER_NAME:-root}
ARG USER_ID
ENV USER_ID ${USER_ID:-0}

# If running grsecurity kernel on the host, Memprotect must be disabled on mono-sgen in the container
RUN apt-get update && apt-get install -y paxctl && \
    { apt-get install -y libgtk2.0 || echo 'libgtk2.0 was not installed'; } && \
    paxctl -cm /usr/bin/mono-sgen && dpkg-reconfigure mono-runtime-sgen && \
    apt-get install -y apache2-dev coreutils devscripts dh-virtualenv vim \
                       python3-pip python3-all python3-venv virtualenv libpython3.5-dev libssl-dev \
                       gnupg2 ruby redis-server git xvfb haveged curl wget \
                       gettext paxctl x11vnc enchant libffi-dev sqlite3 gettext sudo \
                       libasound2 libdbus-glib-1-2 libgtk2.0-0 libfontconfig1 libxrender1 \
                       libcairo-gobject2 libgtk-3-0 libstartup-notification0 tor

RUN gem install sass -v 3.4.23

COPY requirements requirements
RUN python3 -m venv /opt/venvs/securedrop-app-code && \
    /opt/venvs/securedrop-app-code/bin/pip3 install --no-deps --require-hashes -r requirements/python3/docker-requirements.txt && \
    /opt/venvs/securedrop-app-code/bin/pip3 install --no-deps --require-hashes -r requirements/python3/securedrop-app-code-requirements.txt && \
    /opt/venvs/securedrop-app-code/bin/pip3 install --no-deps --require-hashes -r requirements/python3/test-requirements.txt

RUN if test $USER_NAME != root ; then useradd --no-create-home --home-dir /tmp --uid $USER_ID $USER_NAME && echo "$USER_NAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers ; fi && \
    chown -R $USER_NAME.$USER_NAME /opt/venvs/securedrop-app-code/

STOPSIGNAL SIGKILL

EXPOSE 8080 8081 5909
