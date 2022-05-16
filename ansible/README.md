# Ansible Playbook
## Overview
Ansible is an open-source automation tool that provides the ability to configuration management, application deployment and repetitive maintenance tasks in a large scale server cluster.

All automation tasks are defined in a single Ansible playbook `mrc.yaml` which is generally divided into two plays.
- The first play will initialise multiple *MRC instances* with volumes and security rules attached.
- The second play will install packages and required dependencies to set up the environment on newly created servers. Services including *CouchDB*, *Twitter harvester* and *frontend* will be deployed then.

## File streucture
```
.
├── config.sh
├── host_vars
│   └── vars.yaml
├── mrc.yaml
├── roles
│   ├── common
│   ├── create-instance
│   ├── create-security-group
│   ├── create-volume
│   ├── deploy-frontend
│   ├── deploy-harvester
│   ├── init-couchdb
│   ├── install-docker
│   ├── mount-volumes
│   └── set-couchdb-cluster
├── run-mrc.sh
└── set-cors.sh
```
- `config.sh` - OpenStack RC File
- `host_vars` - contains global variables
- `mrc.yaml` - main playbook
- `roles` - list of all tasks
- `run-mrc.sh` - command to execute Ansible playbook

## How to execute
1. Replace `config.sh` with your OpenStack RC File.
2. Modify `run-mrc.sh` with your OpenStack RC File and corresponding private key:
```
. ./<OpenStack RC File>; ansible-playbook -u ubuntu --key-file=<private key> mrc.yaml
```
3. Execute `run-mrc.sh` and enter your OpenStack password when required.