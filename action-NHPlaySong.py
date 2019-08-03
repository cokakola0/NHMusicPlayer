#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
from hermes_python.hermes import Hermes
from hermes_python.ffi.utils import MqttOptions
from hermes_python.ontology import *
import io
import vlc
import time

CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"

class SnipsConfigParser(configparser.SafeConfigParser):
    def to_dict(self):
        return {section : {option_name : option for option_name, option in self.items(section)} for section in self.sections()}


def read_configuration_file(configuration_file):
    try:
        with io.open(configuration_file, encoding=CONFIGURATION_ENCODING_FORMAT) as f:
            conf_parser = SnipsConfigParser()
            conf_parser.readfp(f)
            return conf_parser.to_dict()
    except (IOError, configparser.Error) as e:
        return dict()

def subscribe_intent_callback(hermes, intentMessage):
    conf = read_configuration_file(CONFIG_INI)
    action_wrapper(hermes, intentMessage, conf)


def NHMusicPlayer(hermes, intentMessage, conf):
    {{song_name = intentMessage.slots.song_name.first().value
      artist_name = intentMessage.slots.artist_name.first().value

      """
      player = vlc.MediaPlayer("/media/pi/Verbatim/music/artists/" + artist_name + "/all/" + song_name + ".mp3")
      player.play()
      """

      sound = str("/media/pi/Verbatim/music/artists/" + artist_name + "/all/" + song_name + ".mp3")

      def Sound(sound):
          vlc_instance = vlc.Instance()
          player = vlc_instance.media_player_new()
          media = vlc_instance.media_new(sound)
          player.set_media(media)
          player.play()
          time.sleep(1.5)
          duration = player.get_length() / 1000
          time.sleep(duration)}}
    {{/each}}


if __name__ == "__main__":
    mqtt_opts = MqttOptions()
    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intent("{{intent_id}}", subscribe_intent_callback) \
         .start()
