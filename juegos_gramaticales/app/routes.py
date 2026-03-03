"""
Rutas de la aplicación Flask.
Define los endpoints para páginas, autenticación y API.
"""

from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify, session
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, Progreso, Logro
from app import db
from games import get_game, get_all_games, GAME_CLASSES
from datetime import datetime
import json

# Crear blueprints
main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__)
games_bp = Blueprint('games', __name__)
api_bp = Blueprint('api', __name__)

# ============================================
# RUTAS PRINCIPALES
# ============================================

@main_bp.route('/')
def index():
    """Página de inicio"""
    return render_template('index.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    """Dashboard del usuario"""
    # Progreso por niveles
    progreso_primaria = Progreso.query.filter_by(user_id=current_user.id, nivel='primaria').count()
    total_primaria = len([g for g in GAME_CLASSES if 'primaria' in g.niveles])
    
    progreso_secundaria = Progreso.query.filter_by(user_id=current_user.id, nivel='secundaria').count()
    total_secundaria = len([g for g in GAME_CLASSES if 'secundaria' in g.niveles])
    
    progreso_adultos = Progreso.query.filter_by(user_id=current_user.id, nivel='adultos').count()
    total_adultos = len([g for g in GAME_CLASSES if 'adultos' in g.niveles])
    
    # Últimos juegos
    ultimos = Progreso.query.filter_by(user_id=current_user.id)\
                .order_by(Progreso.ultimo_juego.desc())\
                .limit(5).all()
    
    return render_template('dashboard.html',
                         user=current_user,
                         progreso_primaria=progreso_primaria,
                         total_primaria=total_primaria,
                         progreso_secundaria=progreso_secundaria,
                         total_secundaria=total_secundaria,
                         progreso_adultos=progreso_adultos,
                         total_adultos=total_adultos,
                         ultimos=ultimos)

# ============================================
# RUTAS DE AUTENTICACIÓN
# ============================================

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """Registro de nuevos usuarios"""
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Validaciones
        if User.query.filter_by(username=username).first():
            flash('El nombre de usuario ya existe', 'error')
            return redirect(url_for('auth.register'))
        
        if User.query.filter_by(email=email).first():
            flash('El email ya está registrado', 'error')
            return redirect(url_for('auth.register'))
        
        # Crear usuario
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registro exitoso. Por favor inicia sesión.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Inicio de sesión"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            user.last_login = datetime.utcnow()
            db.session.commit()
            return redirect(url_for('main.dashboard'))
        
        flash('Usuario o contraseña incorrectos', 'error')
    
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    """Cerrar sesión"""
    logout_user()
    return redirect(url_for('main.index'))

# ============================================
# RUTAS DE JUEGOS
# ============================================

@games_bp.route('/')
@login_required
def juegos():
    """Lista de juegos disponibles"""
    nivel = request.args.get('nivel', current_user.nivel)
    games = get_all_games(nivel)
    
    # Obtener progreso para cada juego
    progresos = {}
    for game_class in games:
        prog = Progreso.query.filter_by(
            user_id=current_user.id,
            game_id=game_class.id,
            nivel=nivel
        ).first()
        if prog:
            progresos[game_class.id] = {
                'completado': prog.completado,
                'mejor_puntuacion': prog.mejor_puntuacion,
                'intentos': prog.intentos
            }
    
    return render_template('juegos.html', 
                         games=games, 
                         nivel=nivel,
                         progresos=progresos,
                         niveles=['primaria', 'secundaria', 'adultos'])

@games_bp.route('/<game_id>')
@login_required
def juego(game_id):
    """Página individual de un juego"""
    nivel = request.args.get('nivel', current_user.nivel)
    game_class = get_game(game_id)
    
    if not game_class:
        flash('Juego no encontrado', 'error')
        return redirect(url_for('games.juegos'))
    
    # Verificar nivel
    if nivel not in game_class.niveles:
        flash('Este nivel no está disponible para este juego', 'error')
        return redirect(url_for('games.juegos'))
    
    # Progreso anterior
    progreso = Progreso.query.filter_by(
        user_id=current_user.id,
        game_id=game_id,
        nivel=nivel
    ).first()
    
    return render_template('game.html',
                         game=game_class,
                         nivel=nivel,
                         progreso=progreso)

# ============================================
# API REST
# ============================================

@api_bp.route('/juego/<game_id>/init', methods=['POST'])
@login_required
def game_init(game_id):
    """Inicializar una partida"""
    data = request.get_json()
    nivel = data.get('nivel', current_user.nivel)
    
    game_class = get_game(game_id)
    if not game_class:
        return jsonify({'error': 'Juego no encontrado'}), 404
    
    # Crear instancia del juego
    game = game_class(current_user.id, nivel)
    game_data = game.initialize()
    
    # Guardar en sesión
    session[f'game_{game_id}'] = {
        'state': game.get_state(),
        'start_time': datetime.now().isoformat()
    }
    
    return jsonify(game_data)

@api_bp.route('/juego/<game_id>/check', methods=['POST'])
@login_required
def game_check(game_id):
    """Procesar respuesta del jugador"""
    data = request.get_json()
    
    # Recuperar estado
    game_state = session.get(f'game_{game_id}')
    if not game_state:
        return jsonify({'error': 'Partida no encontrada'}), 404
    
    # Reconstruir juego
    game_class = get_game(game_id)
    game = game_class.from_state(game_state['state'])
    
    # Procesar respuesta
    result = game.check_answer(data)
    
    # Actualizar estado
    session[f'game_{game_id}']['state'] = game.get_state()
    
    return jsonify(result)

@api_bp.route('/juego/<game_id>/save', methods=['POST'])
@login_required
def game_save(game_id):
    """Guardar progreso al finalizar"""
    data = request.get_json()
    nivel = data.get('nivel', current_user.nivel)
    puntuacion = data.get('puntuacion', 0)
    total = data.get('total', 0)
    tiempo = data.get('tiempo', 0)
    
    # Buscar o crear progreso
    progreso = Progreso.query.filter_by(
        user_id=current_user.id,
        game_id=game_id,
        nivel=nivel
    ).first()
    
    if not progreso:
        progreso = Progreso(
            user_id=current_user.id,
            game_id=game_id,
            nivel=nivel
        )
        db.session.add(progreso)
    
    # Actualizar estadísticas
    progreso.intentos += 1
    progreso.ultimo_juego = datetime.utcnow()
    progreso.tiempo_total += tiempo
    
    if puntuacion > progreso.mejor_puntuacion:
        progreso.mejor_puntuacion = puntuacion
    
    if puntuacion == total:
        progreso.completado = True
    
    # Actualizar puntos del usuario
    puntos_ganados = puntuacion * 10
    current_user.puntos_totales += puntos_ganados
    
    db.session.commit()
    
    # Limpiar sesión
    session.pop(f'game_{game_id}', None)
    
    return jsonify({
        'success': True,
        'puntos_ganados': puntos_ganados
    })

@api_bp.route('/usuario/cambiar_nivel', methods=['POST'])
@login_required
def cambiar_nivel():
    """Cambiar nivel del usuario"""
    data = request.get_json()
    nuevo_nivel = data.get('nivel')
    
    if nuevo_nivel in ['primaria', 'secundaria', 'adultos']:
        current_user.nivel = nuevo_nivel
        db.session.commit()
        return jsonify({'success': True})
    
    return jsonify({'error': 'Nivel no válido'}), 400
