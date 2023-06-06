

class FiguaGeometrica:

    def __init__(self,base:float=0.0, altura:float=0.0):
        self._base = base
        self._altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        self._base = base

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        self._altura = altura