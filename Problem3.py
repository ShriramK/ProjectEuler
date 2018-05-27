'''The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
not more that sqrt or **.5 of 6000851475143
'''

def compute_prime_factors():
	num = 600851475143
	div = 2
	while num != 1:
		while num % div == 0:
			yield div
			num = num / div
		div = 3 if div == 2 else div+2 # only account for odd numbers

for each in compute_prime_factors():
	pass
print each
# 6857
