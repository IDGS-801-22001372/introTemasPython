x=0

while x<10:
    print(x)
    x=x+1

        # operacion de multiplicacion de a x b utilizando sumas
        # a=3
        # b=4
        # salida: 3+3+3+3=12

a = 3
b = 4

resultado = 0
contador = 0
sumas = ""

while contador < b:
    resultado += a
    sumas += str(a)
    contador += 1
    if contador < b:
        sumas += "+"

sumas += "=" + str(resultado)

print(sumas)

