    docker run --rm \
       {{ this.tty }} \
       -v $HOME/.enough:/root/.enough \
       -v /etc/ssl/certs:/etc/ssl/certs:ro \
       -v /run/libvirt/libvirt-sock:/run/libvirt/libvirt-sock \
       -v /var/lib/libvirt/images/enough:/var/lib/libvirt/images/enough \
       -v /usr/local/share/ca-certificates:/usr/local/share/ca-certificates:ro \
       -v /var/run/docker.sock:/var/run/docker.sock \
       --entrypoint enough \
       {{ this.registry }}enough{{ this.tag }} "$@"
