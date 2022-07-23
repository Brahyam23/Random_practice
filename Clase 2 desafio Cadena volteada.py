#Dar vuelta a una cadena usando Slice

cadena = "BrahyamLeiva15Matemáticas"
print("Dar vuelta a la cadena:")
cadena_volteada = cadena[::-1]
print(cadena_volteada)

print("\nNombre y apellido:")
nombre_alumno= cadena[0:7]+" "+cadena[7:12]
print(nombre_alumno)

print("\nNota:")
nota= cadena[12:14]
print(nota)

print("\nMateria:")
materia= cadena[14:-1]
print(materia,"\n")

print(nombre_alumno," ha sacado un ", nota, " en ", materia)

cadena_formateada= materia[::-1]+" ,"+nota[::-1]+" ,"+nombre_alumno[::-1]
print("\n",cadena_formateada)
