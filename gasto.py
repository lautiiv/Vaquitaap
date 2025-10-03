class Gasto:
    def __init__(self, descripcion, monto, pagador, involucrados):
        self.descripcion = descripcion
        self.monto = monto
        self.pagador = pagador              
        self.involucrados = involucrados    

    def __str__(self):
        inv = ", ".join(p.nombre for p in self.involucrados)
        return f"{self.descripcion} - ${self.monto:.2f} | Pagó: {self.pagador.nombre} | Involucrados: {inv}"