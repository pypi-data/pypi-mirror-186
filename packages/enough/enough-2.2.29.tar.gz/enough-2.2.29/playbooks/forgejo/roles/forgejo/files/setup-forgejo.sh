#!/bin/bash

set -ex

function wait_for() {
    rm -f /tmp/setup-forgejo.out
    success=false
    for delay in 1 1 5 5 15 15 15 30 30 30 30 ; do
	if "$@" >> /tmp/setup-forgejo.out 2>&1 ; then
	    success=true
	    break
	fi
	cat /tmp/setup-forgejo.out
	echo waiting $delay
	sleep $delay
    done
    if test $success = false ; then
	cat /tmp/setup-forgejo.out
	return 1
    else
	grep 'Access token was successfully created' < /tmp/setup-forgejo.out | sed -e 's/.* //' > /srv/forgejo/forgejo-root-token
	return 0
    fi
}

function setup_forgejo() {
    local user="$1"
    local password="$2"
    local email="$3"

    sleep 5 # for some reason trying to run "gitea admin" while forgejo is booting will permanently break everything
    if sudo docker exec --user 1000 forgejo gitea admin user list --admin | grep "$user" ; then
	sudo docker exec --user 1000 forgejo gitea admin user change-password --username "$user" --password "$password"
    else
	wait_for sudo docker exec --user 1000 forgejo gitea admin user create --access-token --admin --username "$user" --password "$password" --email "$email"
    fi
}

setup_forgejo "$@"
