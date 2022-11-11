from math import sqrt

class Ponto:
    
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    @property
    def x (self):
        return self.__x

    @property
    def y (self):
        return self.__y
    
    def __str__(self):
        return f"({self.__x:.2f}, {self.__y:.2f})"

class Poligono:
    
    def __init__(self, pontos):
        self.__pontos = pontos
    
    @property
    def pontos(self):
        return self.__pontos
    
    def perimetro(self):
        p = 0
        n = len(self.__pontos)
        for i in range(n):
            x1 = self.__pontos[(i + 1) % n].x
            y1 = self.__pontos[(i + 1) % n].y
            x0 = self.__pontos[i % n].x
            y0 = self.__pontos[i % n].y
            p += sqrt((x1 - x0)**2 + (y1 - y0)**2)
        return p
    
    def area(self):
        total = 0
        n = len(self.__pontos)
        for i in range(n):
            x0 = self.__pontos[i].x
            y0 = self.__pontos[i].y
            x1 = self.__pontos[(i + 1) % n].x
            y1 = self.__pontos[(i + 1) % n].y
            total += (x0 * y1 - x1 *y0)
        return total/2
    
quadrado = Poligono([Ponto(1, 1), Ponto(3, 1), Ponto(3, 3), Ponto(1 ,3)])
print(quadrado.perimetro(), quadrado.area())