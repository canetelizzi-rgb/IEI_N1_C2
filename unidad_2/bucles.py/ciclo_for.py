# Ciclo FOR para recorrer colecciones de elementos

lista_juegos = ['Dota 2','CS2','Plantas V/S Zombies','Expedition 33']
lista_numeros = [1,5,89,42,63]
nombre = 'Aquiles Baeza'

for letra in nombre:
    if letra == 'a':
        letra = letra.upper()
    if letra == ' ':
        letra = '-'
    print(letra)

print()
for elemento in lista_juegos:
    elemento = elemento.upper()
    print(elemento)

print(f'\nRecorriendo la lista de números = {lista_numeros}')
for numero in lista_numeros:
    resultado = numero * numero
    print(f'{numero} X {numero} = {resultado}')

conjunto_animales = {'perro','gato','ornitorrinco','murciélago'}
print()
for animal in conjunto_animales:
    print(animal)

tupla_datos_personales = ('Wendy Sulca',25,'peruana','cantante')
print()
for dato in tupla_datos_personales:
    print(dato)

diccionario_asignaturas = {
    'codigo':'TI3011',
    'nombre':'Introducción a la Programación Segura',
    'seccion':'IEI-N1-C2',
    'alumnos':20
}
print()
for elemento in diccionario_asignaturas:
    print(elemento)
print()
for elemento in diccionario_asignaturas.items():
    clave = elemento[0]
    valor = elemento[1]
    print(f'Clave: {clave} - Valor: {valor}')
print()
for elemento in diccionario_asignaturas.items():
    print(elemento[1])

# RANGE es un método que crea un rango de número
# Si a range le paso 1 argumento, crea un rango de números con esa cantidad de elementos
lista_numeros_rango = range(5)
print()
print(lista_numeros_rango)
for numero in lista_numeros_rango:
    print(numero)

# Si a range le paso 2 argumentos, el primero será el número inicial y el segundo el final -1
lista_numeros_rango2 = range(5,26)
print()
print(lista_numeros_rango2)
for numero in lista_numeros_rango2:
    print(numero)
    
# Si a range le paso 2 argumentos, el primero será el número inicial, el segundo el final -1 y el tercero será el PASO, 
# cada cuanto aumento el siguiente número
lista_numeros_rango3 = range(5,26,5)
print()
print(lista_numeros_rango3)
for numero in lista_numeros_rango3:
    print(numero)