def verificar_iguales(a, b, c):
    """Verifica si la suma de dos números es igual al tercero."""
    return (a + b == c) or (a + c == b) or (b + c == a)

def main():
    # Solicitar los tres números al usuario
    a = int(input("Ingresa el primer numero: "))
    b = int(input("Ingresa el segundo numero: "))
    c = int(input("Ingresa el tercer numero: "))
    
    # Verificar las condiciones
    if verificar_iguales(a, b, c):
        print("Iguales")
    else:
        print("Distintas")

if __name__ == "__main__":
    main()
