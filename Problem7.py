'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?

Todo:
Find a way to optimize it further or a different approach to solve it in
milliseconds.
'''
def is_prime(num, primes):
	for each in primes[1:]:
		if num % each == 0:
			return False
	return True

def problem_seven():
	primes = []
	primes.append(2)
	num = 3
	while True:
		if is_prime(num, primes):
			primes.append(num)
		num += 2
		#if len(primes) == 5000:
			#print len(primes)
		if len(primes) == 10001:
			break
	print primes[10000]

problem_seven()
# 104743
