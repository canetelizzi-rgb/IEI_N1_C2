contador_pares = 0  
total_numeros_pedir = 10

print(f"Ingrese {total_numeros_pedir} números enteros")

for numero_actual in range(1, total_numeros_pedir + 1):
    try:
        numero_usuario = int(input(f"Número {numero_actual}/{total_numeros_pedir}: "))
        es_par = numero_usuario % 2 == 0 
        if es_par:
            contador_pares += 1           
    except ValueError:
        print("Debes ingresar solo números enteros. Este intento no se cuenta.")

print(f"Total de números pares ingresados: {contador_pares}")
