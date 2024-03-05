def is_palindrome(string: str) -> bool: # type hinting -> indica el tipo de dato que se espera
    string = string.replace(' ', '').lower() # Elimina los espacios y convierte a minúsculas
    return string == string[::-1] # Compara el string con su inverso y devuelve True o False

def run(): # Función principal que ejecuta el programa principal
    print(is_palindrome(1000)) # False
    print(is_palindrome('ana')) # True
    print(is_palindrome('Ana')) # True
    print(is_palindrome('Ana ana')) # True
    print(is_palindrome('Ana ana!')) # True

if __name__ == '__main__': # Si el archivo es ejecutado directamente, se ejecuta la función run
    run() # Ejecuta la función run