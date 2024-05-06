B1 = {
    'eng1.012':[3,15.9],
    'eng1.013':[3,16],
    'eng1.014':[2,14.3],
    'bio1.001':[4,13.5],
    'che1.001':[4,13.1],
    'mat1.001':[4,14.9],
    'ict1.001':[3,16.6],
    'ict1.001':[3,16.6],	
	'mat1.002':[4,16.6],	
	'phy1.001':[4,16.2],
    'BIO1.002': [3,16.3],	
    'CHE1.002': [4,13.6],	
    'ICT1.002': [4,17.7],	
    'ICT1.003': [3,19.4],	
    'ICT1.004': [3,17.4],	
    'MAT1.003': [3,14.5],	
    'MAT1.004': [3,15.8],	
    'PHY1.002':	[4,12.4],	
    'MS1.001': [2,14.7]
}
B2 = {
    'MAT2.001':[3,16.8],
	'FR2.001':[4],	 	 					
	# 'PHI2.001':[2,11.5]	
	'MS2.005':[2],				
	'DS2.004':[3,11.9],
	'ICT2.001':[3,18.5],
	'ICT2.003':[4,16.8],
    'ICT2.004':[3,10.4],
	'ICT2.005':[3,15.5],
	'ICT3.002':[3],
    'FR2.002':[4],	 	 					
	# 'MS2.006':[2],					
	'ICT2.013':[4],	 	 					
	'MAT2.004':[3],	 	 					
    'DS2.005':[3], 	 					
	'ICT2.009':[3],	 	 					
	'DS2.001':[3,14.2],
    'ICT3.011':[3], 					
	'ICT2.010':[3],	 	 					
    'DS2.002':[3], 	 					
	'DS2.003':[3]	 	 					 	 					
}

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

print(GPA(B2))