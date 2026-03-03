#!/usr/bin/env python
"""
Punto de entrada principal de la aplicación.
Configura y ejecuta el servidor Flask.
"""

import os
import sys
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Añadir directorio actual al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app

# Crear instancia de la aplicación
app = create_app()

if __name__ == '__main__':
    # Configuración del servidor
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    host = os.environ.get('HOST', '0.0.0.0')
    
    # Mensaje de bienvenida
    print(f"""
    {'='*50}
    🎮 Juegos Gramaticales Bilingües
    {'='*50}
    🌐 Servidor: http://{host}:{port}
    🔧 Modo: {'Debug' if debug else 'Producción'}
    📚 Niveles: primaria, secundaria, adultos
    👤 Demo: demo / demo123
    📁 Directorio: {os.getcwd()}
    {'='*50}
    """)
    
    # Iniciar servidor
    app.run(host=host, port=port, debug=debug)
