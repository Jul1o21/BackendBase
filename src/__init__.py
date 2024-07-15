from flask import Flask
from config import dbname, host, password, user
from .routes import index
from paho.mqtt import client as mqtt_client
from mqttconfig import client_id_mq, username_mq, password_mq, broker_mq, port_mq
import threading
import time

app = Flask(__name__)

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            client.subscribe('prueba/emqx')
        else:
            print("Failed to connect, return code %d\n" % rc)
    
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    # Set Connecting Client ID
    client = mqtt_client.Client(client_id=client_id_mq, protocol=mqtt_client.MQTTv311, transport="tcp", callback_api_version=mqtt_client.CallbackAPIVersion.VERSION1)
    client.username_pw_set(username_mq, password_mq)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker_mq, port_mq)
    return client

def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish('prueba/emqx', msg)
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `prueba/emqx`")
        else:
            print(f"Failed to send message to topic `prueba/emqx`")
        msg_count += 1

def start_mqtt():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

def init_app():
    mqtt_thread = threading.Thread(target=start_mqtt)
    mqtt_thread.start()
    
    app.register_blueprint(index.main, url_prefix="/")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{dbname}'
    return app

if __name__ == '__main__':
    app = init_app()
    app.run(debug=True)
