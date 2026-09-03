import numpy as np
from scipy.io.wavfile import write
import sounddevice as sd


def generateTestWav():
    #generate set test wav file
    samplerate = 44100

    #time
    t = np.linspace(0, 5, samplerate*5, endpoint=False)

    #Cmaj chord 
    sinWave = (np.sin(2 * np.pi * 262 * t) + np.sin(2 * np.pi * 330 * t) + np.sin(2 * np.pi * 392 * t))

    #normalize waveform to prevent distortion
    sinWave = sinWave / np.max(np.abs(sinWave))

    #play sound bc its fun
    sd.play(sinWave, samplerate)
    sd.wait()

    #create wav file
    return write('test.wav', samplerate, sinWave)

