import sys
from time import sleep

import rtmidi

import utils

midi_in = utils.IN(sys.argv)
midi_out = utils.OUT()

snare = False

while True:
    midi = midi_in.get_message()
    
    if midi:
        data, delta = midi
        if data == utils.footswitch_on:
            print 'Snare {}'.format('ON' if snare else 'OFF')
            midi_out.send_message(utils.footswitch_on if snare else utils.footswitch_off)
            snare = not snare

    sleep(.1)
