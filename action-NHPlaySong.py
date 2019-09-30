#!/usr/bin/env python3
#encoding: utf-8
import paho.mqtt.client as mqtt 
import json
import io
import time
import vlc

def on_connect(client, userdata, flags, rc): 
    print('Connected') 
    mqtt.subscribe('hermes/intent/NHPlaySong')

def on_message(client, userdata, msg):
    # Parse the json response
    intent_json = json.loads(msg.payload)
    intentName = intent_json['intent']['intentName']
    slots = intent_json['slots']
    print('Intent {}'.format(intentName))
    for slot in slots:
        slot_name = slot['slotName']
        raw_value = slot['rawValue']
        value = slot['value']['value']
        print('Slot {} -> \n\tRaw: {} \tValue: {}'.format(slot_name, raw_value, value))
        
class PlaySong(song_name, artist_name):
    song_name = intentMessage.slots.song_name.first().value
    artist_name = intentMessage.slots.artist_name.first().value
    
    sound = str("/media/pi/Verbatim1/music/artists/" + artist_name + "/all/" + song_name + ".mp3")
    
    player.play(sound)  
        
if __name__ == "__main__":
    PlaySong()
        
mqtt = mqtt.Client() 
mqtt.on_connect = on_connect
mqtt.on_message = on_message
mqtt.connect('raspberrypi.local', 1883) 
mqtt.loop_forever()

