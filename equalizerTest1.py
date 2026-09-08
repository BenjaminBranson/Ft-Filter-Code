import numpy as np
import scipy.io.wavfile as wav
import input
import testSetInput
import matplotlib.pyplot as plt
import numpyFFT
import sounddevice as sd

#try filtering bass

def bassFilter():
    for i in range(len(numpyFFT.fourier)):
        #250 defined as bass
        if numpyFFT.plotAxis[i] < 250:
            numpyFFT.fourier[i] = 0
    plotAxis = np.linspace(0, input.samplerate/2, num=input.N//2+1)
    plt.figure(figsize=(10, 4))
    plt.axis((0, 2000, 0, 25000))
    plt.plot(plotAxis, np.abs(numpyFFT.fourier), 'red')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Magnitude')
    plt.title('EqualizedFrequency Spectrum')
    plt.show(block=False)

    #new sound
    equalizedSound = np.fft.irfft(numpyFFT.fourier)

    #play new sound
    sd.play(equalizedSound, input.samplerate)

    #plot new sound
    timeAxis = np.linspace(0, input.N/input.samplerate, num=input.N)
    plt.figure(figsize=(10, 4))
    plt.axis((0, 0.25, -1.5, 1.5))
    plt.plot(timeAxis, equalizedSound)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.title('Equalized Sound')
    plt.show()

bassFilter()




    