import numpy as np
import scipy.io.wavfile as wav
import audioInput
import testSetInput
import matplotlib.pyplot as plt
import numpyFFT
import sounddevice as sd


bassMultiplier = int(input("Enter bass multiplier: "))
midrangeMultiplier = int(input("Enter midrange multiplier: "))
trebleMultiplier = int(input("Enter treble multiplier: "))

def Equalizer(bassMultiplier, midrangeMultiplier, trebleMultiplier):


    for i in range(len(numpyFFT.fourier)):
    #250 defined as bass
        if numpyFFT.plotAxis[i] < 250:
            numpyFFT.fourier[i] *= bassMultiplier
        elif 250 <= numpyFFT.plotAxis[i] < 4000:
            numpyFFT.fourier[i] *= midrangeMultiplier
        else:
            numpyFFT.fourier[i] *= trebleMultiplier


    plotAxis = np.linspace(0, audioInput.samplerate/2, num=audioInput.N//2+1)
    plt.figure(figsize=(10, 4))
    plt.axis((0, 2000, 0, 25000*max(bassMultiplier, midrangeMultiplier, trebleMultiplier)))
    plt.plot(plotAxis, np.abs(numpyFFT.fourier), 'red')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Magnitude')
    plt.title('EqualizedFrequency Spectrum')
    plt.show(block=False)

    #new sound
    equalizedSound = np.fft.irfft(numpyFFT.fourier)

    #play new sound
    sd.play(equalizedSound, audioInput.samplerate)

    #plot new sound
    timeAxis = np.linspace(0, audioInput.N/audioInput.samplerate, num=audioInput.N)
    plt.figure(figsize=(10, 4))
    plt.axis((0, 0.25, -1.5, 1.5))
    plt.plot(timeAxis, equalizedSound, 'red')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.title('Equalized Sound')
    plt.show()