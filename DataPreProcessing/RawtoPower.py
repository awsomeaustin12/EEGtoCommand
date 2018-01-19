import numpy as np
import pandas as pd
import datetime
import tensorflow as tf



df = pd.read_csv('EEGRaw')
batch_size = 500



class RawtoPower():
    def __init__(self):
        raw = np.shape(batch_size,np.shape(0,12))
        labels = df[:,10]

    #for i in range(batch_size):



