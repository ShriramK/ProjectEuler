'''Problem 9
25 January 2002

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
 (a+b)^2 = (1000-c)^2  , 2ab+2000c = 1000000
 k^2 -> 500^2 , i = j = p , 2*p^2  = k^2 , p = ~ k* 2/3
 range end values for i,j,k could be optimized further
'''

# import sys

def problem_nine():
	for i in range(1, 400):
		for j in range(i + 1, 400):
			for k in range(j + 1, 500):
				if i * j + 1000 * k == 500000 and \
					pow(i, 2) + pow(j, 2) == pow(k, 2):
					print i, j, k
					print i * j * k
					#sys.exit(1)
problem_nine()
# 200, 375, 425
# 31875000
