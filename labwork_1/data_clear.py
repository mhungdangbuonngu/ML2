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
            date = line.split(",")[0]
            time = date.split()[1]
            hour = time.split(":")[0]
            if int(hour)%8 == 0:
                print(date)
                with open(join(getPath(),"new_data.csv"),'a') as new_file:
                    new_file.write(line)
        except ValueError:
            with open(join(getPath(),"new_data.csv"),'a') as new_file:
                new_file.write(line)
            continue