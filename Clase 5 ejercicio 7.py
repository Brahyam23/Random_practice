#Dadas dos listas, debes generar una tercera con todos los elementos que se
#repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista

#Creamos variables
lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_3 = []
lista_4= []
print("Lista 1°= ",lista_1)
print("Lista 2°= ", lista_2)
print("\nUnimos todos los elementos repetidos de ambas listas en una nueva:")
#Añadimos items repetidos en ambas listas a lista_3
for i in lista_1:
    for y in lista_2:
        if i == y:
            lista_3.append(i)
print(lista_3)
print("\nAhora eliminamos elementos repetidos en la nueva lista:")
#Apoyandonos de lista_4, separamos todos los items ÚNICOS de lista_3 
for i in lista_3:
    if i not in lista_4:
        lista_4.append(i)
#Igualamos
lista_3 = lista_4

#Mostramos en pantalla
print(lista_3)
        
