#!/bin/bash

# Ruta del proyecto
cd /home/asistencias/api/API_ISTG

# Inicia Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app