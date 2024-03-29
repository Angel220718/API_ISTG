import pymysql
import logging
from flask import jsonify
from tools import config

logging.basicConfig(level=logging.DEBUG,  # Puedes ajustar el nivel según tus necesidades (DEBUG, INFO, WARNING, ERROR, CRITICAL)
                    format='%(asctime)s - %(levelname)s - %(message)s')


def connect_db():

    conf = config.get_config()
    logging.debug('Database config: ' + str(conf))

    try:
        conn = pymysql.connect(
            host=conf['host'],
            user=conf['user'],
            password=conf['pass'],
            db=conf['db']
        )

        return conn

    except pymysql.connect.Error as e:
        conn.close()
        logging.debug(f"Error: {e}")
        return None


def load_user(cedula, campus):

    try:
        conn = connect_db()
        cursor = conn.cursor()
        #result = cursor.execute('select * from asistencias')
        cursor.callproc('consultar_estudiante', [cedula, campus])

        res = cursor.fetchone()

        conn.commit()

        cursor.close()
        conn.close()
        connect_db().close()

        return jsonify(res)

    except pymysql.connect.Error as e:
        logging.error(f"Error: {e}")


def load_assistence(cedula, dateIni, dateEnd):

    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.callproc('consultar_asistencias', [cedula, dateIni, dateEnd])

        res = cursor.fetchall()

        conn.commit()

        cursor.close()
        conn.close()
        connect_db().close()

        return jsonify(res)

    except pymysql.connect.Error as e:
        logging.error(f"Error: {e}")
