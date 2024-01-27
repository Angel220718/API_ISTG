from flask import Flask, render_template, request, redirect
from tools import database

app = Flask(__name__)


'http://localhost:5000/estudiante?cedula=0958476533&campus=GYE'
@app.route('/estudiante', methods=['GET'])
def get_student():  # put application's code here

    cedula = request.args.get('cedula', '')
    campus = request.args.get('campus', '')

    users = database.load_user(cedula, campus)

    return users


'http://localhost:5000/asistencia?cedula=0958476533&date_ini=2024-01-01&date_end=2024-01-30'
@app.route('/asistencia', methods=['GET'])
def get_asistence():  # put application's code here

    cedula = request.args.get('cedula', '')
    date_ini = request.args.get('date_ini', '')
    date_end = request.args.get('date_end', '')

    assistence = database.load_assistence(cedula, date_ini, date_end)

    return assistence


@app.route('/', methods=['GET'])
def index():
    return "API activa"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
