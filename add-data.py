from datetime import datetime
from elasticsearch import Elasticsearch
import time

# Connect to your Elasticsearch server
es = Elasticsearch(["http://44.203.70.68:9200"])

# Define the index settings and mapping
index_settings = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
        "properties": {
            "networkId": {"type": "keyword"},
            "serial": {"type": "keyword"},
            "interface": {"type": "keyword"},
            "status": {"type": "keyword"},
            "ip": {"type": "ip"},
            "lastReportedAt": {"type": "date", "format": "strict_date_optional_time||epoch_millis"},
            "timestamp": {"type": "date", "format": "strict_date_optional_time||epoch_millis"}
        }
    }
}

# Create the "muz-index" index with the specified settings and mapping
# es.indices.create(index="muz-index", body=index_settings, ignore=400)
es.indices.create(index="muz-index", 
    settings=index_settings["settings"], 
    mappings=index_settings["mappings"], 
    ignore=400,
    headers={"Content-Type": "application/json"})


# Function to add a document to the "muz-index"
def add_document():

    current_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    sample_document = {
    "networkId": "N_772367336094045938",
    "serial": "Q2FY-QY3G-QYDN",
    "interface": "cellular",
    "status": "ready",
    "ip": "192.168.8.124",
    "lastReportedAt": current_time,
    "timestamp": current_time
    }

    es.index(index="muz-index", document=sample_document)
    print("Document added at", datetime.utcnow())

# Add a document every second
while True:
    add_document()
    time.sleep(1)
