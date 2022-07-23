#Utilizando la función range() y la conversión a
#listas genera las siguientes listas dinámicamente:

#Todos los números del 0 al 10 [0, 1, 2, ..., 10]
print("Lista de todos los números del 0 al 10 ")
num_1=[]

for i in range(0,11):
    num_1.append(i)

print(num_1)

#Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
print("\nLista de todos los números del -10 al 0 ")
num_2=[]

for i in range(-10,1):
    num_2.append(i)

print(num_2)

#Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
print("\nLista de todos los números pares del 0 al 20 ")
num_3=[]

for i in range(0,21,2):
    num_3.append(i)

print(num_3)

#Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
print("\nLista de todos los números impares entre -20 y 0 ")
num_4=[]

for i in range(-19,1,2):
    num_4.append(i)

print(num_4)

#Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
print("\nLista de todos los números múltiples de 5 del 0 al 50")
num_5=[]

for i in range(0,51,5):
    num_5.append(i)

print(num_5)
