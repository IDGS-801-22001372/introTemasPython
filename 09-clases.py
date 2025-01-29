class OperasBas:
    # Declaración de propiedades
    num1 = 0
    num2 = 0
    res = 0

    # Declaración del constructor
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # Declaración de métodos de clase
    def suma(self):
        self.res = self.num1 + self.num2
        print("La suma es: {}".format(self.res))

    def resta(self):
        self.res = self.num1 - self.num2
        print("La resta es: {}".format(self.res))


def main():
    obj = OperasBas(3, 4)
    obj.suma()  # Se corrigió el nombre del método


if __name__ == "__main__":
    main()
