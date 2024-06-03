# Selecciona la imagen base de Python
FROM python:3.10-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /code

# Instala las dependencias del sistema
RUN apt-get update && apt-get install -y gcc libpq-dev

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt /code/

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos del proyecto al contenedor
COPY . /code/

# Expone el puerto en el que correrá la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
