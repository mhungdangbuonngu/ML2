from os.path import join

def getPath() -> str:
    """
    Return the path to the folder contains this file
    """
    return __file__[:-len(__file__.split('\\')[-1])]

with open(join(getPath(),'energy_datacsv.csv'),'r') as inputFile:
    lines = inputFile.readlines()
    for line in lines:
        line = line[:-3]
        line = line.replace(',','.')
        line = line.replace(';',',')
        with open(join(getPath(),'energy_data.csv'),'a') as outputFile:
            outputFile.write(line + "\n")
        print(line)