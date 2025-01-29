class Puntos:
    def __init__(self):
        self.x = float(input("Introduce la coordenada x: "))
        self.y = float(input("Introduce la coordenada y: "))


class Dist:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2
        self.res = 0

    def calcular(self):
        numerosX = self.punto2.x - self.punto1.x
        numerosY = self.punto2.y - self.punto1.y
        self.res = (numerosX**2 + numerosY**2) ** 0.5

    def mostrar_res(self):
        print(f"La distancia entre los puntos es: {self.res:.2f}")


print("Introduce las coordenadas del primer punto:")
punto1 = Puntos()

print("Introduce las coordenadas del segundo punto:")
punto2 = Puntos()

distancia = Dist(punto1, punto2)
distancia.calcular()
distancia.mostrar_res()
