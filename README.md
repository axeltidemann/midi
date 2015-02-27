# midi
Small programs that perform simple processing on MIDI signals. For use in my live rig.

The programs are pretty self-explanatory. I use them with Ableton Live, and assign the various controllers manually (i.e. when writing the program itself). For this reason, it is not entirely plug-and-play. Remember to set the input "python MIDI output" as a Remote in Preferences > MIDI Sync. It does not have to be armed for Track.

Install the additional tools for XCode before installing on a Mac. This way you will get all the developer command line tools you need to proceed. The only extra package you need is python-rtmidi. On my MacBook (not on my Air) I needed to pass an extra argument because of some clang compiler option errors that was introduced with a new version of the command line tools. You don't need to install RtMIDI separately this way, as the python-rtmidi will do it for you. Elegant!

```
ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future pip install python-rtmidi
```

So try without the ARCHFLAGS first.



