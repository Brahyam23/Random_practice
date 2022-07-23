#Escribí un programa que pida al usuario un número entero del 0 al 9, y que
#mientras el número no sea correcto se repita el proceso. Luego debe comprobar
#si el númerose encuentra en la lista de números y notificarlo

num = int(input("Bienvenido. Por favor, introduzca un número entero entre 0 y 9: "))
numeros = [1, 3, 6, 9]
while True:
    if 0 <= num <= 9:
        print("\nPerfecto, has introducido un valor válido.",end="")
        break
    else:
        num = int(input("""\nUh, lo siento. Al parecer has introducido un valor fuera del rango.
Intenta de nuevo introducir un valor entero entre 0 y 9: """))
print(" Ahora comprobaremos si el numero que elegiste se encuentra dentro de la siguiente lista:",numeros)

if num in numeros:
    print("\nFelicitaciones! Tu número se encuentra registrado en la lista.")
else:
    print("\nUh, lo siento. Parece que tu número no se encuentra registrado en la lista.")
