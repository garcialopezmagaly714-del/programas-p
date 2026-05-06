# p159-rectangulo
# Clase que modela un rectángulo

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def obtenerArea(self):
        return self.largo * self.ancho

    def obtenerPerimetro(self):
        return 2 * self.largo + 2 * self.ancho

    def __str__(self):
        return f'Rectangulo[Largo={self.largo}, Ancho={self.ancho}, Area={self.obtenerArea():.2f}, Perimetro={self.obtenerPerimetro():.2f}]'


# Programa principal
r1 = Rectangulo(12, 3.4)
print('\nPrimer rectángulo:', r1)
print(f'Área: {r1.obtenerArea():.2f}')
print(f'Perímetro: {r1.obtenerPerimetro():.2f}')

r2 = Rectangulo(5.6, 7.8)
print('\nSegundo rectángulo:', r2)
print(f'Área: {r2.obtenerArea():.2f}')
print(f'Perímetro: {r2.obtenerPerimetro():.2f}')