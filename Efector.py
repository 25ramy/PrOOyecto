class Efector:

    def __init__(self):
        self.estado=False

    def get_estado(self):
        return (self.estado)

    def abrir(self):
        self.estado=True

    def cerrar(self):
        self.estado=False