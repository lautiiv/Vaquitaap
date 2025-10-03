from grupo_clases import Grupo
from grupo_clases import Persona
from menu_opcion_dos import opcion_2_registrar_gasto
from menu_opcion_uno import opcion_numero_uno_menu
from gasto import Gasto


print("Bienvenido a vaquita APP.")

grupo = Grupo("Amigos")


while True:
    try:
        menu = int(input("==== VAQUITA APP ====\n1. Definir y ver integrantes del grupo\n2. Registrar un gasto\n3. Ver gastos registrados\n4. Calcular y dividir gastos.\n5. Salir\n"))
        
        if menu == 1:
          opcion_numero_uno_menu(grupo)                       
                    
    
        elif menu == 2:
            opcion_2_registrar_gasto(grupo)
        
        elif menu == 3:
            print("Los gastos registrados son:\n")
            grupo.mostrar_gastos()
        
        elif menu == 4:
            grupo.calcular_informe()
        
        elif menu == 5:
            print("Gracias por utilizar Vaquita App.")
            break
        
        else:
            print("Introduzca una opcion valida.")
            
    except ValueError:
        print("Introduzca una opcion valida. Son numeros. Opciones disponibles: 1-5")