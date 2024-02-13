#!/bin/bash

ansible-playbook ./playbooks/prerequis -i hosts
ansible-playbook ./playbooks/install-fzf -i hosts
