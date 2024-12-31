
# Helper libraries
import pandas as pd
from scipy import signal
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import os

# print(meta_data.head())

# print(idx)
# if not os.path.exists(path+"\Spectograms"):
#     os.mkdir(path+"\Spectograms")
path = os.getcwd()
meta_data = pd.read_csv(path + '/musicnet_metadata.csv')
idx = []
for i in meta_data["id"]:
    idx.append(i)
window = 30
# print(idx)
for i in idx:
    if os.path.exists(path + "/train_data/"+ os.sep+ str(i)+".wav"):
        file= path +"/train_data/"+ os.sep+ str(i)+".wav"
        sample_rate, samples = wavfile.read(file)
        for j in range(len(samples)//(window*sample_rate)):
            # print(j)
            frequencies,times, spectogram = signal.spectrogram(samples[j*window*sample_rate:(j+1)*window*sample_rate],sample_rate)
            plt.pcolormesh(np.log(spectogram))
            plt.axis('off')
            plt.ylim(ymax = 40)
            temp = meta_data[meta_data['id']==int(1727)]
            composer = list(temp['composer'])[0]
            if not os.path.exists(path + "/Spectograms_cpu/" + os.sep  + composer):
                os.mkdir(path + "/Spectograms_cpu/" + os.sep + composer)
            if not os.path.exists(path + "/Spectograms_cpu/" + os.sep + composer + os.sep + str(i)):
                os.mkdir(path + "/Spectograms_cpu/" + os.sep + composer + os.sep + str(i))
            plt.savefig(path + "/Spectograms_cpu/" + os.sep + composer + os.sep + str(i) + os.sep + str(j) + ".png",transparent = True)

        # else:
        #         file= path+"/test_data/"+ os.sep+ str(i) +".wav"
        #         sample_rate, samples = wavfile.read(file)
        #         frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)
        #         plt.pcolormesh(np.log(spectrogram))
        #         plt.axis('off')
        #         plt.ylim(ymax=40)
        #         # plt.show() # Uncomment if you want to check out the plot.
        #         return plt.savefig(path+"/Spectograms/"+ os.sep + str(i) +".png", transparent=True)





