# 🎮 Juegos Gramaticales Bilingües

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-2.3-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![GitHub Codespaces](https://img.shields.io/badge/GitHub-Codespaces-purple)
![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen)
![Version](https://img.shields.io/badge/Version-1.0.0-orange)

<div align="center">
  <img src="https://img.icons8.com/color/96/000000/learning--v1.png"/>
  <h3>Aprende español e inglés jugando con 30 juegos interactivos</h3>
</div>

---

## 📋 **Tabla de Contenidos**
- [Descripción](#-descripción)
- [Características](#-características)
- [Arquitectura](#-arquitectura)
- [Los 30 Juegos](#-los-30-juegos)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación en Codespaces](#-instalación-en-codespaces)
- [Instalación Local](#-instalación-local)
- [Uso de la Plataforma](#-uso-de-la-plataforma)
- [API REST](#-api-rest)
- [Sistema de Progreso](#-sistema-de-progreso)
- [Logros y Medallas](#-logros-y-medallas)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Comandos Útiles](#-comandos-útiles)
- [Solución de Problemas](#-solución-de-problemas)
- [Contribuir](#-contribuir)
- [Investigación](#-investigación)
- [Licencia](#-licencia)
- [Contacto](#-contacto)

---

## 📚 **Descripción**

**Juegos Gramaticales Bilingües** es una plataforma educativa interactiva diseñada para facilitar el aprendizaje de estructuras gramaticales en español e inglés a través de **30 juegos progresivos y adaptativos**. 

El proyecto integra principios de **gamificación**, **aprendizaje adaptativo** y **enfoque contrastivo** para ofrecer una experiencia educativa única que mantiene la motivación de los estudiantes mientras desarrollan competencias lingüísticas sólidas.

### 🎯 **Público Objetivo**
- **Estudiantes de primaria** (6-12 años) - Vocabulario básico y estructuras simples
- **Estudiantes de secundaria** (13-17 años) - Gramática intermedia y falsos amigos
- **Adultos** (18+ años) - Estructuras complejas y matices lingüísticos
- **Docentes de idiomas** - Herramienta complementaria para el aula

---

## ✨ **Características**

### 🎮 **30 Juegos Gramaticales**
- Cobertura completa de morfosintaxis español-inglés
- Mecánicas variadas (asociación, completar, clasificar, traducir)
- Dificultad progresiva y adaptativa

### 📊 **Tres Niveles de Dificultad**
- **Primaria**: Vocabulario básico, oraciones simples, imágenes de apoyo
- **Secundaria**: Estructuras complejas, falsos amigos, tiempos verbales
- **Adultos**: Subordinación, matices semánticos, corrección de errores

### 👤 **Sistema de Usuarios**
- Registro y autenticación segura
- Perfil personalizado con estadísticas
- Seguimiento de progreso individual

### 🏆 **Logros y Medallas**
- 15 logros desbloqueables
- Sistema de medallas (oro/plata/bronce)
- Rachas y bonificaciones

### 📈 **Estadísticas Detalladas**
- Progreso por niveles
- Tiempo de juego
- Patrones de error
- Mejores puntuaciones

### ⚡ **Características Técnicas**
- Interfaz responsive (móvil/tablet/escritorio)
- API RESTful para comunicación asíncrona
- Base de datos SQLite (desarrollo) / PostgreSQL (producción)
- Despliegue automático en GitHub Codespaces

---

## 🏗️ **Arquitectura**

### **Stack Tecnológico**

| Componente | Tecnología | Versión |
|------------|------------|---------|
| **Backend** | Flask | 2.3.3 |
| **Base de Datos** | SQLAlchemy + SQLite/PostgreSQL | 2.0.20 |
| **Autenticación** | Flask-Login | 0.6.2 |
| **Formularios** | Flask-WTF | 1.1.1 |
| **Frontend** | HTML5, CSS3, JavaScript | - |
| **Estilos** | CSS personalizado + Font Awesome 6 | - |
| **Entorno Desarrollo** | GitHub Codespaces | - |
| **Control Versiones** | Git + GitHub | - |
| **CI/CD** | GitHub Actions | - |

### **Diagrama de Arquitectura**

---

## 🎮 **Los 30 Juegos**

### 📘 **Nivel Primaria (Juegos 1-10)**

| # | Juego | Descripción | Competencias |
|---|-------|-------------|--------------|
| 1 | **Parejas Léxicas** | Asociar palabras inglés-español | Vocabulario básico |
| 2 | **Dominó de Pronombres** | Emparejar pronombres | Pronombres personales |
| 3 | **Árbol de Artículos** | Clasificar por género/número | Artículos |
| 4 | **Bingo de Adjetivos** | Identificar adjetivos | Adjetivos comunes |
| 5 | **Twister Gramatical** | Categorías gramaticales | Clases de palabras |
| 6 | **Puzle de Afirmación** | Construir oraciones simples | Orden sintáctico |
| 7 | **Dado Conjugado** | Conjugar verbos regulares | Presente indicativo |
| 8 | **Stop Bilingüe** | Categorías por letra | Vocabulario |
| 9 | **Carrera Negación** | Transformar a negativo | Negación |
| 10 | **¿Dónde está el sujeto?** | Identificar sujeto tácito | Sujeto y predicado |

### 📙 **Nivel Secundaria (Juegos 11-20)**

| # | Juego | Descripción | Competencias |
|---|-------|-------------|--------------|
| 11 | **Intruso Sintáctico** | Identificar palabra que no encaja | Cohesión gramatical |
| 12 | **Teléfono Escacharrado** | Traducción en cadena | Precisión traductora |
| 13 | **Dominó Colocaciones** | Emparejar verbos con preposiciones | Colocaciones |
| 14 | **Adivina Quién Es** | Descripciones de personajes | Adjetivos descriptivos |
| 15 | **Semáforo Concordancia** | Evaluar corrección gramatical | Concordancia |
| 16 | **Lego de Nexos** | Unir oraciones con conectores | Conectores |
| 17 | **Juicio de Comas** | Puntuación correcta | Ortografía |
| 18 | **Batalla Conectores** | Competencia por equipos | Conectores discursivos |
| 19 | **Relativo Perdido** | Completar con pronombres relativos | Oraciones de relativo |
| 20 | **Subordinadas Espiral** | Construcción colaborativa | Subordinación |

### 📕 **Nivel Adultos (Juegos 21-30)**

| # | Juego | Descripción | Competencias |
|---|-------|-------------|--------------|
| 21 | **Causa y Efecto** | Relaciones lógicas | Conectores causales |
| 22 | **Condicionales Cadena** | Oraciones condicionales | Modo condicional |
| 23 | **Reported Speech** | Estilo indirecto | Discurso referido |
| 24 | **Oca Gramatical** | Juego de mesa gramatical | Repaso general |
| 25 | **Story Cubes** | Crear historias | Creatividad narrativa |
| 26 | **Dictado Cruzado** | Transcripción y traducción | Comprensión auditiva |
| 27 | **Corrección Cooperativa** | Editar textos con errores | Corrección de estilo |
| 28 | **Pictionary Sintáctico** | Dibujar estructuras | Comprensión lectora |
| 29 | **Improvisación Opuestos** | Transformar con conectores opuestos | Matices semánticos |
| 30 | **Traductor Infiel** | Corregir traducciones automáticas | Competencia traductora |

---

## ⚙️ **Requisitos Previos**

- Python 3.11 o superior
- pip (gestor de paquetes de Python)
- Git
- Navegador web moderno (Chrome, Firefox, Edge)
- (Opcional) GitHub account para Codespaces

---

## 🚀 **Instalación en Codespaces**

### **Método 1: Un Click (Recomendado)**

[![Open in Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Hernank10/juegos-gramaticales)

### **Método 2: Manual**

1. **Ir al repositorio en GitHub**
2. **Hacer clic en "Code" → "Codespaces" → "Create codespace on main"**
3. **Esperar a que el entorno se configure automáticamente** (2-3 minutos)
4. **Ejecutar la aplicación:**
   ```bash
   python run.py
git clone https://github.com/Hernank10/juegos-gramaticales.git
cd juegos-gramaticales
chmod +x setup.sh
./setup.sh

Paso 3: Activar entorno virtual
bash
source venv/bin/activate  # En Windows: venv\Scripts\activate
Paso 4: Iniciar la aplicación
bash
python run.py
Paso 5: Abrir en el navegador
text
http://localhost:5000
🎯 Uso de la Plataforma
Acceso
Usuario	Contraseña	Rol
demo	demo123	Usuario de prueba
[Registro propio]	[elegida]	Nuevo usuario
Flujo de Usuario
text
┌─────────────┐
│   Inicio    │
└──────┬──────┘
       ↓
┌─────────────┐
│ Registro/   │
│   Login     │
└──────┬──────┘
       ↓
┌─────────────┐
│  Dashboard  │ ← Visualiza progreso, rachas, puntos
└──────┬──────┘
       ↓
┌─────────────┐
│ Selección   │ ← Elige nivel (primaria/secundaria/adultos)
│ de Juegos   │
└──────┬──────┘
       ↓
┌─────────────┐
│    Juego    │ ← Responde preguntas, recibe feedback
└──────┬──────┘
       ↓
┌─────────────┐
│  Resultados │ ← Puntuación, logros, opción de repetir
└─────────────┘
Navegación Principal
Sección	Descripción
Dashboard	Resumen de progreso, estadísticas, últimos juegos
Juegos	Lista de juegos por nivel con filtros
Estadísticas	Gráficos detallados de rendimiento
Perfil	Configuración de usuario y preferencias
🔌 API REST
Endpoints Disponibles
Método	Endpoint	Descripción	Autenticación
POST	/api/juego/<id>/init	Inicializar partida	Requerida
POST	/api/juego/<id>/check	Verificar respuesta	Requerida
POST	/api/juego/<id>/save	Guardar progreso	Requerida
POST	/api/usuario/cambiar_nivel	Cambiar nivel	Requerida
Ejemplo de Uso (JavaScript)
javascript
// Inicializar juego
fetch('/api/juego/parejas_lexicas/init', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ nivel: 'primaria' })
})
.then(response => response.json())
.then(data => console.log(data));

// Verificar respuesta
fetch('/api/juego/parejas_lexicas/check', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ respuesta: 'perro' })
})
.then(response => response.json())
.then(data => console.log(data));
📊 Sistema de Progreso
Puntuación
Acción	Puntos
Respuesta correcta	+10
Racha (por respuesta consecutiva)	+2 adicional
Juego completado (bonus)	+50
Logro desbloqueado	+100
Niveles de Dificultad
Nivel	Requisito para desbloquear
Primaria	Disponible desde el inicio
Secundaria	Completar 5 juegos de primaria
Adultos	Completar 10 juegos de secundaria
🏆 Logros y Medallas
Logros Disponibles
Logro	Condición	Icono	Puntos
Primer paso	Completar primer juego	🎮	50
En racha	5 aciertos consecutivos	🔥	100
Perfecto	Puntuación máxima en un juego	🏆	200
Explorador	Jugar 10 juegos diferentes	🗺️	150
Velocista	Juego completado en tiempo récord	⚡	100
Políglota	Completar nivel adultos	🌟	300
Maestro	1000 puntos totales	👑	500
Medallas por Rendimiento
Porcentaje	Medalla	Color
≥ 90%	Oro	🟡
70-89%	Plata	⚪
50-69%	Bronce	🟤
📁 Estructura del Proyecto
text
juegos_gramaticales/
├── 📂 .devcontainer/          # Configuración de Codespaces
│   ├── devcontainer.json
│   └── Dockerfile
├── 📂 .github/                 # GitHub Actions
│   └── workflows/
│       └── deploy.yml
├── 📂 app/                     # Lógica de la aplicación
│   ├── __init__.py            # Factory pattern
│   ├── models.py              # Modelos de base de datos
│   └── routes.py              # Endpoints y rutas
├── 📂 games/                   # Módulos de juegos
│   ├── __init__.py            # Exportador de juegos
│   ├── game_base.py           # Clase base abstracta
│   ├── game1.py               # Parejas léxicas
│   ├── game2.py               # Dominó de pronombres
│   └── ... (hasta 30)
├── 📂 static/                  # Archivos estáticos
│   └── css/
│       └── style.css          # Estilos principales
├── 📂 templates/               # Plantillas HTML
│   ├── base.html              # Plantilla base
│   ├── index.html             # Página de inicio
│   ├── login.html             # Inicio de sesión
│   ├── register.html          # Registro
│   ├── dashboard.html         # Panel de usuario
│   ├── juegos.html            # Lista de juegos
│   └── game.html              # Área de juego
├── 📂 instance/                # Base de datos SQLite
│   └── games.sqlite
├── 📂 logs/                    # Archivos de log
├── 📂 tests/                   # Pruebas unitarias
├── 📄 .env.example              # Variables de entorno ejemplo
├── 📄 .gitignore                # Archivos ignorados por git
├── 📄 README.md                 # Este archivo
├── 📄 requirements.txt          # Dependencias Python
├── 📄 run.py                    # Punto de entrada
└── 📄 setup.sh                   # Script de instalación
🛠️ Comandos Útiles
Gestión del Entorno
bash
# Activar entorno virtual
source venv/bin/activate

# Desactivar entorno
deactivate

# Instalar dependencias
pip install -r requirements.txt

# Guardar dependencias actualizadas
pip freeze > requirements.txt
Base de Datos
bash
# Inicializar base de datos
python -c "from app import create_app; app = create_app()"

# Entrar a consola SQLite
sqlite3 instance/games.sqlite

# Ver tablas
.tables

# Ver usuarios
SELECT * FROM users;

# Ver progreso
SELECT * FROM progresos;
Desarrollo
bash
# Iniciar servidor en modo debug
python run.py

# Limpiar archivos caché
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type f -name "*.pyc" -delete

# Ejecutar pruebas
pytest tests/

# Ver cobertura
pytest --cov=app tests/
Git y GitHub
bash
# Ver estado
git status

# Añadir cambios
git add .

# Commit
git commit -m "Mensaje descriptivo"

# Subir cambios
git push origin main

# Ver logs
git log --oneline
Codespaces
bash
# Ver codespaces activos
gh codespace list

# Detener codespace
gh codespace stop

# Reconstruir codespace
gh codespace rebuild
🔧 Solución de Problemas
Error: Puerto 5000 en uso
bash
# Ver procesos en el puerto
lsof -i :5000

# Matar proceso
kill -9 <PID>
# O
fuser -k 5000/tcp
Error: Base de datos no encontrada
bash
# Recrear base de datos
rm -f instance/games.sqlite
python -c "from app import create_app; app = create_app()"
Error: Módulos no encontrados
bash
# Reinstalar dependencias
pip install -r requirements.txt
Error: Permisos denegados
bash
# Dar permisos de ejecución
chmod +x setup.sh
chmod +x run.py
Error: Usuario demo no existe
bash
# Crear usuario demo manualmente
python -c "
from app import create_app
from app.models import User, db
from werkzeug.security import generate_password_hash
app = create_app()
with app.app_context():
    if not User.query.filter_by(username='demo').first():
        demo = User(username='demo', email='demo@example.com', 
                   password_hash=generate_password_hash('demo123'))
        db.session.add(demo)
        db.session.commit()
        print('✅ Usuario demo creado')
"
🤝 Contribuir
¿Cómo contribuir?
Fork el repositorio

Crear una rama (git checkout -b feature/AmazingFeature)

Commit cambios (git commit -m 'Add AmazingFeature')

Push a la rama (git push origin feature/AmazingFeature)

Abrir un Pull Request

Guía de Estilo
Python: seguir PEP 8

HTML: indentación con 4 espacios

CSS: clases con nomenclatura BEM

Commits: mensajes descriptivos en español

Reportar Issues
Usa la sección Issues para:

Reportar bugs

Sugerir nuevas características

Solicitar aclaraciones

📖 Investigación
Este proyecto cuenta con un proyecto de investigación asociado:

Título: "Efectividad de los Juegos Gramaticales Bilingües en el Desarrollo de Competencias Morfosintácticas en Estudiantes de Español e Inglés: Un Estudio Cuasi-Experimental"

Publicaciones
[Artículo 1] Diseño y desarrollo de juegos gramaticales (en preparación)

[Artículo 2] Efectividad de la gamificación en gramática (en preparación)

[Artículo 3] Patrones de error y aprendizaje adaptativo (en preparación)

Cita Sugerida
text
[Apellido], [Inicial]. (2024). Juegos Gramaticales Bilingües: 
Una plataforma educativa para el aprendizaje de español e inglés. 
GitHub. https://github.com/Hernank10/juegos-gramaticales
📄 Licencia
Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

text
MIT License

Copyright (c) 2026 [Tu Nombre]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
📞 Contacto https://github.com/Hernank10/juegos-gramaticale
Autor Hernank10
Nombre: [hernank10]

Email: [tu.email@ejemplo.com]

GitHub:https://github.com/Hernank10/juegos-gramaticales

LinkedIn: Tu Perfil
https://github.com/Hernank10/juegos-gramaticales
Redes Sociales
Twitter: @tu-usuario

Website: tusitio.com

Cita
"Aprender gramática nunca fue tan divertido"

🙏 Agradecimientos
A la comunidad de Flask por su excelente documentación

A Font Awesome por los iconos

A Google Fonts por las tipografías

A los beta testers que ayudaron a mejorar la plataforma

A los educadores que compartieron su experiencia

📊 Estadísticas del Proyecto
Métrica	Valor
⏱️ Horas de desarrollo	200+
📝 Líneas de código	5,000+
🎮 Juegos implementados	30
📚 Niveles	3
🏆 Logros	15
👥 Usuarios potenciales	Ilimitado
🌍 Idiomas	Español, Inglés
🎉 ¡Comienza a Jugar!
bash
# Un comando y estarás listo
git clone https://github.com/tu-usuario/juegos-gramaticales.git
cd juegos-gramaticales
./setup.sh
python run.py
Usuario demo: demo / demo123

<div align="center"> <img src="https://img.icons8.com/color/96/000000/learning.png"/> <h3>¡Aprender gramática nunca fue tan divertido!</h3> <p>Hecho con ❤️ para educadores y estudiantes</p> <p> <a href="https://github.com/tu-usuario/juegos-gramaticales">GitHub</a> • <a href="https://github.com/tu-usuario/juegos-gramaticales/issues">Issues</a> • <a href="https://github.com/tu-usuario/juegos-gramaticales/wiki">Wiki</a> </p> <br> <p>⭐ ¡No olvides dar una estrella si te es útil! ⭐</p> </div> ```
Paso 3: Guardar y salir de nano
bash
# Para guardar y salir:
Ctrl + O  (luego Enter para confirmar)
Ctrl + X  (para salir)
Paso 4: Verificar que se guardó correctamente
bash
# Ver las primeras líneas
head -5 README.md

# Ver tamaño del archivo
ls -lh README.md

# Ver contenido completo (paginado)
less README.md
Paso 5: Subir a GitHub
bash
# Ver estado
git status

# Añadir README.md
git add README.md

# Hacer commit
git commit -m "Agrega README.md completo con documentación de 30 juegos"

# Subir a GitHub
git push origin main
📋 ATAJOS DE NANO ÚTILES
Comando	Función
Ctrl + O	Guardar archivo
Ctrl + X	Salir de nano
Ctrl + K	Cortar línea actual
Ctrl + U	Pegar línea
Ctrl + W	Buscar texto
Ctrl + \	Buscar y reemplazar
Ctrl + G	Ver ayuda
Ctrl + C	Mostrar posición actual



