#!/bin/bash

sudo /usr/sbin/named -4 -L /var/log/named.log

exec "$@"
