#!/usr/bin/env bash

curl -X PUT http://admin:admin@172.26.134.126:5984/_node/couchdb@172.26.134.126/_config/chttpd/enable_cors -d '"true"'

curl -X PUT http://admin:admin@172.26.134.126:5984/_node/couchdb@172.26.134.126/_config/cors/origins -d '"*"'

curl -X PUT http://admin:admin@172.26.134.126:5984/_node/couchdb@172.26.134.126/_config/cors/credentials -d '"true"'

curl -X PUT http://admin:admin@172.26.134.126:5984/_node/couchdb@172.26.134.126/_config/cors/methods -d '"GET, PUT, POST, HEAD, DELETE"'

curl -X PUT http://admin:admin@172.26.134.126:5984/_node/couchdb@172.26.134.126/_config/cors/headers -d '"accept, authorization, content-type, origin, referer, x-csrf-token"'
