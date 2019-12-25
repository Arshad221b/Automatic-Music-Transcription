import sys
from os import listdir
from os.path import join, isfile
from subprocess import call
from scipy import signal
from scipy.io import wavfile
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import audiospec
import argparse
import cqt
import os
import librosa
path   = 'dataMIDI/'
path2  = 'dataWAV/'
path3  = 'dataSPEC/'

files  = os.listdir(path)
files2 = os.listdir(path2)
files3 = os.listdir(path3)

def wav_to_spectrogram(wav_file, output, segment=None):

  cqt.plot_cqt(wav_file, output)

def midi_to_wav(midi_file, output):

  command = ['timidity', midi_file,'-Ow', '-o', output]
  return call(command)

midis =  [x for x in files  if x.endswith('.mid')]
wavs  =  [x for x in files2 if x.endswith('.wav')]
specs =  [x for x in files3 if x.endswith('.jpg')]

for midi in midis:
    print(midi)
    name = midi[:-4]
    #if name + '.wav' not in wavs:
    #   midi_to_wav(join(path, midi), join(path2, name + '.wav'))
    if name + '.jpg' not in specs:
      wav_to_spectrogram(join(path2, name + '.wav'), join(path3, name + '.jpg'))