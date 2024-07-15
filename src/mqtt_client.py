from paho.mqtt import client as mqtt_client
from mqttconfig import client_id_mq, username_mq, password_mq, broker_mq, port_mq
from src.database.db import connection
import threading
import time
import queue

mqtt_message_queue = queue.Queue()
last_message_time = time.time()

def postMessage(contenido):
    try:
        conn = connection()
        inst = '''
                INSERT INTO mensajes (contenido)
                VALUES (%(contenido)s);
               '''
        with conn.cursor() as cursor:
            cursor.execute(inst, {'contenido': contenido})
            conn.commit()
            cursor.close()
        conn.close()
        print("Mensaje insertado en la base de datos.")
    except Exception as e:
        print("(SISTEMA)   Error al insertar el mensaje: " + str(e))

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            client.subscribe('prueba/emqx')
        else:
            print("Failed to connect, return code %d\n" % rc)
    
    def on_message(client, userdata, msg):
        global last_message_time
        message = msg.payload.decode()
        mqtt_message_queue.put(message)
        last_message_time = time.time()
        print(f"Received `{message}` from `{msg.topic}` topic")
        # Aquí se inserta el mensaje en la base de datos
        postMessage(message)  # Solo pasamos el contenido

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

def check_for_empty_messages():
    global last_message_time
    while True:
        time.sleep(5)
        if time.time() - last_message_time > 5:
            mqtt_message_queue.put("EMPTY")
            print("No hay mensajes detectados")

def start_mqtt():
    client = connect_mqtt()
    client.loop_start()
    threading.Thread(target=check_for_empty_messages).start()

def init_mqtt():
    mqtt_thread = threading.Thread(target=start_mqtt)
    mqtt_thread.start()
