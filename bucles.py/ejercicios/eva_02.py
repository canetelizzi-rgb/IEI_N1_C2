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
        for numero in range(1,round(numero_factorial)+1):
            resultado = 1
            resultado = numero * resultado        
    return f'{numero}! = {resultado}'

def menu_principal():
    while True:        
        print()
        print('[1] Saludo')
        print('[2] Saludo Personal')
        print('[3] Volumen Cilindro')
        print('[4] Calcular Factorial')
        print('[0] Salir')
        opcion = input('Seleccione su opción [0-4]: ')
        opciones_validas = ['0','1','2','3','4']

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
                print(f'\n{resultado}')
            else:
                print('Saliendo del sistema...')
                break
        else:
            print('Opción NO corresponde, ingrese nuevamente...')

menu_principal()