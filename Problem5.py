'''
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any #remainder.
What is the smallest positive number that is evenly divisible by all of
the numbers from 1 to 20?

1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20

maintain array for 2s, 3s, 5s, and other numbers
maintain global array prefilled with -1
'''

def problem_five():
	lcm = 2520
	lcm_li = count_divisors(lcm)
	lcm_dict = convert_list_to_dict(lcm_li)
	
	for i in range(11, 21):
		li = count_divisors(i)
		li_dict = convert_list_to_dict(li)
		for item in li_dict:
			if item in lcm_dict:
				lcm_dict[item] = max(li_dict[item], lcm_dict[item])
			else:
				lcm_dict[item] = li_dict[item]
	ans = 1
	for item in lcm_dict:
		ans *= pow(item, lcm_dict[item])
	print ans
	
def convert_list_to_dict(list_of_integers):
	new_dict = {}
	for i in list_of_integers:
		if i not in new_dict:
			new_dict[i] = 1
		else:
			new_dict[i] += 1
	return new_dict

def count_divisors(num):
	primes = []
	div = 2
	while num != 1:
		while num % div == 0:
			primes.append(div)
			num = num/div
		if div == 2:
			div = 3
		else:
			div += 2 # only account for odd numbers
	return primes

problem_five()
#232792560
