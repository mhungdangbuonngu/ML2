from os.path import join

def getPath() -> str:
    """
    Return the path to the folder contains this file
    """
    return __file__[:-len(__file__.split('\\')[-1])]

with open(join(getPath(),'weather_data.csv'),'r') as csv_file:
    lines = csv_file.readlines()
    for line in lines:
        try:
            oo = line.split(",")
            print(oo)
            missData = 0
            for col in range(3,9):
                if col == 8:
                    oo[col] = oo[col][:-1]
                if oo[col] == "0.0" or oo[col] == "0":
                    missData = 1
                    break
            if missData == 1:
                print("deleted")
                continue
            else:
                with open(join(getPath(),"new_data.csv"),'a') as new_file:
                    new_file.write(line)
        except ValueError:
            with open(join(getPath(),"new_data.csv"),'a') as new_file:
                new_file.write(line)
            continue