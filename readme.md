# Requerimientos
Ubuntu 16 o superior

Python 3.6.3

# Instalar librerías
python3.6 -m pip -r install requirements.txt

# Iniciar el proyecto

# Ingresar a la carpeta virtual
source .venv/bin/activate

# Salir
deactivate

# Activar el .venv ejecutar
pip install flask

pip freeze > requirements.txt

# Instalar librerías

# Test
http://localhost:5000/estudiante?cedula=0958476533&sede=GYE

http://localhost:5000/asistencia?cedula=0958476533&date_ini=2024-01-01&date_end=2024-01-30'