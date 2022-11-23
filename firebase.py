
import firebase_admin
import google.cloud
from firebase_admin import credentials
from google.cloud import firestore


cred = credentials.Certificate("onibus.json")
firebase_admin.initialize_app(cred)


db = firestore.Client()  # this connects to our Firestore database
collection = db.collection('linhas')  # opens 'places' collection
doc = collection.document('6az5wSC3Gzs24TrbeaDT')

res = doc.get().to_dict()
print(res)