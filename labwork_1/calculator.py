import pandas as pd
import numpy
from os.path import join as joinPath

def getPath() -> str:
    """
    Return the path to the folder contains this file
    """
    return __file__[:-len(__file__.split('\\')[-1])]

valorantPlayerDataset = pd.read_csv(joinPath(getPath(),'valorant_player.csv'))

weatherDataset = pd.read_csv(joinPath(getPath(),'weather_data.csv'))
# print(valorantPlayerDataset)

