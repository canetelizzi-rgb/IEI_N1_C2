# Colecciones de DATOS

# LISTAS => list
# Es una colección ORDENADA y MUTABLE de datos de cualquier tipo

print('Listas en Python')
mi_primera_lista = ['elizabet cañete ',20,True]

nombre_personal = input('Ingrese su nombre: ')
print(type(mi_primera_lista))
print(mi_primera_lista)
print(f'El primer elemento de la lista es: {mi_primera_lista[0]}')
mi_primera_lista[0] = nombre_personal
print(mi_primera_lista)

mi_primera_lista.append(25)
print(mi_primera_lista)
mi_primera_lista.remove(25)
print(mi_primera_lista)

# DICCIONARIOS dictionary => dict
# Es una colección ORDENADA y MUTABLE de pares de datos de cualquier tipo
# los datos de un diccionario ocupan el doble de espacio en memoria
# deben almacenar la CLAVE y el VALOR de cada dato

print(DICCIONARIOS)
mi_primer_diccionario = {'nombre':'elizabet cañete','edad':50,'asistio a clase hoy?':True}
print(type(mi_primer_diccionario))
print(mi_primer_diccionario)

print(mi_primer_diccionario["nombre"])
mi_primer_diccionario['nombre'] = nombre_personal
print( mi_primer_diccionario)
mi_primer_diccionario['Esta feliz?']=True
print(mi_primer_diccionario)
print(dir(mi_primer_diccionario))
# mi_primer_diccionario_modificado = mi_primer_diccionario.clear()
# print(mi_primer_diccionario_modificado)

# CONJUNTOS set
# es una coleccon DESORDENADA e INMUTABLE de datos de cualquier tipo
# principalmente para área matematica

mi_primer_conjunto = {¨dato 1¨,45,false}
print(type(mi_primer_conjunto))
print(mi_primer_diccionario)
mi_primer_conjunto.add(25)
print(mi_primer_conjunto)

# TUPLAS tuple
# es una coleccion ORDENADA e INMUTABLE de datos de cualquier tipo 

print(TUPLAS)
mi_primera_tupla =(´Elizabet cañete,20,true)
print(type(mi_primera_tupla))
print(mi_primera_tupla{0})

# la tupla no permite asignar un nuevo valor para los elementos 