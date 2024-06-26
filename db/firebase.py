import reflex as rx

import firebase_admin
from firebase_admin import firestore, credentials

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
comments_ref = db.collection('comentarios')

def add_comment(data):  
    doc_ref = comments_ref.document()
    doc_ref.set(data)  
    response = search_comment(doc_ref.id)    
    return response

def search_comment(id):
    rx.console.log(id)
    doc = comments_ref.document(id).get()
    if doc.exists:
        return True
    else:
        return False

