import csv
import json
import logging
# Configuración del sistema de logs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(filename)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("logs/ventas.log"), # Guarda el log en la carpeta logs
        logging.StreamHandler() # Muestra el log también por la terminal
    ]
)
logger = logging.getLogger(__name__)

def realizar_pedido():
    productos_disponibles = []
    
    # 1. Leer el CSV y mostrar el menú
    try:
        # Abrimos el archivo en modo lectura ('r')
        with open('datos/productos.csv', mode='r', encoding='utf-8') as archivo:
            # Usamos DictReader indicando que nuestro separador es el punto y coma
            lector = csv.DictReader(archivo, delimiter=';')
            
            print("\n--- MENÚ PIZZERÍA EL HORNO ---")
            for fila in lector:
                productos_disponibles.append(fila)
                print(f"ID: {fila['id']} | {fila['nombre']} | {fila['precio']}€")
                
    except FileNotFoundError:
        print("Error: No se encuentra el archivo productos.csv")
        logging.error("Intento de pedido fallido: No se encuentra productos.csv")
        return []

    # 2. Bucle para que el usuario seleccione productos
    ticket_pedido = []
    print("\n--- REALIZAR PEDIDO ---")
    
    while True:
        seleccion = input("Introduce el ID del producto (o '0' para terminar): ")
        
        if seleccion == '0':
            break # Salimos del bucle si el usuario escribe 0
            
        # Buscamos si el ID introducido existe en nuestros productos
        producto_encontrado = None
        for producto in productos_disponibles:
            if producto['id'] == seleccion:
                producto_encontrado = producto
                break
                
        if producto_encontrado:
            ticket_pedido.append(producto_encontrado)
            print(f" Añadido: {producto_encontrado['nombre']}")
        else:
            print(" ID no válido. Inténtalo de nuevo.")

    # Devolvemos la lista con los productos que el cliente ha elegido
    return ticket_pedido

def procesar_venta(ticket_pedido):
    if not ticket_pedido:
        print("No se seleccionaron productos.")
        return 0  # Necesario para la prueba unitaria posterior

    subtotal = 0.0
    for producto in ticket_pedido:
        # Los datos del CSV son texto, hay que pasarlos a número decimal (float)
        subtotal += float(producto['precio'])

    iva = subtotal * 0.10  # Cálculo del 10% de IVA
    total = subtotal + iva

    # Creamos la estructura del ticket a guardar
    ticket_final = {
        "productos": ticket_pedido,
        "subtotal": round(subtotal, 2),
        "iva": round(iva, 2),
        "total": round(total, 2)
    }

    # Guardamos el ticket en un archivo JSON
    with open('datos/ultimo_ticket.json', 'w', encoding='utf-8') as archivo:
        json.dump(ticket_final, archivo, indent=4)

    print("\n--- TICKET VIRTUAL ---")
    print(f"Subtotal: {subtotal:.2f}€")
    print(f"IVA (10%): {iva:.2f}€")
    print(f"TOTAL FINAL: {total:.2f}€")
    
    # Generar el log de éxito
    logger.info(f"Venta realizada con éxito. Total: {total:.2f}€")
    
    return total
    