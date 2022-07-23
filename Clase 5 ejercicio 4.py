#Escribí un programa que pida al usuario cuantos números quiere introducir.
#Luego lee todos los números y realiza una media aritmética

#Damos la bienvenida al usuario
print("Hola! Bienvenido a la calculadora de promedio.\n")

#Pedimos datos al usuario
rep = int(input("Por favor, introduce la cantidad de numeros que deseas promediar: "))
print("\nHas elegido", rep, "números.\n")

#Definimos variables para el calculo final y creamos bucle
suma = 0
for i in range(0,rep):
    print("Ingrese el", i+1 , "° valor: ",end="")
    num = int(input(""))
    suma += num
#Mostramos resultado al usuario
print("\nEl promedio de sus números es: ", round(suma/rep,2))
