import pandas as pd
from os.path import join as joinPath

def getPath() -> str:
    """
    Return the path to the folder contains this file
    """
    return __file__[:-len(__file__.split('\\')[-1])]

valorantPlayerDataset = pd.read_csv(joinPath(getPath(),'valorant_player.csv'))

print(valorantPlayerDataset)

