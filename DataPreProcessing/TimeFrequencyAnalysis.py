import numpy as np
import matplotlib.pyplot as plt

import mne
from mne.time_frequency import tfr_morlet, psd_multitaper
from mne.datasets import somato, sample

path_name = 'Waiting_to_be_Set'
raw_fname = path_name + '/MEG/name/filetype.fif'



raw = mne.io.read_raw_eeglab(raw_fname)
events = mne.find_events(raw, stim_channel='STI 014')




