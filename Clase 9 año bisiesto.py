
#Realizar una funcion que permita saber si un año es bisiesto:

def anio_bisiesto (anio:int): #Definimos función

    if isinstance(anio, int): #Verificamos si el argumento recibido es un número
    
        if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0): #Verificamos si cumple con las condiciones
            print(f"El año {anio} es bisiesto.")
    
        else:
            print(f"El año {anio} no es bisiesto.")
        
    else: #Si el argumento recibido no es un número, avisamos por pantalla
        print("No es un número")
        return

anio_bisiesto(2000)