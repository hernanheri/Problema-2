# Solicitar los tres números al usuario
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))

# Verificar las condiciones
if (a + b == c) or (a + c == b) or (b + c == a):
    print("Iguales")
else:
    print("Distintas")
