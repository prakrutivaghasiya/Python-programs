def returnSum(myDict): 
	
	sum = 0
	for i in myDict: 
		sum = sum + myDict[i] 
	
	return sum

dict = {'a': 140, 'b':207, 'c':560} 
print("Sum :", returnSum(dict)) 
