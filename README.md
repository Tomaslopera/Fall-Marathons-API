# Fall Marathons API (2010-2019)

## Autores

- Pedro Sierra
- Tomás Lopera

Este proyecto consiste en una API desarrollada con FastAPI para gestionar y consultar datos de maratones entre los años 2010 y 2019. Los datos incluyen información sobre el nombre del participante, su tiempo de finalización, categoría de edad, entre otros. La API está desplegada dentro de un contenedor Docker y es accesible públicamente utilizando ngrok para generar una URL temporal.

## Características

- **Consultar maratones**: Obtener resultados de maratones filtrados por carrera y paginación.
- **Agregar resultados**: Añadir nuevos resultados de maratones a la base de datos.
- **Desplegable en Docker**: Corre fácilmente dentro de un contenedor Docker.
- **Acceso público con ngrok**: La API puede ser accesible desde cualquier lugar usando ngrok.

## Requisitos

- Docker
- Python 3.12 o superior
- FastAPI
- SQLAlchemy
- MySQL o cualquier base de datos compatible con SQLAlchemy
- Ngrok (para exponer la API públicamente)

## Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/tuusuario/fall-marathons-api.git
   cd fall-marathons-api

2. **Instalar dependencias:**

   ```bash
   pip install -r requirements.txt

3. **Configurar la base de datos**

4. **Levantar el contenedor de docker:**

   ```bash
   docker-compose up --build

5. **Publicar la API usando NGROK:**

   ```bash
   ngrok http 8000

**LINK A LA API:**

   ```bash
     [ngrok http 8000](https://9b19-190-28-11-78.ngrok-free.app/docs)

