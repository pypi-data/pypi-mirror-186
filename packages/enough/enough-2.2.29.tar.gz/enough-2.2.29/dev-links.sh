#!/bin/bash

mkdir -p ~/.enough/dev/inventory
ln -sf ~/.enough/dev/inventory/clouds.yml inventory/group_vars/all/clouds.yml
ln -sf ~/.enough/dev/inventory/domain.yml inventory/group_vars/all/domain.yml
if ! test -e ~/.enough/dev/inventory/domain.yml ; then
    cat > ~/.enough/dev/inventory/domain.yml <<EOF
---
domain: enough.community
EOF
fi
