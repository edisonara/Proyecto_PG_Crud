
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("JordanEdison.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
var = u'OKO0WpJH0bzh0EAoVMht'
#db.collection(u'Data').document(var).delete()
data = {
    'id': 1
}
data1 = db.collection(u'Data').document(u'OKO0WpJH0bzh0EAoVMht').set(data)
print(data1)
exit()

##################                 docs = db.collection(u'Lugar').stream()
##################                 
##################                 for doc in docs:
##################                     print(f'{doc.id} => {doc.to_dict()}')


def agrDat(ciudad , sector):
    dat = {"id":1,"Ciudad": ciudad,"sector" : sector }
    doc = db.collection("Lugar").add(dat)

agrDat("yoyoyoy" , "tutututututu")

## doc_ref = db.collection(u'Lugar')
## doc = doc_ref.get()
## if doc.exists:
##     print(f'Document data: {doc.to_dict()}')
## else:
##     print(u'No such document!')

# data = {
#             u'stringExample': u'Hello, World!',
#             u'booleanExample': True,
#             u'numberExample': 3.14159265,
#             u'arrayExample': [5, True, u'hello'],
#             u'nullExample': None,
#             u'objectExample': {
#                 u'a': 5,
#                 u'b': True
#             }
#         }
#         
# db.collection(u'Data').document(u'one').set(data)
# 
##  fire = db1.collection('Data')
##  data= fire.document('one')
##  leer = firebase_admin.get_app()
##  #data.push({'data1':'10'})
##  #data.update({'data1':'10'})
##  data.get()
##  print(type(leer))
docs = db.collection(u'Data').document('one')
print(docs)
for doc in docs:
    print(f'{doc}')


###### carpeta = db.collection(u'/Data/one', '')
###### carpeta = firebase_admin.get_app()
###### nombre1 = carpeta.get()
###### print(nombre1)

#date =firebase_admin.get_app(u"Data")
#print (date)
##nombre1 = carpeta.get()

