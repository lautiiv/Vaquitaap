from gasto import Gasto

class Persona():
    def __init__(self,nombre):
        self.nombre = nombre
        self.pagado = 0.0
        self.balance = 0.0
        
        
    def __str__(self):
        return f'{self.nombre} (Pagado: {self.pagado}, Balance: {self.balance})'
        
        
class Grupo():
    def __init__(self, nombre):
        self.nombre = nombre
        self.personas = []
        self.gastos = []
        
    def agregar_persona(self,nombre):
        integrante_del_grupo = Persona(nombre)
        self.personas.append(integrante_del_grupo)
        return True, print("Persona agregada.")

        
        
    def listar_personas(self):
        for persona in self.personas:
            print(persona)
            
    
    def calcular_informe(self):
        pass


    def obtener_persona(self, nombre):
        for p in self.personas:
            if p.nombre.lower() == nombre.lower():
                return p
        return None
    
    
    def resolver_personas(self, lista_nombres):
        personas = []
        for n in lista_nombres:
            p = self.obtener_persona(n)
            if not p:
                return None, f"No existe el participante: {n}"
            if p not in personas:           # evita duplicados
                personas.append(p)
        return personas, None    
    
    

    def registrar_gasto(self, descripcion, monto, pagador_nombre, involucrados_nombres):
        if not descripcion.strip():
            return False, "La descripción no puede estar vacía."
        if not isinstance(monto, (int, float)) or monto <= 0:
            return False, "El monto debe ser mayor que 0."

        pagador = self.obtener_persona(pagador_nombre)
        if not pagador:
            return False, f"No existe el pagador: {pagador_nombre}"

        involucrados, err = self.resolver_personas(involucrados_nombres)
        if err: 
             return False, err
        if len(involucrados) == 0:
            return False, "Debe haber al menos un involucrado."

    # si el pagador no viene en la lista de involucrados, lo incluimos
        if pagador not in involucrados:
         involucrados.append(pagador)

        gasto = Gasto(descripcion, monto, pagador, involucrados)
        self.gastos.append(gasto)

    # actualizar saldos
        parte = gasto.monto / len(gasto.involucrados)
        for p in gasto.involucrados:
            p.balance -= parte
        gasto.pagador.pagado += gasto.monto
        gasto.pagador.balance += gasto.monto

        return True, "Gasto registrado."
    
    def mostrar_gastos(self):
        for gasto in self.gastos:
            print(gasto)
            
            
                    
    def __str__(self):
        if not self.personas:
         return f"Grupo {self.nombre} (sin integrantes)"
        nombres = ", ".join(p.nombre for p in self.personas)
        return f"Grupo {self.nombre}: {nombres}"
    
    def calcular_informe(self):
        acreedores = []
        deudores = []
        print("=== Resumen por persona ===")
        for persona in self.personas:
            
            corresponde = persona.pagado - persona.balance
            saldo = persona.balance
           
            print(F"{persona.nombre} pago: {persona.pagado} |"
                 f" Le corresponde pagar: {corresponde} | Saldo final: ${saldo}")
           
            if saldo > 0:
               acreedores.append((persona, saldo))
               
            elif saldo < 0:
               deudores.append((persona, -saldo))
               
               
               
        print("\nAcreedores:", [(persona.nombre, m) for persona, m in acreedores])
        print("Deudores  :", [(persona.nombre, m) for persona, m in deudores])
        
        print("\n=== Informe de pagos ===")

        i, j = 0, 0
        while i < len(deudores) and j < len(acreedores):
         deudor, deuda = deudores[i]
        acreedor, credito = acreedores[j]

        monto = round(min(deuda, credito), 2)
        if monto > 0.01:
            print(f"{deudor.nombre} debe pagarle ${monto:.2f} a {acreedor.nombre}")

        deuda = round(deuda - monto, 2)
        credito = round(credito - monto, 2)

        if deuda <= 0.01:
            i += 1
        else:
            deudores[i] = (deudor, deuda)

        if credito <= 0.01:
            j += 1
        else:
            acreedores[j] = (acreedor, credito)