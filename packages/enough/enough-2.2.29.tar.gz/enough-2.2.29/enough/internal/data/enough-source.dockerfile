ARG IMAGE_NAME
FROM ${IMAGE_NAME}

COPY Pipfile Pipfile.lock /tmp/
RUN . /opt/venv/bin/activate ; cd /tmp ; PIPENV_VERBOSITY=-1 pipenv install --ignore-pipfile

COPY dist/* .
RUN pip3 install *.tar.gz

RUN apt-get remove --quiet -y --auto-remove gcc libffi-dev libssl-dev python3-dev make pkg-config libvirt-dev
RUN apt-get clean

CMD [ "help" ]
ENTRYPOINT [ "python", "-m", "enough.internal.cmd" ]
