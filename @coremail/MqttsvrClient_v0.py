import paho.mqtt.client as paho
import os
import time
import sys
 
broker = "10.12.100.109"
port = 6900
username = "admin@emi.cn"
passwd = "{SES}BAENmEUULoUroPNwyGUUPUkPjBpQhAkg"
 
def on_message(mosq, obj, msg):
        print("Message received on topic "+msg.topic+" with QoS "+str(msg.qos)+" and payload "+msg.payload)
        sys.stdout.flush()
 
mypid = os.getpid()
client_uniq = "pubclient_"+str(mypid)
mqttc = paho.Client()

try:
    #connect to broker
    mqttc.username_pw_set(username, passwd)
    mqttc.on_message = on_message
    mqttc.connect(broker, port, 60)
    mqttc.subscribe([("admin", 0), ("nancy", 0), ("mail", 0)])

    while mqttc.loop() == 0:
       pass
except Exception,e:
    print e
