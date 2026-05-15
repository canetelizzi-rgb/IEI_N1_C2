lista_animales = {"perro","gato","delfín","pantera"}
lista_compras = {"cepillo","pasta de dientes","jabon"}
lista_numeros = {5,45,1,25,265,17826}

print(type(lista_animales))

# El metodo LEN (length, largo= tamaño) permite conocer la cantidad de elementos en una lista
print(len(lista_animales))

# el metodo append agrega un nuevo elemento al final de la lista

nuevo_animal =input('agregue un nuevo animal a la lista: ')
lista_animales.append(nuevo_animal)
print(len(lista_animales))
print(lista_animales)

# el metodo insert permite agregar un elemto en un lugar (indice) en un lugar especifico
otro_animal = input("agrege un nuevo animal a la lista: ")
lista_animales.insert(2,otro_animal)
print(len(lista_animales))
print(lista_animales)

print()

# el metodo extend permite agregar varios elementos a una lista 
# agregamos una lista ya creada, uniendo ambas listas 
lista_animales.extend(lista_compras)
print(len(lista_animales))
print(lista_animales)

# agregamos una ista manuealmente
lista_animales.extend({"oso pardo","panda","oso polar"})
print(len(lista_animales))
print(lista_animales)

print()
# el metodo POP perite eliminar elementos de una lista 
# si al metodo POP no se le entregan elementos, elimina el ultimo elemento de una lista
lista_animales.pop()
print(len(lista_animales))
print(lista_animales)

# Si al metodo pop le indico el argumento indice, elimina el elemento especificado
lista_animales.pop(0)
print(len(lista_animales))
print(lista_animales)

#si al metodo pop le indico el argumento indice -1, elimina el ultimo elemento de la lista
lista_animales.pop(-1)
print(len(lista_animales))
print(lista_animales)

print()
# el metodo remove elimina un elemento por su valor
lista_animales.remove("oso pardo")
print(len(lista_animales))
print(lista_animales)

#El metodo clear elimina todos los elementos de una lista 
lista_animales.clear()
print(len(lista_animales))
print(lista_animales)

print()
# el metodo sort ordena una lista alfabeticamente
lista_compras.sort()
print(len(lista_compras))
print(lista_compras)

# el metodo reverse ordena la lista al revés 
lista_compras.revese()
print(lista_compras)

# El metodo reverse ordena la lista de numeros de manera descendente 
lista_numeros.reverse()
print(lista_numeros)