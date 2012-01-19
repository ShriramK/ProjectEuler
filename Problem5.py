#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any #remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20

#maintain array for 2s, 3s, 5s, and other numbers
#maintain global array prefilled with -1

def problemFive():
	lcm = 2520
	lcmLi = countDivisors(lcm)
	lcmDict = convertListToDict(lcmLi)
	
	for i in range(11,21):
		li = countDivisors(i)
		liDict = convertListToDict(li)
		for item in liDict:
			if item in lcmDict:
				lcmDict[item] = max(liDict[item], lcmDict[item])
			else:
				lcmDict[item] = liDict[item]
	ans = 1
	for item in lcmDict:
		ans *= pow(item, lcmDict[item])
	print ans
	
def convertListToDict(listOfIntegers):
	newDict = {}
	for i in listOfIntegers:
		if i not in newDict:
			newDict[i] = 1
		else:
			newDict[i] += 1
	return newDict

def countDivisors(num):
	primes = []
	div = 2
	while num != 1:
		while num % div == 0:
			primes.append(div)
			num = num/div
		if div == 2:
			div = 3
		else:
			div += 2 #only account for odd numbers
	return primes
problemFive()
#232792560