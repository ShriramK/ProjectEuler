#Problem 15
#19 April 2002

#Starting in the top left corner of a 2×2 grid, there are 6 routes (without backtracking) to the #bottom right corner.

#How many routes are there through a 20×20 grid?

#http://grom.zeminvaders.net/blog/project-euler-problem-15#comment-1635

def problemFifteen():
	ans = 1
	for i in xrange(21,41):
		ans *= i
	for i in xrange(1, 21):
		ans /= i
	print ans

problemFifteen()
#137846528820