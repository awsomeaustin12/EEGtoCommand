import numpy as np
import mne
from mne.datasets import sample
import mne.filter.filter_data


class DataFilter():

    def __init__(self):
        data_path = "path_yet_to_be_made"
        raw_fname = data_path + 'EEG/Theta/R'
        #proj_fname =

        tmin, tmax = 0,100  #going to use first 100 of training data

        raw = mne.io.read_raw_fif(raw_fname)
        raw = raw.crop(tmin,tmax)
        raw.info['bads'] = ['T4', 'F1']

        fmin, fmax = 10,300
        power_fft = 2048



    def dropElectrodes(self, bad, raw_fname, droppedElectrode):
        bad += droppedElectrode
        evoked = mne.read_evokeds(raw_fname, condition='Parietal', baseline=(None,0))

        #restrict the evoked to EEG channels
        evoked.pick_types(meg=False,eeg=True,exclude=[])

    def plotBads(self,evoked):
        evoked.plat(exclude=[])
        print(evoked.info['bads'])


if __name__ == "__main__":

    data_path = "path_yet_to_be_made"
    raw_fname = data_path + "/EEG/nametbd/tbdname.fif"
    # proj_fname = ""

    tmin, tmax = 0, 100   #going to use first 100 of training data


    raw = mne.io.read_raw_fif(raw_fname)
    raw = raw.crop(tmin, tmax)
    raw.info['bads'] = ['EEGn1','EEGn2'] #the numbers of the channels will be filtered out at

    fmin, fmax = 10, 300  #choose the frequency values we look to inspect
    power_fft = 2048 #the FFT size (number of size of professor)


    #region name tat we will be filtering out
    region_name = 'Left-Temporal' #wherever the region of the brain where commands are given

    #pick a subset of channels(here for a speed reason{)
    selection = mne.read_selection(region_name)
    picks = mne.pick_types(raw.info,meg=False,eeg=True,eog=False,stim=False,exclude='bads',selection=selection)

    raw.plot_psd(area_mode='range', tmax=10.0, picks=picks, average=False)

    sampling_rate = 400 #how much to be determined
    # EEGsize1 =   tbd depends on how much data
    # EEGsize2 =   tbd depends on how much data
    # EEGsize3 =   tbd depends on how much data


    highPassFilter = False
    #choose what type of filter you want
    if(highPassFilter):



#we can remove noise using a notch filter
raw.notch_filter(np.arrange())