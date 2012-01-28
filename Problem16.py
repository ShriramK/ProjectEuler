#Problem 16
#03 May 2002

#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

#What is the sum of the digits of the number 2^1000?
#concept of Arbitrary precision arithmetic
def problemSixteen():
	num = 1
	for i in range(0,1000):
		num*=2
	sum = 0
	for digit in str(num):
		sum += int(digit)
	print sum

problemSixteen()
#1366 
