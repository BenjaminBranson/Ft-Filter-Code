import numpy as np
import scipy.io.wavfile as wav
import testSetInput
import matplotlib.pyplot as plt

testSetInput.generateTestWav()

samplerate, samples = wav.read('test.wav')

#sampleamount N
N = len(samples)

#Verständnis shit
#if N == 44100 * 5:
#    print("Test wav file generated successfully with correct sample amount.")

#print(samplerate)
#print(samples)
#print(N)

# graph wave 

timeAxis = np.linspace(0, N/samplerate, num=N)
plt.figure(figsize=(10, 4))
plt.axis((0, 0.25, -1.5, 1.5))
plt.plot(timeAxis, samples)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Waveform')
plt.show(block=False)