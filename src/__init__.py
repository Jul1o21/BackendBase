from flask import Flask
from config import dbname, host, password, user
from .routes import index
from src.mqtt_client import init_mqtt, mqtt_message_queue

app = Flask(__name__)

def init_app():
    init_mqtt()
    
    app.register_blueprint(index.main, url_prefix="/")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{dbname}'
    app.config['MQTT_MESSAGE_QUEUE'] = mqtt_message_queue
    return app

if __name__ == '__main__':
    app = init_app()
    app.run(debug=True)
