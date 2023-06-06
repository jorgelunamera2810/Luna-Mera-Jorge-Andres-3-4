from figura_geometrica import FiguraGeometrica

class Triangulo (FiguraGeometrica)

    def __init__(self, base, altura):
        super().__init__(base=base, altura=altura)
        self.base = base
        self.altura = altura


    def area(self):
        return(self.base * self.altura) / 2

    def perimetro(self):
        return (self.base*3)

if __name__== '__main__':
    t1 =  (3, 4)
    print(t1)