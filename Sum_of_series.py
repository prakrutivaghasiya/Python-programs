
def sumOfSeries(n): 
	sum = 0
	for i in range(1, n+1): 
		sum +=i*i*i 
		
	return sum


print('Enter last number of series :')
number = int(input())
print(sumOfSeries(number)) 

 
