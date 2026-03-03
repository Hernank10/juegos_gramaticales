"""
Modelos de base de datos para la aplicación.
Define las estructuras de usuarios, progreso y logros.
"""

from app import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    """Modelo de usuario"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    nivel = db.Column(db.String(20), default='primaria')
    puntos_totales = db.Column(db.Integer, default=0)
    racha_actual = db.Column(db.Integer, default=0)
    racha_maxima = db.Column(db.Integer, default=0)
    avatar = db.Column(db.String(200), default='default.png')
    
    # Relaciones
    progresos = db.relationship('Progreso', backref='user', lazy=True, cascade='all, delete-orphan')
    logros = db.relationship('Logro', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def set_password(self, password):
        """Establece la contraseña hasheada"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Verifica la contraseña"""
        return check_password_hash(self.password_hash, password)
    
    def update_racha(self, acierto):
        """Actualiza la racha del usuario"""
        if acierto:
            self.racha_actual += 1
            if self.racha_actual > self.racha_maxima:
                self.racha_maxima = self.racha_actual
        else:
            self.racha_actual = 0
        db.session.commit()
    
    def __repr__(self):
        return f'<User {self.username}>'

class Progreso(db.Model):
    """Progreso del usuario en cada juego"""
    __tablename__ = 'progresos'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    game_id = db.Column(db.String(50), nullable=False)
    nivel = db.Column(db.String(20), nullable=False)
    puntuacion = db.Column(db.Integer, default=0)
    total_preguntas = db.Column(db.Integer, default=0)
    completado = db.Column(db.Boolean, default=False)
    mejor_puntuacion = db.Column(db.Integer, default=0)
    intentos = db.Column(db.Integer, default=0)
    ultimo_juego = db.Column(db.DateTime, default=datetime.utcnow)
    tiempo_total = db.Column(db.Integer, default=0)  # en segundos
    
    __table_args__ = (
        db.UniqueConstraint('user_id', 'game_id', 'nivel', name='unique_user_game_nivel'),
    )
    
    @property
    def porcentaje(self):
        """Calcula el porcentaje de progreso"""
        if self.total_preguntas > 0:
            return int((self.mejor_puntuacion / self.total_preguntas) * 100)
        return 0
    
    def __repr__(self):
        return f'<Progreso {self.game_id} - {self.user_id}>'

class Logro(db.Model):
    """Logros desbloqueados por el usuario"""
    __tablename__ = 'logros'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    logro_id = db.Column(db.String(50), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200))
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    icono = db.Column(db.String(50))
    
    __table_args__ = (
        db.UniqueConstraint('user_id', 'logro_id', name='unique_user_logro'),
    )
    
    def __repr__(self):
        return f'<Logro {self.nombre} - {self.user_id}>'
