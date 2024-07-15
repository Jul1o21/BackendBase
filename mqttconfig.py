import random


broker_mq = 'k4e32f15.ala.dedicated.aws.emqxcloud.com'
port_mq = 1883
topic_mq = 'prueba/emqx'
client_id_mq = f'python-mqtt-{random.randint(0, 1000)}'
username_mq = 'emqx'
password_mq = 'admin'