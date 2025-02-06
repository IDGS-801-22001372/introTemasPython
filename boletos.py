class Boletos:

    precioBoleto = 12.00
    maxBoletosPersona = 7
    
    #logica de totales y descuentos
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
            return "Cantidad de boletos no valida."
        
        total = self.cantidadBoletos * self.precioBoleto
        totalFinal = self.descuento(total)
        return totalFinal
    
    def resumen(self):
        totalPagar = self.total()
        resumen = f"\nCliente: {self.nombre}\n"
        resumen += f"Numero de personas: {self.numPersonas}\n"
        resumen += f"Cantidad de boletos: {self.cantidadBoletos}\n"
        resumen += f"Metodo de Pago: {'Tarjeta Cinepolis' if self.tarjetaCinepolis else 'Efectivo'}\n"
        resumen += f"Total a pagar: ${totalPagar:.2f}\n"
        
        print(resumen)
        
        return resumen, totalPagar

#funcion para piedir solo numeros donde sea necesario
def pedir_numero(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit():
            return int(valor)
        else:
            print("Por favor ingrese un valor numerico valido.")

def menu():
    transacciones = [] 
    totalGeneral = 0

    #se crea el documento txt
    with open("Tickets.txt", "w") as texto:
        pass

    while True:
        print("\nMenu:")
        print("1. Comprar boletos")
        print("2. Salir")
        opcion = input("Seleccione una opcion: ")

        #si la opcion es 2 se hace el corte de caja con las transacciones 
        if opcion == "2":
            print("\nResumen del dia:")
            for resumen, totalPagar in transacciones:
                print(resumen)
                print("----------------------------")

            print(f"\nTotal acumulado de todos los tickets: ${totalGeneral:.2f}")
            print("\nGracias por su visita.")

            with open("Tickets.txt", "a") as texto:
                texto.write("\nResumen del dia:\n")
                for resumen, totalPagar in transacciones:
                    texto.write(resumen + "\n----------------------------\n")
                
                texto.write(f"\nCorte de venta, total de tickets: ${totalGeneral:.2f}\n")
            
            break
        #SI ES 1 TE MANDA AL MENU
        elif opcion == "1":
            nombre = input("Ingrese su nombre: ")

            num_personas = pedir_numero("Ingrese cuantas personas van: ")
            while num_personas < 1:
                #no deja ingresar  0 peronsas
                print("El numero de personas debe ser mayor que 0. Intente nuevamente.")
                num_personas = pedir_numero("Ingrese cuantas personas van: ")

            max_boletos = num_personas * Boletos.maxBoletosPersona
            cantidad_boletos = pedir_numero(f"Ingrese la cantidad de boletos a comprar (maximo {max_boletos}): ")

            while cantidad_boletos < num_personas or cantidad_boletos > max_boletos:
                if cantidad_boletos < num_personas:
                    print("No puedes comprar menos boletos que las personas que van. Intenta nuevamente.")
                else:
                    print(f"No puedes comprar mas de {max_boletos} boletos.")
                    opcion = input("¿Quieres cambiar el numero de personas para poder comprar esta cantidad? (s/n): ").strip().lower()
                    if opcion == 's':
                        num_personas = pedir_numero("Ingrese un nuevo numero de personas: ")
                        while num_personas < 1:
                            print("El numero de personas debe ser mayor que 0. Intente nuevamente.")
                            num_personas = pedir_numero("Ingrese un nuevo numero de personas: ")

                        max_boletos = num_personas * Boletos.maxBoletosPersona
                        if cantidad_boletos <= max_boletos:
                            print(f"Ajuste realizado. Ahora puedes comprar {cantidad_boletos} boletos.")
                            break  
                        else:
                            print(f"Aun no puedes comprar {cantidad_boletos} boletos con {num_personas} personas.")
                    else:
                        cantidad_boletos = pedir_numero(f"Ingrese la cantidad de boletos a comprar (maximo {max_boletos}): ")

            print("Metodo de Pago:")
            print("1. Efectivo")
            print("2. Tarjeta Cinepolis")

            while True:
                metodoPago = input("Selecciona una opcion: ")
                
                if metodoPago == '1' or metodoPago == '2':
                    usa_tarjeta = metodoPago == '2' 
                    break
                else:
                    print("Opcion no valida. Por favor ingrese '1' o '2'.")

            compra = Boletos(nombre, num_personas, cantidad_boletos, usa_tarjeta)
            resumen, totalPagar = compra.resumen()
            transacciones.append((resumen, totalPagar))
            totalGeneral += totalPagar

            with open("Tickets.txt", "a") as texto:
                texto.write(f"Cliente: {nombre} - Total: ${totalPagar:.2f}\n")
                texto.write("-----------------------\n")

        else:
            print("Opcion no valida, intente nuevamente.")

def main():
    menu()

if __name__ == "__main__":
    main()
