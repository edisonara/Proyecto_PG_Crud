import firebase_admin
from firebase_admin import credentials, firestore
from random import *
def numero():
    variable=randint(10000,99999)
    return variable

class Entidades():
    def __init__(self):
        cred = credentials.Certificate("JordanEdison.json")
        firebase_admin.initialize_app(cred)
        self.__db = firestore.client()


    def inserta(self,id, provincia, canton, parroquia, colegio ):
        """
        Id: de tipo int 
        provincia, canton, parroquia, colegio: de tipo str. """
        data = {
            u'id': id, 
            u'PROV_COD': provincia,
            u'CANT_COD': canton,
            u'PARR_COD': parroquia,
            u'COLE_COD': colegio
        }
        
        self.__db.collection(u'MIES').document(u'one').add(data)


    def busca(self,id ):
        ##################                 docs = db.collection(u'Lugar').stream()
        ##################                 
        ##################                 for doc in docs:
        ##################                     print(f'{doc.id} => {doc.to_dict()}')
        ###    self.carpeta = self.__db.collection(u'MIES').document(u'')
        ###    dato = self.carpeta.get()
        ###    return dato
        ####  data = {
        ####      u'id': id
        ####  }
        ####  data = self.__db.collection(u'MIES').document(u'one').set(data)
        ####  ##  for recorre in data:
        ####  ##      return recorre
        ####  return data
        pass

    def elimina(self, documento, provincia, canton, parroquia, colegio2):
        self.__db.collection(u'MIES').document(u'DC').delete()

        
  
    def actualiza(self, documento, ):
        pass


datos = Entidades()
