import json
from os.path import join

def getPath() -> str:
    """
    Return the path to the folder contains this file
    """
    return __file__[:-len(__file__.split('\\')[-1])]

def GPA(year:dict) -> float:
    """
    This function takes known marks to calculate GPA with respect to their credits
    """
    creditTotal:int = 0
    sum:float = 0
    for key in year.keys():
        marks = year.get(key)
        if len(marks) == 1:
            continue
        sum += marks[0] * marks[1]
        creditTotal += marks[0]
    return sum/creditTotal

def updateMark(subject:str, mark:float, year:dict, mode:str='add') -> dict:
    """
    Add or modify the saved result of a subject
    """
    if mode == 'add':
        try:
            year.get(subject).append(mark)
        except TypeError:
            print(f"There is no {subject}")
    elif mode == 'modify':
        try:
            year.get(subject)[1] = mark
        except TypeError:
            print(f"There is no {subject}")
    else:
        raise ValueError(f"Possible mode is 'add' or 'modify', got '{mode}'")
    return year

def saveToJson(fileName:str, year:dict) -> None:
    with open(join(getPath(),fileName),'w') as jf:
        json.dump(year,jf) 

def loadFromJson(path:str) -> dict:
    B1:dict
    with open(path,'r') as jf:
        B1 = json.load(jf)
    return B1

def isValidMark(mark:float) -> bool:
    try:
        mark = float(mark)
    except:
        return False
    if mark <= 20 and mark > 0:
        return True
    return False

def createDataSet(year:int) -> dict:
    """
    Create a new dict contains new marks for new person\n
    Input mark number for each subjects, none if there is no mark
    """
    if not year < 3 and year > 0:
        raise ValueError(f'Only accept year 1 2 3, got {year}')
    
    markDict = loadFromJson(join(getPath(),f'tempB{year}.json'))
    for key in markDict.keys():
        mark = input(f'{key}: ')
        if mark == 'none':
            continue
        while not isValidMark(mark):
            mark = input(f'reinput {key}, invalid value: ')
        markDict.get(key).append(float(mark))
    return markDict

if __name__ == "__main__":
    marks = createDataSet(2)
    print(GPA(marks))
    saveToJson('B2.json',marks)