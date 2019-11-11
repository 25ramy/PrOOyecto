class Robot:
    from Efector import Efector
    efector= Efector()
    from Vinculo import Vinculo
    vinculo1=Vinculo()
    vinculo2=Vinculo()
    vinculo3=Vinculo()

    def __init__(self):
        self.estado=False

    def get_estado(self):
        return (self.estado)

    def activar(self):
        self.estado=True

    def desactivar(self):
        self.estado=False