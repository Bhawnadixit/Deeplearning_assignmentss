
# Helper libraries
import pandas as pd
from scipy import signal
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import os
import librosa
import librosa.display
import collections
import math


path = os.getcwd()
meta_data = pd.read_csv(path + '\\musicnet\\musicnet_metadata.csv')
id_x = []
for i in meta_data["id"]:
    id_x.append(i)

# CREATES FOLDER BASED ON CLASSES
# for x, y in collections.Counter(id_x).items():
#     if y > 1:
#         # print(x)
#         if not os.path.exists(path+x):
#             os.mkdir(path+x)

def fft(window, idx, path):
   # if not os.path.exists(path+"\\Spectograms_fft"):
   #     os.mkdir(path+"\\Spectograms_fft")

# print(idx)
    for i in idx:
        print(i)
        try:
        #        if os.path.exists(path + "\\musicnet\\train_data\\"+ os.sep+ str(i)+".wav"):
            file= path + "\\musicnet\\train_data\\"+ os.sep+ str(i)+".wav"
            sample_rate, samples = wavfile.read(file)
            for j in range(len(samples)//(window*sample_rate)):
                print(j)
                    # print(j*window*sample_rate)nperseg=window*sample_rate, noverlap=(window*sample_rate)//4
                    # d = signal.get_window(samples[j*window*sample_rate:(j+1)*window*sample_rate], (j+1)*window*sample_rate, fftbins=True)
                    # print(d)
                frequencies,times, spectogram = signal.spectrogram(samples[j*window*sample_rate:(j+1)*window*sample_rate],sample_rate)
                plt.pcolormesh(np.log(spectogram))
                plt.axis('off')
                plt.ylim(ymax = 40)
                temp = meta_data[meta_data['id']==int(1727)]
                composer = list(temp['composer'])[0]
                if not os.path.exists(path + "\\Spectograms_fft" + os.sep  + composer):
                    os.mkdir(path + "\\Spectograms_fft" + os.sep + composer)
                if not os.path.exists(path + "\\Spectograms_fft" + os.sep + composer + os.sep + str(i)):
                    os.mkdir(path + "\\Spectograms_fft" + os.sep  + composer + os.sep + str(i))
                plt.savefig(path + "\\Spectograms_fft" + os.sep + composer + os.sep + str(i) + os.sep + format(i)+'_'+str(j)+".png",transparent = True)
                plt.close()
        except:
            pass

def cqt(window, idx, path):
    if not os.path.exists(path+"\\Spectograms_cqt"):
        os.mkdir(path+"\\Spectograms_cqt")

    # print(idx)
    for i in idx:
        print(i)
        # if os.path.exists(path + "\\musicnet\\train_data\\"+ os.sep+ str(i)+".wav"):
        file = path + "\\musicnet\\train_data\\"+ os.sep+ str(i)+".wav"
        samples, sample_rate = librosa.load(file, sr=None)     # it sr =None takes original sampling rate
        for j in range(len(samples)//(window*sample_rate)):
            print(j)
            X1 = librosa.cqt(samples[j * window * sample_rate:(j + 1) * window * sample_rate])
            Xdb = librosa.amplitude_to_db(abs(X1), ref=np.max)
            plt.figure(figsize=(14, 5))
            librosa.display.specshow(Xdb, sr=sample_rate, x_axis='time', y_axis='hz')

            temp = meta_data[meta_data['id']==int(1727)]
            composer = list(temp['composer'])[0]
            if not os.path.exists(path + "\\Spectograms_cqt" + os.sep  + composer):
                os.mkdir(path + "\\Spectograms_cqt" + os.sep + composer)
            if not os.path.exists(path + "\\Spectograms_cqt" + os.sep + composer + os.sep + str(i)):
                os.mkdir(path + "\\Spectograms_cqt" + os.sep  + composer + os.sep + str(i))
            plt.savefig(path + "\\Spectograms_cqt" + os.sep + composer + os.sep + str(i) + os.sep + format(i)+'_'+str(j)+".png",transparent = True)
            plt.close()

def stft(window, idx, path):
    if not os.path.exists(path+"\\Spectograms_stft"):
        os.mkdir(path+"\\Spectograms_stft")

    # print(idx)
    for i in idx:
        print(i)
        # if os.path.exists(path + "\\musicnet\\train_data\\"+ os.sep+ str(i)+".wav"):
        file = path + "\\musicnet\\train_data\\"+ os.sep+ str(i)+".wav"
        samples, sample_rate = librosa.load(file, sr=None)     # it sr =None takes original sampling rate
        for j in range(len(samples)//(window*sample_rate)):
            print(j)
            X1 = librosa.stft(samples[j * window * sample_rate:(j + 1) * window * sample_rate])
            Xdb = librosa.amplitude_to_db(abs(X1), ref=np.max)
            plt.figure(figsize=(14, 5))
            librosa.display.specshow(Xdb, sr=sample_rate, x_axis='time', y_axis='hz')

            temp = meta_data[meta_data['id']==int(1727)]
            composer = list(temp['composer'])[0]
            if not os.path.exists(path + "\\Spectograms_stft" + os.sep  + composer):
                os.mkdir(path + "\\Spectograms_stft" + os.sep + composer)
            if not os.path.exists(path + "\\Spectograms_stft" + os.sep + composer + os.sep + str(i)):
                os.mkdir(path + "\\Spectograms_stft" + os.sep  + composer + os.sep + str(i))
            plt.savefig(path + "\\Spectograms_stft" + os.sep + composer + os.sep + str(i) + os.sep + format(i)+'_'+str(j)+".png",transparent = True)
            plt.close()

def mfcc(window, idx, path):
    if not os.path.exists(path+"\\Spectograms_mfcc"):
        os.mkdir(path+"\\Spectograms_mfcc")


    SAMPLE_RATE = 44100
    SEGMENT = 30  # duration
    num_mfcc = 13
    n_fft = 2048
    hop_length = 512
    samples_per_segment = SEGMENT * SAMPLE_RATE
    num_mfcc_vectors_per_segment = math.ceil(samples_per_segment / hop_length)

    for i in idx:
        print(i)
        # if os.path.exists(path + "\\musicnet\\train_data\\"+ os.sep+ str(i)+".wav"):
        file = path + "\\musicnet\\train_data\\"+ os.sep+ str(i)+".wav"
        signal, sample_rate = librosa.load(file, sr=SAMPLE_RATE)
        total_samples = len(signal)
        num_segments = int(total_samples / (SEGMENT * sample_rate))
        for j, d in zip(range(num_segments), range(len(signal)//(window*sample_rate))):
            start = samples_per_segment * d
            finish = start + samples_per_segment
            # print(finish)
            # extract mfcc
            mfcc = librosa.feature.mfcc(signal[start:finish], sample_rate, n_mfcc=num_mfcc, n_fft=n_fft, hop_length=hop_length)
            mfcc = mfcc.T
            if len(mfcc) == num_mfcc_vectors_per_segment:
                fig, ax = plt.subplots()
                librosa.display.specshow(mfcc, sr=sample_rate, cmap='gray_r', hop_length=hop_length)

                temp = meta_data[meta_data['id'] == int(1727)]
                composer = list(temp['composer'])[0]
                if not os.path.exists(path + "\\Spectograms_mfcc" + os.sep + composer):
                    os.mkdir(path + "\\Spectograms_mfcc" + os.sep + composer)
                if not os.path.exists(path + "\\Spectograms_mfcc" + os.sep + composer + os.sep + str(i)):
                    os.mkdir(path + "\\Spectograms_mfcc" + os.sep + composer + os.sep + str(i))
                plt.savefig(
                    path + "\\Spectograms_mfcc" + os.sep + composer + os.sep + str(i) + os.sep + format(i) + '_' + str(j) + ".png",
                    transparent=True)
                plt.close()

win= 30

fft(win, id_x, path)

