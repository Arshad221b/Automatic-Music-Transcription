from os import path
from pydub import AudioSegment

# files                                                                         
src = "test.mp3"
dst = "test1.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")
