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

# Delete all data under the '/users' node
snapshot = ref.delete()
print(snapshot)
