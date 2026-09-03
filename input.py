import numpy as np
import scipy.io.wavfile as wav
import testSetInput

testSetInput.generateTestWav()

samplerate, samples = wav.read('test.wav')

#sampleamount N
N = len(samples)

#Verständnis shit
#if N == 44100 * 5:
#    print("Test wav file generated successfully with correct sample amount.")

print(samplerate)
print(samples)