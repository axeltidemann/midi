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
            value = 127 if snare else 0
            midi_out.send_message(footswitch[:2] + [value])
            snare = not snare

    sleep(.1)
