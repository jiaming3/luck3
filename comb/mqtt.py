 #do not use any function from this .py
import paho.mqtt.client as mqtt

import json
import time
receive_data = 1

def ini_mqtt():
 client = mqtt.Client(userdata=receive_data)
 client.connect("test.mosquitto.org",port=1883)
 def on_message(client, userdata, message):
   userdata = json.loads(message.payload)
   client.user_data_set(userdata)
 client.on_message = on_message()
 client.subscribe("IC.embedded/Team_ALG/#")
 

def publish_data(temp,hum,pressure,flower_pot):
  payload=json.dumps({"temp":temp,"humidity":hum,"pressure":pressure,"flowerpot":flower_pot})
  client.publish("IC.embedded/Team_ALG/test",payload)
  #default keep alive is 60s,thus we need at least 1 imformation change between broker and client per minutes#
  
def receive():
  client.loop_start()
  time.sleep(20) #change holding-connection-state time here
  client.loop_stop()
  return receive_data
   
  
  
  
