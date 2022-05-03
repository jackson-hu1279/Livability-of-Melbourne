#!/bin/bash/

# the general command is (repeat for all 100 extracted json files)

curl -d @json_file -H "Content-type: application/json" -X POST: http://user:password@IPaddress:port/db_name/_bulk_docs

# modification needed for cluster? not sure 