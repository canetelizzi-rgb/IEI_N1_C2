opcion_valida = True
suma_total = 0
while opcion_valida == True:
    try:
        num_usuario = int(input('ingrese sus numeros'))
        if num_usuario != 0:
            suma_total = suma_total + num_usuario
        else:
            opcion_valida = False
    except ValueError:
        print('Debes ingresar un numero')

print(f'la suma total de los numeros ingresados es: {suma_total}')