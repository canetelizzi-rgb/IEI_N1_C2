# ingreso contraseña mediante ciclo for

contrasena ='eureka'
for numero in range(3):
     contrasena_usuario = input('Ingrese contraseña: ')
    if contrasena_usuario == contrasena:
        print('Contraseña Correcta!')
    else:
        if numero < 2:
            print('Contraseña Incorrecta, intente nuevamente.')
        else:
            print('Contraseña Incorrecta, Cerrando Sistema!')