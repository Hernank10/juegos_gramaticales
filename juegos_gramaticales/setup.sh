#!/bin/bash

# 🎮 Juegos Gramaticales Bilingües - Script de instalación
# ==================================================

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Funciones de utilidad
print_message() {
    echo -e "${BLUE}[$(date +'%H:%M:%S')]${NC} $1"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️ $1${NC}"
}

# Verificar que estamos en el directorio correcto
if [ ! -f "requirements.txt" ]; then
    print_error "No se encuentra requirements.txt"
    print_error "Ejecuta este script desde el directorio raíz del proyecto"
    exit 1
fi

print_message "🎮 Configurando Juegos Gramaticales Bilingües para Codespaces..."
print_message "=================================================="

# 1. Crear entorno virtual
print_message "📦 Creando entorno virtual..."
if [ -d "venv" ]; then
    print_warning "El entorno virtual ya existe"
else
    python -m venv venv
    print_success "Entorno virtual creado"
fi

# 2. Activar entorno virtual
print_message "🔌 Activando entorno virtual..."
source venv/bin/activate
print_success "Entorno virtual activado"

# 3. Actualizar pip
print_message "📦 Actualizando pip..."
pip install --upgrade pip > /dev/null 2>&1
print_success "pip actualizado"

# 4. Instalar dependencias
print_message "📦 Instalando dependencias (esto puede tomar unos minutos)..."
pip install -r requirements.txt > /dev/null 2>&1
if [ $? -eq 0 ]; then
    print_success "Dependencias instaladas correctamente"
else
    print_error "Error instalando dependencias"
    exit 1
fi

# 5. Verificar instalación de dependencias principales
print_message "🔍 Verificando instalación..."
python -c "
import sys
try:
    import flask
    import sqlalchemy
    import flask_login
    print('✅ Módulos principales: OK')
except ImportError as e:
    print(f'❌ Error: {e}')
    sys.exit(1)
" 2>/dev/null

if [ $? -eq 0 ]; then
    print_success "Verificación completada"
else
    print_error "Error en la verificación"
fi

# 6. Configurar variables de entorno
print_message "🔧 Configurando variables de entorno..."
if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        cp .env.example .env
        print_success "Archivo .env creado desde .env.example"
    else
        print_warning "No se encuentra .env.example"
    fi
else
    print_message "Archivo .env ya existe"
fi

# 7. Crear estructura de directorios
print_message "📁 Creando estructura de directorios..."
mkdir -p instance
mkdir -p static/images
mkdir -p static/css
mkdir -p static/js
mkdir -p logs
mkdir -p temp
print_success "Directorios creados"

# 8. Inicializar base de datos
print_message "🗄️ Inicializando base de datos..."
python -c "
from app import create_app
app = create_app()
with app.app_context():
    from app import db
    db.create_all()
    print('✅ Base de datos creada exitosamente')
" 2>/dev/null

if [ $? -eq 0 ]; then
    print_success "Base de datos inicializada"
    
    # Verificar que el archivo de BD existe
    if [ -f "instance/games.sqlite" ]; then
        print_success "Archivo de BD creado: $(ls -lh instance/games.sqlite | awk '{print $5}')"
    fi
else
    print_error "Error inicializando la base de datos"
fi

# 9. Mensaje final
echo ""
echo "=================================================="
echo -e "${GREEN}🎉 ¡Configuración completada con éxito!${NC}"
echo "=================================================="
echo ""
echo -e "${YELLOW}📝 Resumen:${NC}"
echo "   - Entorno virtual: venv/"
echo "   - Base de datos: instance/games.sqlite"
echo "   - Directorios: static/, logs/, temp/"
echo ""
echo -e "${YELLOW}🚀 Para iniciar la aplicación:${NC}"
echo "   1. Activar entorno: source venv/bin/activate"
echo "   2. Ejecutar: python run.py"
echo ""
echo -e "${YELLOW}👤 Usuario demo (creado automáticamente):${NC}"
echo "   Usuario: demo"
echo "   Contraseña: demo123"
echo ""
echo -e "${YELLOW}📋 Comandos útiles:${NC}"
echo "   - Ver logs: tail -f logs/app.log"
echo "   - Base de datos: sqlite3 instance/games.sqlite"
echo "   - Tests: pytest tests/"
echo "=================================================="

# Crear archivo de bienvenida
cat > welcome.txt << WELCOME
🎮 Juegos Gramaticales Bilingües
================================
✅ Entorno configurado: $(date)
✅ Dependencias instaladas
✅ Base de datos inicializada

Comandos rápidos:
- python run.py : Iniciar servidor
- source venv/bin/activate : Activar entorno
- deactivate : Desactivar entorno

¡Feliz aprendizaje! 📚
WELCOME

print_success "Archivo welcome.txt creado"
