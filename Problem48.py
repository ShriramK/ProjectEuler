'''Problem 48
18 July 2003
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
'''

def problem_fortyeight():
	sum_of_nums = sum(pow(i, i) for i in range(1, 1001))
	sum_str = str(sum_of_nums)
	print sum_str[len(sum_str)-10:]

problem_fortyeight()
# 9110846700
