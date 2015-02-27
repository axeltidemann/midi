import sys
import time
import multiprocessing as mp

import rtmidi

import utils

midi_in = utils.IN(sys.argv)
midi_out = utils.OUT()

run = False

stop = [185, 5, 127]
start = [185, 6, 127]
next_marker = [185, 7, 127]

wait_time = 3

# RtMIDI does not like to be started in a subprocess, apparently.
def counter():
    for i in range(wait_time):
        time.sleep(1)
        print i
    print 'ALL CLEAR'

while True:
    midi = midi_in.get_message()
    if midi:
        data, delta = midi
        if data == utils.footswitch_on:
            pressed = time.time()

            process = mp.Process(target=counter)
            process.start()

        now = time.time()
        if data == utils.footswitch_off and now - pressed < wait_time:
            print 'TOO SLOW, AMIGO!'
            process.terminate()

        if data == utils.footswitch_off and now - pressed > wait_time:
            if run:
                midi_out.send_message(stop)
                print 'Stop'
            else:
                midi_out.send_message(next_marker)
                midi_out.send_message(start)
                print 'Jump to next marker & start' 

            run = not run

    time.sleep(.1)
