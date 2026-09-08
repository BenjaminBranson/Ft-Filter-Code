import numpy as np
import scipy.io.wavfile as wav
import testSetInput
import matplotlib.pyplot as plt
import sounddevice as sd

#testSetInput.generateTestWav()

#samplerate, samples = wav.read('test.wav')
samplerate, samples = wav.read('file_example_WAV_1MG.wav')

#stereo to mono
if len(samples.shape) == 2:
    samples = np.mean(samples, axis=1)
    samples = samples/32768
sd.play(samples, samplerate)
sd.wait()
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
plt.axis((0, N/samplerate, -1.5, 1.5))
plt.plot(timeAxis, samples)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Waveform')
#plt.show(block=False)