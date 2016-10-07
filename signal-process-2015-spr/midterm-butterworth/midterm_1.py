#libraries that needed for butterworth filter
from math import *
import numpy as np
from pylab import *
import random as ran
from scipy.signal import butter, lfilter

#Low-Pass Frequency Response Function
def lowpass_signal_func(frequency_domain_signal,f_c, nyq, n):
    h_lowpass=np.zeros(1000)
    lowpass_signal=np.zeros(1000)
    for i in range(len(frequency_domain_signal)):
            h_lowpass[i]=sqrt(1./(1+(i/(f_c/nyq))**(2*n)))
            lowpass_signal[i]=h_lowpass[i]*frequency_domain_signal[i]
    return lowpass_signal

#Ready to use function for butterworth filter
def butter_read_func(noise_signal,f_c1,f_c2, f_s, n):
    b,a=butter(n,[f_c1,f_c2],btype='band')
    signal=lfilter(b,a,noise_signal)
    return signal

#generating time domain
t=linspace(1, 1000,1000,endpoint=False)

#generating a clean signal
clean_signal = cos(t*pi/180)

#adding noise to clean signal
noise_signal=clean_signal
for i in range(len(clean_signal)):
    noise_signal[i]=noise_signal[i]*ran.uniform(1,1.1)

#Taking the Fast Fourier Transform of the signal
frequency_domain_signal=np.fft.fft(noise_signal)

#Sampling Rate
f_s=500.
#Nyquist Frequency
nyq=0.5 * f_s
#lower frequency limit
f_c1=150
#upper frequency limit
f_c2=400
#order of the response function
n=2
#Butterworth Filter
bandpass_signal=lowpass_signal_func(frequency_domain_signal,f_c2,nyq,n)-lowpass_signal_func(frequency_domain_signal,f_c1,nyq,n)

#Inverse fast fourier transform for filtered signal
filtered_signal=np.fft.ifft(bandpass_signal)

#Butterworth using ready to use function
butter_signal=butter_read_func(noise_signal,f_c1,f_c2, f_s, n)

#plotting the butterworth filtered signal
plot(butter_signal)

#plotting the filtered signal
plot(t,filtered_signal)

#plotting the original signal for comparison
plot(t,noise_signal)

show()
