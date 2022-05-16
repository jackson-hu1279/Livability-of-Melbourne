# Liveability of Melbourne
[![All Contributors](https://img.shields.io/badge/all_contributors-5-orange.svg?style=flat-square)](#contributors-)
![GitHub repo size](https://img.shields.io/github/repo-size/jackson-hu1279/Livability-of-Melbourne)
![GitHub](https://img.shields.io/github/license/jackson-hu1279/Livability-of-Melbourne)


COMP90024 Cluster and Cloud Computing Assignment 2 - TEAM 53

 
## Overview
This is the git repository for COMP90024 Assignment 2 Team 53. The purpose of this assignment is to develop a cloud based solution to explore aspects of the livability of Melbourne through a set of livability indicators by developing scenarios for these indicators and analysing the scenarios based on real time tweet data. In this project, we focused on the neighbourhood and health indicators, specifically focusing on the crime and mental health aspect in Greater Melbourne. 

## Video
https://youtube.com/playlist?list=PLNH1Fhe-gYxM0mh9OAEuU9f57RHeB2Llb

## Report
- [Project Report](./CCC2022-Team53-Report.pdf)

## Software Tool
- Ansible
- CouchDB
- Docker
- Kepler.gl
- Melbourne Research Cloud (MRC)
- Node
- Python
- React 
- Tweepy
- Twitter API

## Contributors

| Name | Student ID | Contact |
| :---                      |     :---    | :---                                              |
| Renwei Hu                 | 1067974     |  renweih@student.unimelb.edu.au                   |
| Siwat Chairattanamanokorn | 1338152     |  siwat.chairattanamanokorn@student.unimelb.edu.au |
| Renkai Liao               | 1141584     |  renkai@student.unimelb.edu.au                    |
| Chi Yin Wong              | 836872      |  chiw2@student.unimelb.edu.au                     |
| Kaiquan Lin               | 1147233     |  kaiquanl@student.unimelb.edu.au                  |

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/SiwatChairat"><img src="https://avatars.githubusercontent.com/u/48028669?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Siwat Chairattanamanokorn</b></sub></a><br /><a href="https://github.com/jackson-hu1279/Livability-of-Melbourne/commits?author=SiwatChairat" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/kkiill"><img src="https://avatars.githubusercontent.com/u/44608285?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Renkai Liao</b></sub></a><br /><a href="https://github.com/jackson-hu1279/Livability-of-Melbourne/commits?author=kkiill" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/jackson-hu1279"><img src="https://avatars.githubusercontent.com/u/68998854?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Renwei Hu</b></sub></a><br /><a href="https://github.com/jackson-hu1279/Livability-of-Melbourne/commits?author=jackson-hu1279" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/chiwong97"><img src="https://avatars.githubusercontent.com/u/89626592?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Chi Yin Wong</b></sub></a><br /><a href="https://github.com/jackson-hu1279/Livability-of-Melbourne/commits?author=chiwong97" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Tianlalu233"><img src="https://avatars.githubusercontent.com/u/42634872?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Kaiquan Lin</b></sub></a><br /><a href="https://github.com/jackson-hu1279/Livability-of-Melbourne/commits?author=Tianlalu233" title="Documentation">📖</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

## Folder Structure
```
.
├── adding-LGA
├── ansible
│   ├── host_vars
│   └── roles
│       ├── common
│       ├── create-instance
│       ├── create-security-group
│       ├── create-volume
│       ├── deploy-frontend
│       ├── deploy-harvester
│       ├── init-couchdb
│       ├── install-docker
│       ├── mount-volumes
│       └── set-couchdb-cluster
├── crawler
├── frontend
│   └── webapp
│       ├── public
│       └── src
├── import-historic-tweets-couchdb
└── keyword-list
```
### Directories:
- `ansible` - Ansible scripts
- `crawler` - Twitter harvester Python scripts
- `frontend` - Frontend React application
- `adding-LGA` - Python scripts to attach LGA code/name
- `import-historic-tweets-couchdb` - Scripts to import historical data
- `keyword-list` - contains list of keywords for scenarios
