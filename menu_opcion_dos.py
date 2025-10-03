

def opcion_2_registrar_gasto(grupo):
    while True:
       while True:
        print("\n== Opción 2: Registrar gasto ==")
        try:
            descripcion = input("Descripción: ").strip()
            mont_str = input("Monto: ").strip()
            pagador = input("Nombre del pagador: ").strip()
            inv_str = input("Involucrados (separados por coma): ").strip()
            involucrados_nombres = [n.strip() for n in inv_str.split(",") if n.strip()]

            # delega toda la validación al método del Grupo
            try:
                monto = float(mont_str)
            except ValueError:
                print("Ingresá un número válido para el monto.")
                continue

            ok, msg = grupo.registrar_gasto(descripcion, monto, pagador, involucrados_nombres)
            print(msg)

            if ok:
                seguir = input("¿Registrar otro gasto? (s/n): ").strip().lower()
                if seguir != "s":
                    return
        except KeyboardInterrupt:
            print("\nCancelado por el usuario.")
            return