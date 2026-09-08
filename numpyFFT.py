import numpy as np
import scipy.io.wavfile as wav
import audioInput
import testSetInput
import matplotlib.pyplot as plt

#fft
fourier = np.fft.rfft(audioInput.samples)

#plot fft

#x axis, list 0->nyquist (/2)                  equal amount of values
plotAxis = np.linspace(0, audioInput.samplerate/2, num=audioInput.N//2+1)
plt.figure(figsize=(10, 4))
plt.axis((0, 2000, 0, 25000))
plt.plot(plotAxis, np.abs(fourier))
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.title('Frequency Spectrum')
plt.show(block=False)

#print(fourier)


