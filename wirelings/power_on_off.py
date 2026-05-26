#!/usr/bin/env python3
# button_power.py
# hold the large button for 2 seconds to trigger shutdown

import time
import subprocess
import tinycircuits_wireling

PORT = 3 # change if using different port
HOLD_TIME = 2 # seconds

wireling = tinycircuits_wireling.Wireling()

print('Power button monitor running. Hold button to shut down.')

pressed_since = None

while True:
    state = wireling.digtialRead(PORT) # 0 = presssed, 1 = not pressed

    if state == 0:
        if pressed_since is None:
            pressed_since = time.time()
        elif time.time() - pressed_since >= HOLD_TIME:
            print('Shutting down...')
            subprocess.run(['sudo', 'shutdown', '-h', 'now'])
            break
    else:
        pressed_since = None # reset if released early