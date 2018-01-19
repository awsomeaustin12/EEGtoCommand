import numpy as np
import mne
from mne.datasets import sample


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


