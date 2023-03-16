import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os
import json

my_secret_cred = os.environ.get('FIREBASE_CRED')
my_secret_db_url = os.environ.get('DB_URL')


cred = credentials.Certificate(json.loads(my_secret_cred))
firebase_admin.initialize_app(cred, {
    'databaseURL': my_secret_db_url
})

# Get a reference to the root node of your database
ref = db.reference('/users')
# Check if a node with the key "user1" exists under the '/users' node
if 'user1' in ref.get():
    # If the node exists, update its data
    snapshot = ref.child('Juan').update({
        'age': 30,
        'city': 'New York'
    })
    print(snapshot)
