import rtmidi

footswitch_on = [185, 4, 127]
footswitch_off = [185, 4, 0]

def IN(argv):
    midi_in = rtmidi.MidiIn()
    print 'Available MIDI inputs:'
    for port, name in enumerate(midi_in.get_ports()):
        print '\t{}: {}'.format(port, name)

    input_port = 0 if len(argv) == 1 else int(argv[1])

    print 'Opening input port "{}"'.format(midi_in.get_port_name(input_port))
    midi_in.open_port(input_port)

    return midi_in

def OUT(virtual_out='python MIDI output'):
    midi_out = rtmidi.MidiOut()
    print 'Creating virtual port "{}"'.format(virtual_out)
    midi_out.open_virtual_port(virtual_out)
    
    return midi_out
