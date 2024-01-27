import json
import logging

logging.basicConfig(level=logging.DEBUG,  # Puedes ajustar el nivel según tus necesidades (DEBUG, INFO, WARNING, ERROR, CRITICAL)
                    format='%(asctime)s - %(levelname)s - %(message)s')


def get_config():
    try:
        with open('config.json', 'r') as file:
            return json.load(file)

    except Exception as e:
        logging.debug(f"Error: {e}")
        return None
