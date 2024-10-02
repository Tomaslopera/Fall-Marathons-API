# Usar una imagen base de Python
FROM python:3.12-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos requeridos
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de tu aplicación
COPY . .

# Exponer el puerto que utiliza tu API
EXPOSE 8000

# Comando para ejecutar tu aplicación
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
