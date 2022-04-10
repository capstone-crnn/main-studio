from cmath import sqrt
# from scipy.fft import fft, fftfreq
from scipy.fftpack import fft, fftfreq
from scipy.signal import butter, lfilter, sosfilt, sosfreqz, detrend
from scipy.stats import zscore
from scipy.ndimage.interpolation import shift
import numpy as np
np.set_printoptions(threshold = False)
import pandas as pd
import matplotlib.pyplot as plt
import csv
import time
import math
import Adafruit_ADS1x15

def motion_traj_opt (I,Q):
    x = np.zeros(len(I))
    accum = 0 
    for n in range(1, len(I)):
        accum = accum + I[n-1]*Q[n] - I[n]*Q[n-1]
        x[n] = accum
    return x

def butter_bandpass(lowcut, highcut, fs, order=5):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        sos = butter(order, [low, high], analog=False, btype='band', output='sos')
        return sos
    
def filter(sos, data):
    return sosfilt(sos, data)

def estimate_rate(y, x, rate_type):
    F1 = 0
    F2 = 0

    if rate_type == 'respiratory':
        F1 = 0.15
        F2 = 0.4
    elif rate_type == 'heart':
        F1 = 0.8
        F2 = 1.5

    rate = 0
    max_idx = 0
    for i in range(len(x)):
        if x[i] >= F1 and x[i] <= F2: #look at frequencies between these values
            if y[i] > y[i-1] and y[i] > y[i+1]: #take the peak
                if y[i] >= rate or y[i] > 0.001: #if greater than 0.001, then use this frequency
                    rate = y[i]
                    max_idx = i
    rate = x[max_idx]*60

    return rate

#DEFINE CONSTANTS/VARIABLES
FFT_BIN_LEN = 2048
INTERVAL_LEN = 32*20
SAMP_FREQ = 32
FFT_RES = SAMP_FREQ/FFT_BIN_LEN

I = np.zeros(INTERVAL_LEN)
Q = np.zeros(INTERVAL_LEN)
I_sec = np.zeros(SAMP_FREQ)
Q_sec = np.zeros(SAMP_FREQ)
resp_freq_buff = np.zeros(10)
index = 0

adc = Adafruit_ADS1x15.ADS1115()
butter_coeff = butter_bandpass(0.8,2,SAMP_FREQ,order=4)

while True:
    
    #READ 1 SEC BLOCK
    while (index < 32):
        s = time.time()
        I_sec[index] = adc.read_adc(0, gain=1, data_rate=860)
        Q_sec[index] = adc.read_adc(1, gain=1, data_rate=860)
        index = index + 1
        time.sleep(0.03125-(time.time()-s))
     
    s = time.time()
    index = 0
    
    #APPEND BLOCK TO 20-SEC INTERVAL
    I[:len(I)-len(I_sec)] = I[len(I_sec):]
    I[len(I)-len(I_sec):] = I_sec[:]
    
    Q[:len(Q)-len(Q_sec)] = Q[len(Q_sec):]
    Q[len(Q)-len(Q_sec):] = Q_sec[:]
    
    x = detrend(motion_traj_opt(I,Q))
    x = np.append(x,np.zeros(FFT_BIN_LEN-INTERVAL_LEN))
    
    #COMPUTE FFT AND GET MAX FREQ
    fftx = fft(x)
    xf = fftfreq(FFT_BIN_LEN,1/SAMP_FREQ)[:FFT_BIN_LEN//2]
    peak_freq_index = np.argmax(2/INTERVAL_LEN*np.abs(fftx[0:INTERVAL_LEN//2]))
    peak_freq = xf[peak_freq_index]
    
    #COMPUTE AVERAGE RESP FREQUENCY (last 10 seconds)
    resp_sd = np.std(resp_freq_buff)
    resp_ave = np.average(resp_freq_buff)
    resp_freq_buff = np.roll(resp_freq_buff, 1)
    resp_freq_buff[0] = peak_freq
    resp_zscore = zscore(resp_freq_buff)
    
    #DETERMINE RESP DETECTION
    # threshold = 0.5*resp_sd
    threshold = resp_sd
    for i in resp_zscore:
        if (abs(i) < threshold):
            resp_detection = 1
        else:
            resp_detection = 0
            break;
    for i in resp_freq_buff:
        if (i > 0.1 and i < 0.35):
            resp_detection = 1
        else:
            resp_detection = 0
            break
    
    #COMPUTE AVERAGE HEART FREQUENCY
    """
    x_filt = filter(butter_coeff, x)
    fftx_filt = fft(x_filt)
    xf_filt = fftfreq(FFT_BIN_LEN,1/SAMP_FREQ)[:FFT_BIN_LEN//2]
    """
    heart_ave = 0
    
    with open('shared_file', "w") as myfile:
        myfile.write(str([resp_ave*60, heart_ave, resp_detection]))
    
    # time.sleep(0.03125-(time.time()-s))
    temp_time = time.time() - s

    if(0.03125 - temp_time < 0):
        time.sleep(0.03125)
    else:
        time.sleep(0.03125 - temp_time)