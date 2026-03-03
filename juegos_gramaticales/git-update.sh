#!/bin/bash

echo "🚀 ACTUALIZANDO REPOSITORIO EN GITHUB"
echo "======================================"

# Colores
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Mostrar estado actual
echo -e "${YELLOW}📋 Estado actual:${NC}"
git status
echo ""

# Preguntar mensaje de commit
echo -e "${YELLOW}📝 Mensaje del commit:${NC}"
read commit_message

if [ -z "$commit_message" ]; then
    commit_message="Actualización: $(date +'%Y-%m-%d %H:%M:%S')"
fi

# Añadir archivos
echo -e "${YELLOW}📦 Añadiendo archivos...${NC}"
git add .

# Hacer commit
echo -e "${YELLOW}💾 Haciendo commit...${NC}"
git commit -m "$commit_message"

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Commit exitoso${NC}"
    
    # Subir a GitHub
    echo -e "${YELLOW}📤 Subiendo a GitHub...${NC}"
    git push origin main
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ Subida exitosa a GitHub${NC}"
    else
        echo -e "${RED}❌ Error al subir${NC}"
    fi
else
    echo -e "${YELLOW}⚠️ No hay cambios para commit${NC}"
fi

echo ""
echo "======================================"
git log --oneline -1
git status
