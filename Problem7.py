#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

def problemSeven():
	primes = []
	primes.append(2)
	num = 3 
	while True:
		val = True
		for i in primes:
			if num%i == 0:
				val = False
				break
		if val == True:
			primes.append(num)
		num += 1
		#if len(primes) == 5000:
			#print len(primes)
		if len(primes) == 10001:
			break
	print primes[10000]
problemSeven()