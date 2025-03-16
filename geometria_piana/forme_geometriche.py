class Quadrato:
    def __init__(self, lato):
        self.lato = lato

    def perimetro(self):
        return 4 * self.lato

class Rettangolo:
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def perimetro(self):
        return 2 * (self.base + self.altezza)

class Cerchio:
    def __init__(self, raggio):
        self.raggio = raggio

    def perimetro(self):
        import math
        return 2 * math.pi * self.raggio

class Trapezio:
    def __init__(self, base_maggiore, base_minore, altezza):
        self.base_maggiore = base_maggiore
        self.base_minore = base_minore
        self.altezza = altezza

    def perimetro(self):
        import math
        base_diff = (self.base_maggiore - self.base_minore) / 2
        lato_obliquo = math.sqrt(base_diff**2 + self.altezza**2)
        return self.base_maggiore + self.base_minore + 2 * lato_obliquo

class Triangolo:
    def __init__(self, lato1, lato2, lato3):
        self.lato1 = lato1
        self.lato2 = lato2
        self.lato3 = lato3

    def perimetro(self):
        return self.lato1 + self.lato2 + self.lato3
