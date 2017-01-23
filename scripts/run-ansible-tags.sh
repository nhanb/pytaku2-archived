#!/usr/bin/env bash

ansible-playbook \
  -i ansible/inventories/vagrant ansible/vagrant-playbook.yml \
  -u vagrant \
  --private-key='.vagrant/machines/default/virtualbox/private_key' \
  --tags "$1"
