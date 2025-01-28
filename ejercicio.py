class Puntos:
    def __init__(self,x,y):
        self.x=float(input)
        self.y=y

class Dist:
    def __init__(self,punto1,punto2):
        self.punto1=punto1
        self.punto2=punto2
        self.res=0

    def calcular(self):
        numerosX= self.punto2.x - self.punto1.x
        numerosY= self.punto2.y - self.punto1.y
        self.res=(numerosX**2 + numerosY**2)**0.5

    def res(self):
        print(f"la distrancia entre los puntos es: {self.res:.2f}")






