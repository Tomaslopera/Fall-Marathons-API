import requests

BASE_URL = "http://localhost:8000"

# Prueba 1: Agregar una maratón con datos válidos
print("Prueba 1: Agregar una maratón con datos válidos")
response = requests.post(f"{BASE_URL}/add_marathon", json={
    "Race": "Test Marathon",
    "Year": 2024,
    "Name": "John Doe",
    "Gender": "M",
    "Age": 30,
    "Finish": 13657,
    "Age_Bracket": "30-34"
})
print("Respuesta:", response.json())

# Prueba 2: Agregar una maratón con datos erroneos (debe fallar)
print("Prueba 2: Agregar una maratón con datos incompletos")
response = requests.post(f"{BASE_URL}/add_marathon", json={
    "Race": "",
    "Year": 2024,
    "Name": "Jane Doe",
    "Gender": "F",
    "Age": 25,
    "Finish": "03:27:33",
    "Age_Bracket": "25-29"
})
print("Respuesta:", response.json())

# Prueba 3: Obtener maratones con paginación y datos válidos
print("Prueba 3: Obtener maratones con datos válidos")
response = requests.get(f"{BASE_URL}/marathons/Test Marathon", params={"offset": 0, "limit": 5})
print("Respuesta:", response.json())

# Prueba 4: Obtener maratones con un límite superior a 100 (debe fallar)
print("Prueba 4: Obtener maratones con un límite superior a 100")
response = requests.get(f"{BASE_URL}/marathons/Test Marathon", params={"offset": 0, "limit": 101})
print("Respuesta:", response.json())
