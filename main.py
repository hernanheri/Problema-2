from src.verificacion import verificar_iguales

def main():
    # Solicitar los tres números al usuario
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    c = int(input("Ingresa el tercer número: "))
    
    # Verificar las condiciones
    if verificar_iguales(a, b, c):
        print("Iguales")
    else:
        print("Distintas")

if __name__ == "__main__":
    main()
