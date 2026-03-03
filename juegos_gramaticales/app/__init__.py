"""
Módulo principal de la aplicación Flask.
Configura la aplicación y sus extensiones.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Inicializar extensiones
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

def create_app():
    """Factory para crear la aplicación Flask"""
    
    # Crear aplicación
    app = Flask(__name__, 
                static_folder='../static',
                template_folder='../templates')
    
    # Configuración básica
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URL', 
        'sqlite:///' + os.path.join(app.instance_path, 'games.sqlite')
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['WTF_CSRF_ENABLED'] = os.environ.get('WTF_CSRF_ENABLED', 'True').lower() == 'true'
    
    # Asegurar que existe el directorio instance
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Inicializar extensiones con la app
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    
    # Configuración de login
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Por favor inicia sesión para acceder'
    login_manager.login_message_category = 'info'
    
    # Importar y registrar blueprints
    from app.routes import main_bp, auth_bp, games_bp, api_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(games_bp, url_prefix='/juegos')
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Crear tablas y usuario demo
    with app.app_context():
        db.create_all()
        
        from app.models import User
        from werkzeug.security import generate_password_hash
        
        # Crear usuario demo si no existe
        if not User.query.filter_by(username='demo').first():
            demo = User(
                username='demo',
                email='demo@example.com',
                password_hash=generate_password_hash('demo123'),
                nivel='primaria',
                puntos_totales=0
            )
            db.session.add(demo)
            db.session.commit()
            print("✅ Usuario demo creado: demo/demo123")
    
    return app
