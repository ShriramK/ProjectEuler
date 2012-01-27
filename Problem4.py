#A palindromic number reads the same both ways. The largest palindrome made from the product of two #2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

def problemFour():
	max = 0
	for i in range(100, 1000):
		for j in range(100, 1000):
			stri = str(i*j)
			if stri == stri[::-1]:
				if int(stri) > max:
					max = int(stri)
	print max
			
problemFour()
#906609
#sys:1: DeprecationWarning: Non-ASCII character '\xd7' in file Problem4.py on line 1, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details
#http://docs.python.org/howto/unicode.html