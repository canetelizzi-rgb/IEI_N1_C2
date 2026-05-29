from datos import listado_rifas
from prettytable import PrettyTable

def obtener_listado_rifas():
    tabla_rifas = PrettyTable()
    tabla_rifas.field_names = ['Nombre','Fecha Creación','Precio Número','Cantidad Rifas','Fecha Lanzamiento']

    for rifa in listado_rifas:
        tabla_rifas.add_row([rifa['nombre'], rifa['fecha_creacion'], f'${rifa['precio']}', rifa['cantidad_rifas'], rifa['fecha_lanzamiento']])
    
    return tabla_rifas