import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
        print message.payload

def on_connect(client, userdata, flags, code):
    print "connected: " + str(code)
    client.subscribe("test/all")


client=mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message
client.connect("moorhouseassociates.com", 1883, 60)

client.loop_forever()
