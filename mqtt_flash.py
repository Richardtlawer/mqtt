from gpiozero import LED

from time import sleep


import paho.mqtt.client as mqtt


led = LED(17)

def dot():
        led.on()
        sleep(1)
        led.off()
        sleep(1)
        
def message_type(message):
	       #print "msg.payload: " + message.payload
                if(message.payload=="ninja"):
                    dot()
                    dot()
                    print "yes man me bredda i"
                else:
                  print "no ninja"

def on_message(client, userdata, message):
       # print "msg: " + message.payload
        message_type(message)

def on_connect(client, userdata, flags, code):
    print "connected: " + str(code)
    client.subscribe("test/all")


client=mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message

client.connect("moorhouseassociates.com", 1883, 60)

client.loop_forever()


