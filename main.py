# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 09:14:33 2024

@author: Navuru.Prasad
"""

#import json
import os
#from google.cloud import pubsub_v1
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

# Initialize the Pub/Sub client
project_id = "automate-cicd-gcp"  # Make  sure this is correct
topic_id = "bigquery-events"
#publisher = pubsub_v1.PublisherClient()
#topic_path = publisher.topic_path(project_id, topic_id)
current_time = datetime.now().isoformat()
business_rule = 'Null'

data_store = {
   "request_id":"ab6c0079-70c1-433e-a3c3-3391eef0cbde",
   "id":"73e001d9-81e7-4fa5-8a6d-2b33effb03dc",
   "dt":"June 21, 2023, 1:51:27 AM",
   "domain":"meta.wikimedia.org",
   "stream":"mediawiki.page-create",
   "topic":"eqiad.mediawiki.page-create",
   "partition":0,
   "offset":224707499,
   "page_id":11738673,
   "rev_timestamp":" June 21, 2023, 1:51:26 AM",
   "rev_id":22922162,
   "user_id":29235191,
   "user_edit_count":8138
}

# Expose data_store via API endpoint
@app.route("/data_store", methods=["GET"])
def get_event_data():
    return jsonify(data_store), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
