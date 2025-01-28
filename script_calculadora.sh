#!/bin/bash

# Verifica se o Python está instalado

echo "Vericando instalação do Python..."

if ! command -v python3 &>/dev/null; then
    echo "Python3 não está instalado no sistema."
    echo "Instalando Python3..."
    sudo apt update
    sudo apt install -y python3
    echo "Python3 instalado com sucesso!"
else
    echo "Python3 já está instalado."
fi

# Executa a calculadora
echo "Iniciando a calculadora..."
echo "============== CALCULADORA =============="
python3 calculadora_python.py
