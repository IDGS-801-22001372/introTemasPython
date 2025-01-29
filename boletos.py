class Boletos:

    precioBoleto = 12.00
    maxBoletosPersona = 7
    
    def __init__(self, nombre, numPersonas, cantidadBoletos, tarjetaCinepolis):
        self.nombre = nombre
        self.numPersonas = numPersonas
        self.cantidadBoletos = cantidadBoletos
        self.tarjetaCinepolis = tarjetaCinepolis
    
    def descuento(self, total):
        descuento = 0
        
        if self.cantidadBoletos > 5:
            descuento = total * 0.15
        elif 3 <= self.cantidadBoletos <= 5:
            descuento = total * 0.10
        
        totalDescuento = total - descuento
        
        if self.tarjetaCinepolis:
            descuentoTarjeta = totalDescuento * 0.10
            totalDescuento -= descuentoTarjeta
        
        return totalDescuento
    
    def total(self):
        boletosDisponibles = self.numPersonas * self.maxBoletosPersona
        if self.cantidadBoletos < 1 or self.cantidadBoletos > boletosDisponibles:
            return "Cantidad de boletas no válida."
        
        total = self.cantidadBoletos * self.precioBoleto
        totalFinal = self.descuento(total)
        return totalFinal
    
    def resumen(self):
        totalPagar = self.total()
        resumen = f"Cliente: {self.nombre}\n"
        resumen += f"Numero de personas: {self.numPersonas}\n"
        resumen += f"Cantidad de boletos: {self.cantidadBoletos}\n"
        resumen += f"Usa tarjeta Cinepolis: {'Si' if self.tarjetaCinepolis else 'No'}\n"
        resumen += f"Total a pagar: ${totalPagar:.2f}\n"
        
        print(resumen)
        
        return resumen

def menu():
    transacciones = [] 

    while True:
        print("\nMenú:")
        print("1. Comprar boletos")
        print("2. Salir")
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "2":
            with open("Tickets.txt", "w") as texto:
                for transaccion in transacciones:
                    texto.write(transaccion + "\n" + "-"*40 + "\n")
            print("Gracias por su visita. ¡Hasta luego!")
            break
        elif opcion == "1":
            nombre = input("Ingrese su nombre: ")

            while True:
                num_personas = int(input("Ingrese cuantas personas van: "))
                #validacion boletos
                if num_personas < 1:
                    print("El número de personas debe ser mayor que 0. Intente nuevamente.")
                else:
                    break 

            while True:
                max_boletos = num_personas * Boletos.maxBoletosPersona
                cantidad_boletos = int(input(f"Ingrese la cantidad de boletos a comprar (máximo {max_boletos}): "))
                #validacion boletos
                if cantidad_boletos < num_personas:
                    print("No puedes comprar menos boletos que las personas que van. Intenta nuevamente.")
                elif cantidad_boletos > max_boletos:
                    print(f"No puedes comprar más de {max_boletos} boletos. Intenta nuevamente.")
                elif cantidad_boletos < 1:
                    print("La cantidad de boletos debe ser mayor que 0. Intente nuevamente.")
                else:
                    break

            while True:
                usa_tarjeta_cinepolis = input("¿Usará tarjeta Cinepolis? (s/n): ").strip().lower()
                if usa_tarjeta_cinepolis == 's':
                    usa_tarjeta = True
                    break
                elif usa_tarjeta_cinepolis == 'n':
                    usa_tarjeta = False
                    break
                else:
                    #validacion de si o no
                    print("Opción no válida. Por favor ingrese 's' o 'n'.")

            compra = Boletos(nombre, num_personas, cantidad_boletos, usa_tarjeta)
            resumen = compra.resumen()
            transacciones.append(resumen)
        else:
            print("Opción no válida, intente nuevamente.")

def main():
    menu()

if __name__ == "__main__":
    main()
