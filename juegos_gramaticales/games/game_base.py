"""
Clase base para todos los juegos gramaticales.
Define la interfaz común y funcionalidad compartida.
"""

import random
from datetime import datetime

class JuegoBase:
    """
    Clase base abstracta para juegos gramaticales.
    Todas las clases de juego deben heredar de esta.
    """
    
    # Atributos de clase (sobrescribir en cada juego)
    id = "base"
    nombre = "Juego Base"
    descripcion = "Descripción del juego base"
    instrucciones = "Instrucciones básicas"
    niveles = ["primaria", "secundaria", "adultos"]
    tiempo_limite = None  # None = sin límite, o segundos
    
    def __init__(self, user_id, nivel):
        """
        Inicializa una instancia del juego.
        
        Args:
            user_id (int): ID del usuario
            nivel (str): Nivel de dificultad
        """
        self.user_id = user_id
        self.nivel = nivel
        self.puntuacion = 0
        self.indice = 0
        self.completado = False
        self.estado = {}
        self.inicializar_juego()
    
    def inicializar_juego(self):
        """
        Inicializa el estado del juego.
        Debe ser sobreescrito por las subclases.
        """
        pass
    
    def get_state(self):
        """
        Retorna el estado actual para guardar en sesión.
        
        Returns:
            dict: Estado del juego
        """
        return {
            'user_id': self.user_id,
            'nivel': self.nivel,
            'puntuacion': self.puntuacion,
            'indice': self.indice,
            'completado': self.completado,
            'estado': self.estado
        }
    
    @classmethod
    def from_state(cls, state):
        """
        Crea una instancia desde un estado guardado.
        
        Args:
            state (dict): Estado previo del juego
            
        Returns:
            JuegoBase: Instancia del juego reconstruida
        """
        game = cls(state['user_id'], state['nivel'])
        game.puntuacion = state['puntuacion']
        game.indice = state['indice']
        game.completado = state['completado']
        game.estado = state['estado']
        return game
    
    def initialize(self):
        """
        Prepara datos para el frontend al iniciar el juego.
        
        Returns:
            dict: Datos iniciales del juego
        """
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'instrucciones': self.instrucciones,
            'nivel': self.nivel,
            'tiempo_limite': self.tiempo_limite,
            'pregunta_actual': self.get_pregunta_actual(),
            'progreso': {
                'actual': self.indice,
                'total': self.total_preguntas
            }
        }
    
    def get_pregunta_actual(self):
        """
        Retorna la pregunta actual.
        Debe ser sobreescrito por las subclases.
        
        Returns:
            dict: Pregunta actual o None si terminó
        """
        return {}
    
    def check_answer(self, data):
        """
        Verifica la respuesta del usuario.
        
        Args:
            data (dict): Datos de la respuesta
            
        Returns:
            dict: Resultado de la verificación
        """
        correcto = self.verificar_respuesta(data)
        
        if correcto:
            self.puntuacion += 1
            self.estado['ultimo_acierto'] = True
        else:
            self.estado['ultimo_acierto'] = False
        
        self.indice += 1
        self.estado['ultima_respuesta'] = data
        
        if self.indice >= self.total_preguntas:
            self.completado = True
        
        return {
            'correcto': correcto,
            'puntuacion': self.puntuacion,
            'completado': self.completado,
            'siguiente_pregunta': self.get_pregunta_actual() if not self.completado else None,
            'mensaje': self.get_mensaje_resultado(correcto),
            'feedback': self.get_feedback(correcto, data)
        }
    
    def verificar_respuesta(self, data):
        """
        Lógica específica de verificación.
        Debe ser sobreescrito por las subclases.
        
        Args:
            data (dict): Datos de la respuesta
            
        Returns:
            bool: True si la respuesta es correcta
        """
        return False
    
    def get_mensaje_resultado(self, correcto):
        """
        Retorna mensaje según el resultado.
        
        Args:
            correcto (bool): Si la respuesta fue correcta
            
        Returns:
            str: Mensaje motivador
        """
        if correcto:
            return random.choice([
                "¡Excelente!", "¡Muy bien!", "¡Correcto!", 
                "¡Perfecto!", "¡Así se hace!", "¡Magnífico!"
            ])
        else:
            return random.choice([
                "Casi", "Sigue intentando", "No es correcto",
                "¡Ánimo!", "Inténtalo de nuevo", "Por poco"
            ])
    
    def get_feedback(self, correcto, data):
        """
        Retorna feedback específico sobre la respuesta.
        Opcional, puede ser sobreescrito.
        
        Args:
            correcto (bool): Si la respuesta fue correcta
            data (dict): Datos de la respuesta
            
        Returns:
            str: Feedback o None
        """
        return None
    
    @property
    def total_preguntas(self):
        """
        Número total de preguntas.
        Debe ser sobreescrito por las subclases.
        
        Returns:
            int: Total de preguntas
        """
        return 0
