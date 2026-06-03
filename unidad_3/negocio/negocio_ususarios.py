from datos import listado_usuarios
from prettytable import prettytable

def obtener_listado_usuarios():
    tabla_usuarios = prettytable()
    tabla_usuarios.field_names ['nombre','rut','telefono','email','tipo_usuario']

    for usuario in listado_usuarios:
        tabla_usuarios.add_row([usuario['nombre'], usuario['rut'], usuario['telefono'], usuario['email'], usuario['tipo_usuario']])
    
    return tabla_usuarios
