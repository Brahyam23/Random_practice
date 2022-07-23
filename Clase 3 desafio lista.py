lista1 = [1, 12, 123]
lista2 = ["Bye", "Ciao", "Agur", "Adieu"]

lista1.append(1234)
lista1.append("Hola")

lista2.append("Adios")
lista2.append(1234)

lista3 = lista1[:-1]
lista4 = lista2[1:-1]
lista5 = lista3+lista4
print(lista3)
print(lista4)
print(lista5)
