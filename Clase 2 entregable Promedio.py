print("===========================================================================")
print("Bienvenido al programa para calcular la calificación final de un estudiante")
print("===========================================================================\n")

nombre = input("Por favor, inserte el nombre del estudiante: ")

x=True
while x==True:
    nota_1 = input("\nInserte la calificación del primer exámen: ")
    try:
        entero1 = float(nota_1)
        x=False
    except (ValueError):
        print("Error: ha introducido un valor inválido.")

x=True
while x==True:
    nota_2 = input("\nInserte la calificación del segundo exámen: ")
    try:
        entero2 = float(nota_2)
        x=False
    except (ValueError):
        print("Error: ha introducido un valor inválido.")

resultado = (40*entero1 + 60*entero2)/100
print("\nLa nota final de", nombre, "es de", resultado)
