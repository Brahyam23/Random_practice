#Escribí un programa que lea un número impar por teclado.
#Si el usuario no introduce un número impar, debe repetirse el proceso
#hasta que lo introduzca correctamente.

#Damos la bienvenida al usuario
print("Bienvenido.",end=" ")

#Creamos el bucle
while True:

#Pedimos el dato al usiario
    num = int(input("Por favor, ingrese un número impar: "))

#Si el dato es correcto y cumple la condición, el programa continua su flujo
    if num%2 == 1:

        print("\nPerfecto!, el número '",num,"' es un número impar, el programa puede continuar")
        break

#De lo contrario, el usuario queda encerrado en un bucle para el resto de su vida por desobediente
    else:
        
        print("\nUh, lo siento. Parece que '",num,"' no es un número impar. Inténtalo de nuevo.\n") 
print("\nHasta luego, gracias por tu colaboración!")
