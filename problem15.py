#Problem 15
#19 April 2002

#Starting in the top left corner of a 2×2 grid, there are 6 routes (without backtracking) to the #bottom right corner.

#How many routes are there through a 20×20 grid?

#http://grom.zeminvaders.net/blog/project-euler-problem-15#comment-1635

def problemFifteen():
	"""	
	ans = 1
	for i in xrange(21,41):
		ans *= i
	for i in xrange(1, 21):
		ans /= i
	print ans
	"""
#http://projecteuler.net/thread=15 - solution by roxtar
l=[]
for i in range(21):
       l.append([])
       for j in range(21):
              l[i].append(0)
              
for i in range(21):
       l[20][i]=1
       l[i][20]=1
       
for i in range(19,-1,-1):
       for j in range(19,-1,-1):
              l[i][j]=l[i+1][j]+l[i][j+1]
              
print l[0][0]
problemFifteen()

#137846528820

