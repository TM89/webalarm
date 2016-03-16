#imports
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
import json
from StringIO import StringIO
import ast

#GPIO setup
LED = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)

#mqtt functions
def on_connect(client, userdata, flags, rc):
        print "connected"
        client.subscribe("home/livingroom",0)

def on_message(client, userdata, msg):
        print "on message"
        d = ast.literal_eval(str(msg.payload))
        print d['output']
        if str(d['output']) == str("led"):
                print "calling ledAction"
                ledAction(d['action'])

#gpio functions
def ledAction(turnOn):
        print "ledAction"
        GPIO.output(LED, turnOn)

#mqtt setup
client = mqtt.Client()
client.on_message = on_message
client.on_connect = on_connect
client.connect("localhost",1883,60)
print "past connect"

client.loop_forever()
