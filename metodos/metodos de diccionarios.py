datos_personales = {
    "nombre": "elizabet cañete",
    "edad":20,
    "titulo":"ingeniero informatico"
}

print(len(datos_personales))

print()
# el metodo KEYS permite obtener las CLAVES de un diccionario
claves = datos_personales.keys()
print(claves)

print()
# el metodo VALUES permite obtener los valores de un diccionario
valores = datos_personales.values()
print(valores)

print()
# el metodo get permite obtener el VALOR de un elemento mediante su clave
nombre_personal = datos_personales.get("nombre")
print(nombre_personal.title)

# el metodo items permite obtener cada uno de los pares de elementos
print(datos_personales.items())

# para agregar un nuevo elemento a un diccionario 
# debemos definir su clave y su valor
datos_personales{"es profesor?"} = True
print(datos_personales)

print()
# el metodo pop elimina un elemento por su clave
datos_personales.pop('es profesor')
print(datos_personales)

print()
# el metodo clear elimina todos los elementos de un diccionario
datos_personales.clear()
print(datos_personales)
