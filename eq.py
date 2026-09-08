import numpy as np
import scipy.io.wavfile as wav
import audioInput
import testSetInput
import matplotlib.pyplot as plt
import numpyFFT
import sounddevice as sd


bassMultiplier = float(input("Enter bass multiplier: "))
midrangeMultiplier = float(input("Enter midrange multiplier: "))
trebleMultiplier = float(input("Enter treble multiplier: "))

def Equalizer(bM, mM, tM):


    for i in range(len(numpyFFT.fourier)):
    #250 defined as bass
        if numpyFFT.plotAxis[i] < 250:
            numpyFFT.fourier[i] *= bM
        elif 250 <= numpyFFT.plotAxis[i] < 4000:
            numpyFFT.fourier[i] *= mM
        else:
            numpyFFT.fourier[i] *= tM


    plotAxis = np.linspace(0, audioInput.samplerate/2, num=audioInput.N//2+1)
    plt.figure(figsize=(10, 4))
    plt.axis((0, 2000, 0, 25000))
    plt.plot(plotAxis, np.abs(numpyFFT.fourier), 'red')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Magnitude')
    plt.title('EqualizedFrequency Spectrum')
    #plt.show(block=False)

    #new sound
    equalizedSound = np.fft.irfft(numpyFFT.fourier)

    #play new sound in comparison to original sound
    sd.play(audioInput.samples, audioInput.samplerate)
    sd.wait()
    sd.play(equalizedSound, audioInput.samplerate)
    sd.wait()

    #plot new sound
    timeAxis = np.linspace(0, audioInput.N/audioInput.samplerate, num=audioInput.N)
    plt.figure(figsize=(10, 4))
    plt.axis((0, audioInput.N/audioInput.samplerate, -1.5, 1.5))
    plt.plot(timeAxis, equalizedSound, 'red')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.title('Equalized Sound')
    plt.show()

Equalizer(bassMultiplier, midrangeMultiplier, trebleMultiplier)