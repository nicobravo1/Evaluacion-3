import json

def eliminarUsuario(UsuarioID:int):
    with open ('biblioteca.json',mode='r') as ArchivoJson:
        datos=json.load(ArchivoJson)
        usuarios=datos["UsuariosID"]
        for usuario in [usuarios]:
            if usuario['UsuarioID']==UsuarioID:
                
                usuarios.remove(UsuarioID)
                break
    with open('biblioteca.json',mode='w') as ArchivoJson:
        json.dump(datos,ArchivoJson,indent=4)





def agregarUsuario(nom:str,email:str):
    with open('biblioteca.json') as ArchivoJson:
        datos=json.load(ArchivoJson)
        usuarios=datos["Nombre,Email"]
        Usuario={
            "UsuarioID":len(datos[usuarios])+1,
            "Nombre":nom,
            "Email":email
            
            
            }
        datos["usuario"].append(Usuario)
    with open('biblioteca.json',mode='w') as ArchivoJson:
        json.dump(datos,ArchivoJson,ident=4)






def EditarUsuario(nom:str,email:str,fecha:str):
    with open('biblioteca.json',mode ='r') as ArchivoJson:
        datos=json.load(ArchivoJson)
        for i in len(ArchivoJson["Usuario"]):
            print()


    with open('biblioteca.json',mode='w') as ArchivoJson:
        json.dump(datos,ArchivoJson,ident=4)





def BuscarUsario(UsuarioID:int):
    with open('biblioteca.json',mode='r') as ArchivoJson:
        datos=json.load(ArchivoJson)
        print(ArchivoJson["Usuario"])

