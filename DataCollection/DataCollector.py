import mne
import os.path as op
from matplotlib import pyplot as plt
import numpy as np


class DataCollector:
    def __init__(self):
        n_channels = 64
        sampling_rate = 400
        channel_names = ['eegT1', 'eegT2', 'eegF1', 'eegf2', 'eegP1', 'eegP2', 'eegO1', 'eegO2']
        channel_types = ['eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg']
        montage = 'standard_1005' #referential montage

        info = mne.create_info(channel_names,sampling_rate,channel_types,montage=montage)


        data_path = "datapathyetTBD"
        raw = mne.io.read_raw_fif(op.join(data_path,'EEG', 'nameTBD', 'nameTBD.fif'))





    def changeNames(self,indexofChange,newElectode,channel_names):
        channel_names[indexofChange] = newElectode

    def setMontage(self,indexOfChange,montageType,montage):
        montage = montageType

    def createDescriptio(self,description,info):
        info['description'] = description

    def identifyBadChannels(self,badChannels,info):
        info['bads'] = badChannels

    def printInfo(self,info):
        print(info)

    def constructEventArray(self,stimChannel,rawFile):
        events = mne.find_events(raw=rawFile,stim_channel=stimChannel)

    def printNumberEvents(self, events):
        print('Number of events:', len(events))

    def printUniqueEvents(self,events):
        print('Unique Event Codes:', np.unique(events[:,2]))


