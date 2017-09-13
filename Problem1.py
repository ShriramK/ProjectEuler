'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.ind the sum of all
the multiples of 3 or 5 below 1000.
'''

def compute_sum_of_multiples_below_thousand():
	print sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1, 1000)))

compute_sum_of_multiples_below_thousand()
# 233168
