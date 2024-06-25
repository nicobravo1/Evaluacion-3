import os
from funcion import *



while True:
    print("*********************")
    print("*********************")
    print("      MUNDO LIBRO    ")
    print("*********************")
    print("*********************")
    print(f"\n \n \n")

    print("[1]-  Mantenedor de usuarios") 
    print("[2]-  Reportes") 
    print("[3]-  Salir") 
    opc=int(input("Seleccione una opción: "))
    os.system(1)

    if opc==1:
        print("*********************")
        print("*********************")
        print("      Mantenedor Usuario    ")
        print("*********************")
        print("*********************")
        print(f"\n \n \n")

        print("[1]-  Agregar usuario") 
        print("[2]-  Editar usuario") 
        print("[3]-  Eliminar usuario")
        print("[4]-  Buscar usuario") 
        print("[5]-  volver") 
        mantenedor=int(input("¿Que desea realizar?[1-5]: "))
        if mantenedor==1:
            
            nom=str(input("Ingrese su nombre: "))
            email=str(input("Ingrese su correo: "))
            agregarUsuario(nom,email)
        if mantenedor==2:
            nom=str(input("Ingrese un nombre: "))
            email=str(input("Ingrese su correo: "))
            fecha=str(input("Ingrese la fecha:(dd-mm-aaaa): "))
            EditarUsuario(nom,email,fecha)

        if mantenedor==3:
            UsuarioID=int(input("Ingrese el ID del usuario que desea eliminar"))
            eliminarUsuario(UsuarioID)

        if mantenedor==4:
            print(BuscarUsario)

        if mantenedor==5:
            break
    if opc==3:
        break
    
    if opc==2:
        print(f"*********************************************")
        print("* Categoria             -   cantidad de libros")
        print(f"*********************************************")
        print(LeerCategorias)


    
        
        
