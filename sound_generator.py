"""Python 2 and 3 sterio sound gnerator for breakdown of Ventriloquism"""
# it runs much faster with Python 2!

from struct import pack
from math import sin, pi
import wave
import random

SAMPLE_RATE = 44100 # in samples per second
FREQ = 400.0 # frequency in HZ
TIME = 10 # in seconds
STEPS = 1000 # decay steps
DECAY_RATE = 0.995 # decay per step
AMPLITUDE = 2 ** 15 - 1.0 # maximum amplitude
DECAY_DIR = 'Right' # which channel to decay

length = SAMPLE_RATE * TIME
step_lenght = length // STEPS
leftMaxVol = rightMaxVol = AMPLITUDE

wv = wave.open('%s_decay.wav'%DECAY_DIR, 'w')
wv.setparams((2, 2, SAMPLE_RATE, 0, 'NONE', 'not compressed'))
wvData = b''
for i in range(length):
    wvData += pack('h', int(leftMaxVol * sin(i * FREQ / SAMPLE_RATE))) # left
    wvData += pack('h', int(rightMaxVol * sin(i * FREQ / SAMPLE_RATE))) # right
    if i % step_lenght == 0:
        if DECAY_DIR == 'Left':
            leftMaxVol *= DECAY_RATE
        else:
            rightMaxVol *= DECAY_RATE

wv.writeframes(wvData)
wv.close()
