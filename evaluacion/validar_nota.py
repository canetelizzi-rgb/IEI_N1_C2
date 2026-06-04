opcion_valida = True
while opcion_valida == True:
    try:
        nota_usuario = float(input('ingrese una nota entre 1.0 y 7.0'))
        if nota_usuario >= 1.0 and nota_usuario <= 7.0:
            print(f'tu nota es valida {nota_usuario}')
            opcion_valida = False
        else:
            print('ingresa nuevamente, tu nota debe estar entre 1.0 y 7.0')
    except ValueError:
        print('Debes ingresar un numero')
         
