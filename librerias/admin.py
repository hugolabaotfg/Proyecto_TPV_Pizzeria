import os
import sys
import json
import logging
import pandas as pd

# Comprueba si productos.csv existe al iniciar el programa.
def verificar_archivos():
    if not os.path.exists('datos/productos.csv'):
        logging.error("El archivo productos.csv no existe al iniciar el programa.")
        print("Error: Falta el archivo 'datos/productos.csv'.")

def iniciar_sesion():
    try:
        # La contrasena se lee desde el archivo JSON
        with open('datos/config.json', 'r') as f:
            config = json.load(f)
            password_correcta = config['password']
    except FileNotFoundError:
        print("Error: No se encuentra el archivo 'datos/config.json'.")
        return False

    intentos = 0
    # El usuario dispone de un maximo de 3 intentos
    while intentos < 3:
        clave = input("Introduce la contrasena de administrador: ")
        if clave == password_correcta:
            # Si el acceso es correcto, se registra log INFO
            logging.info("Acceso autorizado al panel de administracion.")
            return True
        else:
            intentos += 1
            print(f"Contrasena incorrecta. Te quedan {3 - intentos} intentos.")
    
    # Tras 3 intentos fallidos, log ERROR y el programa se cierra
    logging.error("Acceso bloqueado: 3 intentos fallidos.")
    print("")
    print("Sistema bloqueado por seguridad. Cerrando programa...")
    sys.exit()

def panel_administracion():
    print("")
    print("--- PANEL DE ADMINISTRACION ---")
    try:
        # Usamos Pandas para leer el JSON que ahora es una lista de ventas
        df_ventas = pd.read_json('datos/ventas_totales.json')
        
        # Pandas suma todos los totales y saca la media de todas las ventas
        total_recaudado = df_ventas['total'].sum()
        media_ticket = df_ventas['total'].mean()
        
        # Mostrar el total y la media
        print(f"Total de dinero recaudado: {total_recaudado:.2f} euros")
        print(f"Media de gasto por ticket: {media_ticket:.2f} euros")
        
    except FileNotFoundError:
        print("Aun no hay ventas registradas para analizar.")
    except Exception as e:
        print(f"Error al leer los datos con Pandas: {e}")
