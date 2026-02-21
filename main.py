import logging
from librerias.pedidos import realizar_pedido, procesar_venta
from librerias.admin import verificar_archivos, iniciar_sesion, panel_administracion

# Configuracion general del log
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[
        logging.FileHandler("logs/ventas.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)

# 1. Comprobacion inicial de errores 
verificar_archivos()

# 2. Menu principal ejecutandose directamente
opcion=7
while opcion!=0:
    print("============================")
    print("PIZZERIA EL HORNO")
    print("============================")
    print("1. Realizar Pedido ")
    print("2. Panel de Administracion")
    print("3. Salir del programa")
    print("")
    opcion = int(input("Selecciona una opcion: "))
    print("")
    
    match opcion:
            case 1:
                ticket = realizar_pedido()
                if ticket: 
                    procesar_venta(ticket)
                print("")
                    
            case 2:
                if iniciar_sesion():
                    panel_administracion()
                print("")
    
            case 3:
                opcion=0
                print("Gracias por usar el TPV de El Horno.")
                print("Saliendo...")
                
            case _:
                print("Opcion no valida. Intentalo de nuevo.")
                print("")
