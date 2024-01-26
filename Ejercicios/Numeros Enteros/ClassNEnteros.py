class NumeroEntero:
    def __init__(self, valor):
        self.valor = valor

    def sumar(self, otro_numero):
        resultado = self.valor + otro_numero.valor
        return NumeroEntero(resultado)

    def restar(self, otro_numero):
        resultado = self.valor - otro_numero.valor
        return NumeroEntero(resultado)

    def multiplicar(self, otro_numero):
        resultado = self.valor * otro_numero.valor
        return NumeroEntero(resultado)

    def dividir(self, otro_numero):
        if otro_numero.valor == 0:
            print("No es posible dividir por cero.")
            return None
        resultado = self.valor / otro_numero.valor
        return NumeroEntero(int(resultado))
    
    def contarDigitos(self):
        return len(str(self.valor))
    
    def invertirDigito(self, valor):
        return int(str(valor)[::-1])
    
    def mostrarCantidadPares(self):
        cantidad = 0
        for i in str(self.valor):
            if int(i) % 2 == 0:
                cantidad += 1
        return cantidad
    

