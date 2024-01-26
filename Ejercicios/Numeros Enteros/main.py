from ClassNEnteros import NumeroEntero

def mostrar_menu():
    print("\n------ MENÚ ------")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Contar Dígitos")
    print("6. Invertir Dígitos")
    print("7. Cantidad de Dígitos Pares")
    print("0. Salir")

if __name__ == '__main__':
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (0-10): ")

        if opcion == "0":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        elif opcion == "1":
            valor1 = int(input("Ingrese el valor para num1: "))
            num1 = NumeroEntero(valor1)
            valor2 = int(input("Ingrese el valor para num2: "))
            num1 = NumeroEntero(valor1)
            suma = num1.sumar(num2)
            print("Suma:", suma.valor)
        elif opcion == "2":
            valor1 = int(input("Ingrese el valor para num1: "))
            num1 = NumeroEntero(valor1)
            valor2 = int(input("Ingrese el valor para num2: "))
            num1 = NumeroEntero(valor1)
            resta = num1.restar(num2)
            print("Resta:", resta.valor)
        elif opcion == "3":
            valor1 = int(input("Ingrese el valor para num1: "))
            num1 = NumeroEntero(valor1)
            valor2 = int(input("Ingrese el valor para num2: "))
            num1 = NumeroEntero(valor1)
            multiplicacion = num1.multiplicar(num2)
            print("Multiplicación:", multiplicacion.valor)
        elif opcion == "4":
            valor1 = int(input("Ingrese el valor para num1: "))
            num1 = NumeroEntero(valor1)
            valor2 = int(input("Ingrese el valor para num2: "))
            num1 = NumeroEntero(valor1)
            division = num1.dividir(num2)
            print("División:", division.valor)
        elif opcion == "5":
            valor1 = int(input("Ingrese el valor: "))
            num1 = NumeroEntero(valor1)
            print("Cantidad de dígitos:", num1.contarDigitos())
        elif opcion == "6":
            valor1 = int(input("Ingrese el valor: "))
            num1 = NumeroEntero(valor1)
            print("Invertir dígitos:", num1.invertirDigito(valor1))
        elif opcion == "7":
            valor1 = int(input("Ingrese el valor: "))
            num1 = NumeroEntero(valor1)
            print("Cantidad de dígitos pares:", num1.mostrarCantidadPares())
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
