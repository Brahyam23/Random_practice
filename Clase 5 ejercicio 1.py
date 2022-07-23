# Escribí un programa que lea dos números por
# teclado y permita elegir entre 4 opciones en un menú:

# 1 Mostrar una suma de los dos números
# 2 Mostrar una resta de los dos números (el primero menos el segundo)
# 3 Mostrar una multiplicación de los dos números
# 4 Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
# 5 En caso de no introducir una opción válida, el programa informará de que no es correcta.

#Saludamos al usuario"
print("Hola! Bienvenido a la calculadora de Brahyam\n")
print("Que operación desea realizar?")

#Creamos bucle y pedimos que seleccione alguna opción del menú
while True:
    menu = int(input("""
1) Sumar dos números
2) Restar dos números
3) Multiplicar dos números
4) Salir\n"""))
#De haber elegido 1, se suman los dos números que desee y se muestran en pantalla
    if menu == 1:
               
        print("Ha seleccionado suma.\n")
        num_1 = int(input("Ingrese el primer valor: "))
        num_2 = int(input("Ingrese el segundo valor: "))
        print("El resultado de la suma es:", num_1+num_2)
        print("\nDesea realizar algo más?")

#De haber elegido 2, se restan los dos números que desee y se muestran en pantalla
    elif menu == 2:
               
        print("Ha seleccionado resta.\n")
        num_1 = int(input("Ingrese el primer valor: "))
        num_2 = int(input("Ingrese el segundo valor: "))
        print("El resultado de la resta es:", num_1-num_2)
        print("\nDesea realizar algo más?")

#De haber elegido 3, se multiplican los dos números que desee y se muestran en pantalla
    elif menu == 3:
        
        print("Ha seleccionado multiplicación.\n")
        num_1 = int(input("Ingrese el primer valor: "))
        num_2 = int(input("Ingrese el segundo valor: "))
        print("El resultado de la multiplicación es:", num_1*num_2)
        print("\nDesea realizar algo más?")

#De haber elegido 4, se termina el programa y nos despedimos del usuario
    elif menu == 4:
        print("Hasta luego. Vuelva pronto!")
        break

#Si selecciona una opcion fuera del menú, vuelve al bucle
    else:
        print("Ha elegido una opción no válida, intentelo de nuevo")
        

