#!/usr/bin/python

import datetime
import time
import jwt
import paho.mqtt.client as mqtt
import random

# Define some project-based variables
ssl_private_key_filepath = '/Users/vcubells/Developer/iot/demo_private.pem'
ssl_algorithm = 'RS256'  # Either RS256 or ES256
root_cert_filepath = '/Users/vcubells/Developer/iot/roots.pem'
project_id = 'test-vcn-249912'
gcp_location = 'us-central1'
registry_id = 'semana-i'
device_id = 'rpi'

# Get current time

cur_time = datetime.datetime.utcnow()

# Create a JWT

def create_jwt():
    token = {
        'iat': cur_time,
        'exp': cur_time + datetime.timedelta(minutes=60),
        'aud': project_id
    }

    with open(ssl_private_key_filepath, 'r') as f:
        private_key = f.read()

    return jwt.encode(token, private_key, ssl_algorithm)


_CLIENT_ID = 'projects/{}/locations/{}/registries/{}/devices/{}'.format(
    project_id, gcp_location, registry_id, device_id)
_MQTT_TOPIC = '/devices/{}/events'.format(device_id)

client = mqtt.Client(client_id=_CLIENT_ID)
# authorization is handled purely with JWT, no user/pass, so username can be whatever
client.username_pw_set(
    username='unused',
    password=create_jwt())


def error_str(rc):
    return '{}: {}'.format(rc, mqtt.error_string(rc))


def on_connect(unusued_client, unused_userdata, unused_flags, rc):
    print('on_connect', error_str(rc))


def on_publish(unused_client, unused_userdata, unused_mid):
    print('on_publish')


client.on_connect = on_connect
client.on_publish = on_publish

# Replace this with 3rd party cert if that was used when creating registry
client.tls_set(ca_certs=root_cert_filepath)
client.connect('mqtt.googleapis.com', 8883)
client.loop_start()

# Could set this granularity to whatever we want based on device, monitoring needs, etc
temperature = 0
humidity = 0
pressure = 0


for i in range(1, 11):
    cur_temp = random.randint(0,40)
    cur_pressure = random.random()
    cur_humidity = random.uniform(0.0,100.0)

    if cur_temp == temperature and cur_humidity == humidity and cur_pressure == pressure:
        time.sleep(1)
        continue

    temperature = cur_temp
    pressure = cur_pressure
    humidity = cur_humidity

    payload = '{{ "ts": {}, "temperature": {}, "pressure": {}, "humidity": {} }}'.format(
        int(time.time()), temperature, pressure, humidity)

    # Uncomment following line when ready to publish
    client.publish(_MQTT_TOPIC, payload, qos=1)

    print("{}\n".format(payload))

    time.sleep(1)

client.loop_stop()
