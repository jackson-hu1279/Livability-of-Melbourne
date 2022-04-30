import json
import couchdb

server = couchdb.Server("http://172.26.134.126:5984")
server.resource.credentials = ("admin", "admin")

with open("results-distress.json") as f:
    data = json.load(f)
    records = data["greater_melbourne"]

    # create db if necessary
    db_name = "aurin-distress"
    if db_name not in server:
        server.create(db_name)
    db = server[db_name]

    for record in records:
        db.save(record)
