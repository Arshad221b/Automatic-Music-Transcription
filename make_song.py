import numpy as np
import utils
import pretty_midi
from keras.models import load_model
import os
from PIL import Image
import re

model       = load_model('ckpt3.h5')
images_path = 'data4_test/'
midi_path   = 'data2_test/'

y = []
z = []

filenums = []
for song in os.listdir(images_path):
    im      = Image.open(images_path+str(song))
    resize  = im.resize((601, 308), Image.NEAREST)
    x       = []
    arr     = np.asarray(resize, dtype="float32")
    x.append(arr)
    x       = np.array(x)
    x /= 255.0
    y.append(model.predict(x))
    filenums.append(int(re.search(r'\d+', song).group()))
    print(song)

    
notes_unsorted = [np.argmax(y[n]) for n in range(len(y))]

notes = [x for _,x in sorted(zip(filenums, notes_unsorted))]
print(notes)

i=0
for note in notes:
	one_hot = np.zeros((128, 25))
	one_hot[note, :] = 1
	mid = utils.one_hot_to_pretty_midi(one_hot)
	mid.write('output_songs/daylight_' + str(i) + ".mid")
	i += 1
