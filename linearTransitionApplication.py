import numpy as np
import scipy.io.wavfile as wav
import audioInput
import testSetInput
import matplotlib.pyplot as plt
import numpyFFT
import sounddevice as sd
import linearTransitionFunction as ltf

linearFunction = ltf.linearTransition()
linearFilteredFourier = np.multiply(numpyFFT.fourier, linearFunction)

plotAxis = np.linspace(0, audioInput.samplerate/2, num=audioInput.N//2+1)

plt.figure(figsize=(12, 7))

# Before linear transformation
plt.subplot(3, 1, 1)
plt.plot(plotAxis, np.abs(numpyFFT.fourier[:audioInput.N//2+1]))
plt.axis((0, 2000, 0, 25000))
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.title('Frequency Spectrum Before Linear Transformation')
plt.grid()

# linear function plot
plt.subplot(3, 1, 2)
plt.plot(numpyFFT.plotAxis, linearFunction)
plt.axis((0, 2000, 0, 20))
plt.xlabel('Frequency [Hz]')
plt.ylabel('Gain')
plt.title('Linear Transition Function')
plt.grid()

# After linear transformation
plt.subplot(3, 1, 3)
plt.plot(plotAxis, np.abs(linearFilteredFourier[:audioInput.N//2+1]))
plt.axis((0, 2000, 0, 25000))
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.title('Frequency Spectrum After Linear Transformation')
plt.grid()

plt.tight_layout()
plt.show()
