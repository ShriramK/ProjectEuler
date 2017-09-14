'''The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
not more that sqrt or **.5 of 6000851475143
'''

def problem_three():
	primes = []
	num = 600851475143
	temp = num
	div = 2
	while num != 1:
		while num % div == 0:
			primes.append(div)
			num = num / div
		if div == 2:
			div = 3
		else:
			div += 2 # only account for odd numbers
	print primes[len(primes) - 1]
	print primes

problem_three()
# 6857
