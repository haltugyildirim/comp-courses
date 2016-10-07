#libraries that needed for butterworth filter
from math import *
import numpy as np
from pylab import *
import random as ran
from scipy.signal import butter, lfilter

#Low-Pass Frequency Response Function
def lowpass_signal_func(t,frequency_domain_signal,f_c, nyq, n):
    h_lowpass=np.zeros(len(t))
    lowpass_signal=[]
    for i in range(len(frequency_domain_signal)):
            h_lowpass[i]=1-sqrt(1./(1+((i-nyq)/(f_c))**(2*n)))
            lowpass_signal.append(h_lowpass[i]*frequency_domain_signal[i])
    return lowpass_signal, h_lowpass

def scipy_lowpass_filter(frequency_domain_signal,f_c,nyq,n):
    cut=f_c/nyq
    b,a=butter(n,cut,btype='low')
    y=lfilter(b,a,frequency_domain_signal)
    return y


#Sampling Rate
f_s=1024.
#Nyquist Frequency
nyq=0.5 * f_s
#Generating Time Domain
t=linspace(0, f_s,f_s,endpoint=False)

#generating a clean signal
clean_signal = cos(t*pi/180)

#adding noise to clean signal
noise_signal=clean_signal
for i in range(len(clean_signal)):
    noise_signal[i]=noise_signal[i]*ran.uniform(1,1.05)

#Taking the Fast Fourier Transform of the signal
frequency_domain_signal=np.fft.fft(noise_signal,1024)

#Butterworth Filter
#Cutoff Frequency
f_c=400
#Order
n=8
frequency_domain_signal_filtered,G=lowpass_signal_func(t,frequency_domain_signal,f_c,nyq,n)
frequency_domain_signal_filtered_ready=scipy_lowpass_filter(frequency_domain_signal,f_c,nyq,n)

#Inverse fast fourier transform for filtered signal
filtered_signal=np.fft.ifft(frequency_domain_signal_filtered, 1024)
filtered_signal_ready=np.fft.ifft(frequency_domain_signal_filtered_ready, 1024)

#plot(t)
plot(noise_signal)
#plot(frequency_domain_signal)
#plot(G)
#plot(frequency_domain_signal_filtered)
#plot(frequency_domain_signal_filtered_ready)
plot(filtered_signal)
plot(filtered_signal_ready)

show()
