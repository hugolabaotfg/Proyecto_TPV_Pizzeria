from librerias.pedidos import realizar_pedido, procesar_venta

def main():
    print("Iniciando el TPV de la Pizzería El Horno...\n")
    
    ticket = realizar_pedido()
    procesar_venta(ticket)

if __name__ == "__main__":
    main()