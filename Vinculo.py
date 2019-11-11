class Vinculo:

    def __init__(self):
        self.alpha=0
        self.limart=90

    def get_posicion(self):
        return (self.alpha)

    def set_posicion(self,alpha):
        if alpha > self.limart:
            alpha=self.limart
        
        if alpha < -(self.limart):
            alpha=-(self.limart)
        
        self.alpha=alpha

    def set_limart(self,limart):
        self.limart=limart