class NumeroEntero:
    # Constructor
    def __init__(self, valor):
        self.valor = valor

    # Suma entera
    def sumar(self, otro_numero):
        resultado = self.valor + otro_numero.valor
        return NumeroEntero(resultado)

    # Resta entera
    def restar(self, otro_numero):
        resultado = self.valor - otro_numero.valor
        return NumeroEntero(resultado)

    # Multiplicación entera
    def multiplicar(self, otro_numero):
        resultado = self.valor * otro_numero.valor
        return NumeroEntero(resultado)

    # División entera
    def dividir(self, otro_numero):
        if otro_numero.valor == 0:
            print("No es posible dividir por cero.")
            return None
        resultado = self.valor / otro_numero.valor
        return NumeroEntero(int(resultado))
    
    # Contar la cantidad de dígitos
    def contarDigitos(self):
        return len(str(self.valor))
    
    # Invertir los dígitos
    def invertirDigito(self, valor):
        return int(str(valor)[::-1])
    
    # Mostrar la cantidad de dígitos pares
    def mostrarCantidadPares(self):
        cantidad = 0
        for i in str(self.valor):
            if int(i) % 2 == 0:
                cantidad += 1
        return cantidad
    
    # Mostrar la cantidad de dígitos impares
    def mostrarCantidadImpares(self):
        cantidad = 0
        for i in str(self.valor):
            if int(i) % 2 != 0:
                cantidad += 1
        return cantidad
    
    # Mostrar los números pares
    def mostrarNumerosPares(self):
        lista = []
        for i in str(self.valor):
            if int(i) % 2 == 0:
                lista.append(i)
        return lista
    
    # Mostrar los números impares
    def mostrarNumerosImpares(self):
        lista = []
        for i in str(self.valor):
            if int(i) % 2 != 0:
                lista.append(i)
        return lista

    # Mostrar los números primos
    def mostrarNumerosPrimos(self):
        lista = []
        for i in str(self.valor):
            if int(i) % 2 != 0:
                lista.append(i)
        return lista
    
    
# Solicitar al usuario que ingrese valores por consola
valor1 = int(input("Ingrese el valor para num1: "))
valor2 = int(input("Ingrese el valor para num2: "))

# Crear instancias de la clase NumeroEntero con los valores ingresados por el usuario
num1 = NumeroEntero(valor1)
num2 = NumeroEntero(valor2)

# Ejemplo de uso
suma = num1.sumar(num2)
#resta = num1.restar(num2)
#multiplicacion = num1.multiplicar(num2)
#division = num1.dividir(num2)

# Mostrar resultados
print("Suma:", suma.valor)
#print("Resta:", resta.valor)
#print("Multiplicación:", multiplicacion.valor)
#print("División:", division.valor)    