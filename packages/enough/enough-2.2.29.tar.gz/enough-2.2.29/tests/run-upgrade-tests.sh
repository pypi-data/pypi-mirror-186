#!/bin/bash

set -e

function refdir() {
    local ref="$1"

    local toplevel=$(git rev-parse --show-toplevel)
    local basedir=$(dirname $toplevel)
    echo "$basedir/infrastructure-versions/$ref"
}

function prepare_refdir() {
    local refdir="$1"
    local ref="$2"

    mkdir -p $refdir
    if ! test -d $refdir/infrastructure ; then
        git clone --reference . . $refdir/infrastructure
    fi
    git -C $refdir/infrastructure checkout $ref
    cp inventory/group_vars/all/clouds.yml $refdir/infrastructure/inventory/group_vars/all/clouds.yml
    cp inventory/group_vars/all/clouds.yml $refdir/infrastructure/tests/clouds.yml
}

function rsync_pytest_cache() {
    local refdir="$1"
    local service="$2"
    
    local c=.tox/$service/.pytest_cache/d
    mkdir -p $c
    rsync -av --delete $refdir/infrastructure/$c/ $c/
    sed -i -e "s|$refdir/infrastructure/||" $c/dotenough/$service.test/inventory/group_vars/all/private-key.yml
    rm -f $refdir/infrastructure/.tox/*/.pytest_cache/d/dotenough/*.test/inventory/hosts.yml
}

function main() {
    local ref="$1"
    shift
    local service="$1"
    shift
    local refdir=$(refdir $ref)
    prepare_refdir $refdir $ref
    ( cd $refdir/infrastructure ; tests/run-tests.sh tox -e $service "$@")
    rsync_pytest_cache $refdir $service
    tests/run-tests.sh tox -e $service "$@"
}

main "$@"
