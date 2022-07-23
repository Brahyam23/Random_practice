#Escribí un programa que sume todos los
#números enteros impares desde el 0 hasta el 100

#Damos la bienvenida al programa
print("""Bienvenido, a continuacion sumaremos todos
los números enteros impares desde el 0 hasta el 100\n""")

#Creamos variable para guardar el resultado de la suma
resultado = 0

#Creamos bucle para sumar todos los numeros
for i in range(1,101,2):
    resultado += i
    print("Vamos por el número",i)
#Mostramos el resultado al usuario
print("\nEl resultado de la suma de los números impares del 0 al 100 es:",resultado)
