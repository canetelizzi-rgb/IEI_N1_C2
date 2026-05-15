# Resuelva los siguientes ejercicios mediante funciones,
# las que serán llamadas dentro de un menú de opciones.
from math import pi

def solicitar_datos_personales():
    nombre = input('Ingrese su nombre: ')
    print('[H] Hombre')
    print('[M] Mujer')
    genero = input('Ingrese su Género, H para hombre o M para mujer: ')
    return nombre.title(), genero.upper()

def solicitar_datos_cilindro():
    continuar = True
    while continuar == True:
        str_radio = input('Ingrese RADIO Circunferencia: ')
        str_altura = input('Ingrese ALTURA Cilindro: ')

        radio = convertir_decimal(str_radio)
        altura = convertir_decimal(str_altura)
        if radio and altura:
            continuar = False
            return radio,altura

def convertir_decimal(texto):
    try:
        return float(texto)
    except ValueError:
        print('Valor ingresado NO se puede convertir a número, ingrese nuevamente.')
    except Exception as error:
        print(f'Error: {error}, ingrese nuevamente.')


def solicitar_numero():
    continuar = True
    while continuar == True:
        str_numero = input('Ingrese Número: ')

        numero = convertir_decimal(str_numero)
        if numero:
            continuar = False
            return numero

# 1.- Cree una función que entregue el saludo "Buen día!"
def saludo_cordial():
    saludo = "Buen día!"
    return saludo

# 2.- Cree una función que solicite el nombre y el género al usuario y luego, 
# llamando a la función anterior, salude al usuario, el saludo debe quedar así: 
# "Buen día nombre_usuario!", 
# y agregue el texto "Hoy te ves hermosa" si el usuario es mujer 
# o "cómo estás campeón?" si el usuario es hombre
def saludo_personal(nombre,genero):
    saludo = saludo_cordial()
    mensaje = ''
    '''
    saludo = saludo.replace('!','')
    saludo_split = saludo.split('!')
    '''
    if genero == 'M':
        mensaje = f'{saludo[:-1]} {nombre}!, Hoy te ves hermosa'
    elif genero == 'H':
        mensaje = f'{saludo[:-1]} {nombre}!, cómo estás campeón?'
    else:
        mensaje = 'Género inválido, ingrese nuevamente.'
    return mensaje

# 3.- Cree una función que permita calcular el área de una circunferencia 
# y otra que permita calcular el volumen de un cilindro usando la función anterior
# los datos deben ser ingresados por el usuario
def area_circunferencia(radio):
    area = pi * radio ** 2
    return area

def volumen_cilindro():
    radio,altura = solicitar_datos_cilindro()
    if radio:
        area = area_circunferencia(radio)
        if area and altura:
            volumen = area * altura
            return f'Radio: {radio}, Altura: {altura}, Volumen: {round(volumen,2)}'

# 4.- Cree una función que pida un número entero al usuario 
# y calcule el factorial de ese número
def factorial():
    # !5 = 1*2*3*4*5
    numero_factorial = solicitar_numero()
    if numero_factorial:
        resultado = 1
        for numero in range(1,round(numero_factorial)+1):
            resultado = numero * resultado        
    return f'{numero}! = {resultado}'

# 5.- Solicite al usuario el ingreso del nombre del estudiante,
# luego solicite el ingreso de las notas del estudiante,
#calcular el promedio del estudiante y mostrar su situacon final 
# aprobado (nota >=4.0) o reprobado (nota < 4.0)

# la salida debe ser la siguiente:
# nombre: nombre_estudiante
# Notas: notas 
# promedio: promedio
# situacion final: Aprobado/reprobado
# nombre_estudiante
nombre_estudiante=input('ingrese su nombre y apellido')

# nota
notas_profesor= int(input('cuantas notas debe ingresar el estudiante?'))

def calcular_promedio():
    nombre_estudiante = solicitar_nombre('Ingrese nombre estudiante: ')
    notas_estudiante = []
    cantidad_notas = solicitar_numero('Ingrese la cantidad de notas: ')

    contador = 1
    while len(notas_estudiante) < cantidad_notas:
        nota = solicitar_numero(f'Ingrese nota {contador}: ')
        if 1 < nota <= 7.0:
            # notas_estudiante.insert(i,nota)
            notas_estudiante.append(nota)
            contador += 1

    promedio = sum(notas_estudiante)/len(notas_estudiante)
    situacion_final = ''
    if promedio >= 4.0:
        situacion_final = 'Aprobado'
    else:
        situacion_final = 'Reprobado'
    
    resultado = f'''
Nombre: {nombre_estudiante}
Notas: {notas_estudiante}
Promedio: {round(promedio,1)}
Situación Final: {situacion_final}
'''
    return resultado

def calcular_promedio():
    resultado = f'''
Nombre: nombre_estudiante
Notas: notas
Promedio: promedio
Situación Final: Aprobado/Reprobado
'''
    return resultado

def menu_principal():
    opciones_menu = ['Saludo','Saludo Personal','Volumen Cilindro','Calcular Factorial','Calcular Promedio']
    contador = 1
    while True:      
        print()
        for opcion_menu in opciones_menu:
            print(f'[{contador}] {opcion_menu}')
            contador += 1
        print('[0] Salir')

        opcion = input(f'Seleccione su opción [0-{len(opciones_menu)}]: ')
        opciones_validas = ['0','1','2','3','4','5']

        if opcion in opciones_validas:
            if opcion != '0':
                if opcion == '1':
                    resultado = saludo_cordial()
                elif opcion == '2':
                    nombre,genero = solicitar_datos_personales()
                    resultado = saludo_personal(nombre,genero)
                elif opcion == '3':
                    resultado = volumen_cilindro()
                elif opcion == '4':
                    resultado = factorial()
                elif opcion=='5':
                    resultado = calcular_promedio()
                print(f'\n{resultado}')
            else:
                print('Saliendo del sistema...')
                break
        else:
            print('Opción NO corresponde, ingrese nuevamente...')

menu_principal()