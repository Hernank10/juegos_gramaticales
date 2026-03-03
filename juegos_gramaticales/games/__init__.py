"""
Módulo de juegos gramaticales.
Exporta las clases de juegos y funciones de utilidad.
"""

from .game_base import JuegoBase
from .game1 import Juego1

# Lista completa de clases de juegos
# Se irán añadiendo más juegos progresivamente
GAME_CLASSES = [
    Juego1,
    # Juego2, Juego3, ... (se añadirán después)
]

def get_game(game_id):
    """
    Obtiene una clase de juego por su ID.
    
    Args:
        game_id (str): Identificador del juego
        
    Returns:
        class: Clase del juego o None si no se encuentra
    """
    for game_class in GAME_CLASSES:
        if game_class.id == game_id:
            return game_class
    return None

def get_all_games(nivel=None):
    """
    Obtiene todos los juegos, opcionalmente filtrados por nivel.
    
    Args:
        nivel (str, optional): Nivel para filtrar
        
    Returns:
        list: Lista de clases de juegos
    """
    if nivel:
        return [g for g in GAME_CLASSES if nivel in g.niveles]
    return GAME_CLASSES

def get_games_count():
    """Retorna el número total de juegos"""
    return len(GAME_CLASSES)
