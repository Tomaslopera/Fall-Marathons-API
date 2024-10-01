#!/bin/bash

# Endpoint base
BASE_URL="http://127.0.0.1:8000"

# Prueba 1: Agregar una maratón con datos válidos
echo "Prueba 1: Agregar una maratón con datos válidos"
RESPONSE=$(curl -s -X POST "$BASE_URL/add_marathon" \
    -H "Content-Type: application/json" \
    -d '{
        "Race": "Test Marathon",
        "Year": 2024,
        "Name": "John Doe",
        "Gender": "M",
        "Age": 30,
        "Finish": "2:30:45",
        "Age_Bracket": "30-34"
    }')

echo "Respuesta: $RESPONSE"

# Prueba 2: Agregar una maratón con datos incompletos (debe fallar)
echo "Prueba 2: Agregar una maratón con datos incompletos"
RESPONSE=$(curl -s -X POST "$BASE_URL/add_marathon" \
    -H "Content-Type: application/json" \
    -d '{
        "Race": "",
        "Year": 2024,
        "Name": "Jane Doe",
        "Gender": "F",
        "Age": 25,
        "Finish": "3:15:00",
        "Age_Bracket": "25-29"
    }')

echo "Respuesta: $RESPONSE"

# Prueba 3: Obtener maratones con paginación y datos válidos
echo "Prueba 3: Obtener maratones con datos válidos"
RESPONSE=$(curl -s -X GET "$BASE_URL/marathons/Test Marathon?offset=0&limit=5")

echo "Respuesta: $RESPONSE"

# Prueba 4: Obtener maratones con un límite superior a 100 (debe fallar)
echo "Prueba 4: Obtener maratones con un límite superior a 100"
RESPONSE=$(curl -s -X GET "$BASE_URL/marathons/Test Marathon?offset=0&limit=101")

echo "Respuesta: $RESPONSE"
