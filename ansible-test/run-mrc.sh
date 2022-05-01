#!/bin/bash

. ./config.sh; ansible-playbook -u ubuntu --key-file=~/.ssh/cloud.key mrc.yaml