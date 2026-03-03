"""
Juego 1: Parejas Léxicas
Aprende falsos amigos y cognados entre inglés y español
"""

from .game_base import JuegoBase
import random

class Juego1(JuegoBase):
    """
    Juego de parejas léxicas.
    El usuario debe relacionar palabras en inglés con su significado en español.
    """
    
    id = "parejas_lexicas"
    nombre = "Parejas Léxicas"
    descripcion = "Aprende falsos amigos y cognados entre inglés y español"
    instrucciones = "Se te mostrará una palabra en inglés. Escribe su significado correcto en español."
    tiempo_limite = 30  # segundos
    
    def inicializar_juego(self):
        """
        Configura las palabras según el nivel seleccionado.
        """
        if self.nivel == "primaria":
            self.pares = [
                {"en": "dog", "es": "perro", "imagen": "perro"},
                {"en": "cat", "es": "gato", "imagen": "gato"},
                {"en": "house", "es": "casa", "imagen": "casa"},
                {"en": "tree", "es": "árbol", "imagen": "arbol"},
                {"en": "apple", "es": "manzana", "imagen": "manzana"},
                {"en": "car", "es": "coche", "imagen": "coche"},
                {"en": "book", "es": "libro", "imagen": "libro"},
                {"en": "sun", "es": "sol", "imagen": "sol"},
                {"en": "moon", "es": "luna", "imagen": "luna"},
                {"en": "star", "es": "estrella", "imagen": "estrella"}
            ]
        elif self.nivel == "secundaria":
            self.pares = [
                {"en": "embarrassed", "es": "avergonzado"},
                {"en": "constipated", "es": "estreñido"},
                {"en": "sensible", "es": "sensato"},
                {"en": "actual", "es": "real"},
                {"en": "carpet", "es": "alfombra"},
                {"en": "library", "es": "biblioteca"},
                {"en": "exit", "es": "salida"},
                {"en": "success", "es": "éxito"},
                {"en": "eventually", "es": "finalmente"},
                {"en": "sensitive", "es": "sensible"}
            ]
        else:  # adultos
            self.pares = [
                {"en": "eventually", "es": "finalmente"},
                {"en": "sensible", "es": "sensible"},
                {"en": "library", "es": "biblioteca"},
                {"en": "success", "es": "éxito"},
                {"en": "exit", "es": "salida"},
                {"en": "constipated", "es": "estreñido"},
                {"en": "embarrassed", "es": "avergonzado"},
                {"en": "actual", "es": "real"},
                {"en": "carpet", "es": "alfombra"},
                {"en": "sensitive", "es": "sensible"}
            ]
        
        # Mezclar para que sea aleatorio
        random.shuffle(self.pares)
        self.total_preguntas = len(self.pares)
        self.indice = 0
        self.estado['respuestas'] = []
        self.estado['aciertos'] = 0
    
    def get_pregunta_actual(self):
        """
        Retorna la pregunta actual.
        
        Returns:
            dict: Datos de la pregunta o None si terminó
        """
        if self.indice < self.total_preguntas:
            par = self.pares[self.indice]
            return {
                'tipo': 'texto_imagen',
                'palabra': par['en'],
                'imagen': par.get('imagen'),
                'opciones': self.generar_opciones(par['es']) if self.nivel != "primaria" else None,
                'numero': self.indice + 1,
                'total': self.total_preguntas
            }
        return None
    
    def generar_opciones(self, correcta):
        """
        Genera opciones múltiples para niveles superiores.
        
        Args:
            correcta (str): Respuesta correcta
            
        Returns:
            list: Lista de 4 opciones mezcladas
        """
        # Todas las respuestas posibles
        todas_es = [p['es'] for p in self.pares]
        opciones = [correcta]
        
        # Añadir opciones distintas
        while len(opciones) < 4:
            opcion = random.choice(todas_es)
            if opcion not in opciones:
                opciones.append(opcion)
        
        random.shuffle(opciones)
        return opciones
    
    def verificar_respuesta(self, data):
        """
        Verifica si la respuesta es correcta.
        
        Args:
            data (dict): Debe contener 'respuesta'
            
        Returns:
            bool: True si es correcta
        """
        respuesta = data.get('respuesta', '').strip().lower()
        correcta = self.pares[self.indice]['es'].lower()
        
        # Registrar respuesta
        acierto = (respuesta == correcta)
        self.estado['respuestas'].append({
            'pregunta': self.pares[self.indice]['en'],
            'respuesta': respuesta,
            'correcta': correcta,
            'acierto': acierto
        })
        
        if acierto:
            self.estado['aciertos'] += 1
        
        return acierto
    
    def get_feedback(self, correcto, data):
        """
        Proporciona feedback específico.
        
        Args:
            correcto (bool): Si fue correcto
            data (dict): Datos de la respuesta
            
        Returns:
            str: Feedback
        """
        if not correcto:
            return f"La respuesta correcta era: {self.pares[self.indice]['es']}"
        return None
    
    @property
    def total_preguntas(self):
        return len(self.pares)
    
    def get_resumen(self):
        """
        Retorna un resumen del juego.
        
        Returns:
            dict: Estadísticas del juego
        """
        return {
            'total': self.total_preguntas,
            'aciertos': self.estado.get('aciertos', 0),
            'fallos': self.total_preguntas - self.estado.get('aciertos', 0),
            'porcentaje': (self.estado.get('aciertos', 0) / self.total_preguntas) * 100 if self.total_preguntas > 0 else 0
        }
