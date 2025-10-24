# Imagen base oficial de Python
FROM python:3.10-slim

# Establecer carpeta de trabajo
WORKDIR /app

# Copiar archivos
COPY . .

# Instalar dependencias
RUN pip install -r requirements.txt

# Ejecutar pruebas
CMD ["pytest", "test_app.py"]