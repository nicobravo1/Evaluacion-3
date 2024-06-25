import json
from funcion import *

def LeerCategorias(Nom:str):
    with open('biblioteca.json',mode='r') as ArchivoJson:
        datos=json.load(ArchivoJson)
        categorias=datos["categoria"]
    
        print(ArchivoJson['categoria'])


