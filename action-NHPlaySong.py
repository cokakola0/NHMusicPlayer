#!/usr/bin/env python3
#encoding: utf-8
import paho.mqtt.client as mqtt 
import json
import io
import time
import vlc

def on_message(client, userdata, msg):
    if msg.topic == 'hermes/intent/#':
        payload = json.loads(msg.payload)
        name = payload["intent"]["intentName"]
        slots = payload["slots"]
        artist_name = str(intentMessage.slots.artist_name.first().value)
        song_name = str(intentMessage.slots.song_name.first().value)

class PlaySong(song_name, artist_name):
    sound = str("/media/pi/Verbatim1/music/artists/" + artist_name + "/all/" + song_name + ".mp3")
    
    player.play(sound)  
        
if __name__ == "__main__":
    PlaySong()
        
mqtt = mqtt.Client() 
mqtt.on_connect = on_connect
mqtt.on_message = on_message
mqtt.connect('raspberrypi.local', 1883) 
mqtt.loop_forever()
