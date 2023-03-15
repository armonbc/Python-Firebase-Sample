import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os

my_secret_cred = os.environ.get('FIREBASE_CRED')
my_secret_db = os.environ.get('DB_URL')


cred = credentials.Certificate(my_secret_cred)
firebase_admin.initialize_app(cred, {
    'databaseURL': my_secret_db
})

# Get a reference to the root node of your database
ref = db.reference('/')

# Write data to the database
ref.child('users').child('user1').set({
    'name': 'John',
    'age': 30
})

# Read data from the database
snapshot = ref.child('users').get()
print(snapshot)
