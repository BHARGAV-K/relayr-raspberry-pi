import time
from relayr import Client
from relayr.dataconnection import MqttStream
c = Client(token='<my_access_token>')
dev = c.get_device(id='<my_device_id>')
def mqtt_callback(topic, payload):
    print('%s %s' % (topic, payload))
stream = MqttStream(mqtt_callback, [dev])
stream.start()
time.sleep(10)
stream.stop()