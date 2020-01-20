
import numpy as np
import utils
import pretty_midi
from keras.models import load_model
import os
from PIL import Image

def test():
    model       = load_model('ckpt3.h5')
    images_path = 'testimg/'
    midi_path   = 'testmid/'


    y     = []
    z     = []
    final = []
    i = 0
    acc = 0
    for song in os.listdir(images_path):
        im      = Image.open(images_path+str(song))
        resize  = im.resize((601, 308), Image.NEAREST)
        x       = []
        arr     = np.asarray(resize, dtype="float32")
        x.append(arr)
        x       = np.array(x)
        x /= 255.0
        y1      = model.predict(x)
        result  = np.where(y1 == np.amax(y1))
        y.append(result)


        m_fn    = song.replace(".jpg", ".mid")
        act_song= pretty_midi.PrettyMIDI(os.path.join(midi_path, m_fn))
        oh      = utils.pretty_midi_to_one_hot(act_song)
        result2 = np.where(oh == np.amax(oh))
        z.append(result2)
        if abs(result[1][0]-result2[0][0]) < 2:
            acc = acc + 1
        if result2[0][0] != 0:
            i= i + 1
        final.append(str(result[1][0]))
        #array_size = len(final)
        #print(str(song)+str(result2[0][0]) + '  ' + str(result[1][0]))

    total = (acc/i)*100
    #print('Accuracy is '+str(total))
    #print(array_size)
    return(final)

#print(test())
