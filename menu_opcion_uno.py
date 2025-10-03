def opcion_numero_uno_menu(grupo):   
    while True:
        
        try:
            menu_opcion_uno = int(input("==Submenu grupo==\n1. Agregar persona\n2. Listar personas\n3. Volver\n"))
            
            if menu_opcion_uno == 1:
                crear_usuario = input("Introduzca el nombre del participante que desea agregar:\n")
                grupo.agregar_persona(crear_usuario)
            
            elif menu_opcion_uno == 2:
                grupo.listar_personas()
            
            elif menu_opcion_uno == 3:
                break
            
            else:
                print("Introduzca una opcion valida.")
        except ValueError:
            print("Introduzca una opcion valida. Son numeros. Opciones disponibles: 1-3")