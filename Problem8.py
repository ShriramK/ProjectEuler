#Find the greatest product of five consecutive digits in the 1000-digit number.
def problemEight():
		
	num = str( 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)
	
	#num = str(123456789106789123456023456078912034567);
	print 'num ', num, ' len ', len(num)	
	start = 0
	end = 4
	substr = num[start:end+1]
	max = 0
	sum = 0
	while end < len(num):
		if '0' not in substr:
			sum = findSum(substr)
			if sum > max:
				max = sum
				ans = substr
			start += 1
			end += 1
			substr = num[start:end+1]
		else:
			start += substr.find('0')+1	
			end = start + 5 - 1
			substr = num[start:end+1]
		print ' max ans  sum ', max, ans , sum,
	"""
	sum = 0
	max = 0
	pos = 0#5
	substr = ""#num[:5]
	con = True
	while pos+5 <= len(num):
		print 'substr ', substr, 'sum', sum
		if num[pos] != '0' and'0' not in num[pos:pos+5]:
			if con == True:
				print 'con == True'
				# string not picked condition
				substr = num[pos:pos+5]
				sum = findSum(substr)
				pos = pos + 5 - 1
				con = False
			else:
				#take last four and add next character
				print 'num[pos] ', num[pos], ' substr[-1] ', substr[-1]
				print 'SUBSTR ', substr
				substr = substr[1:] + num[pos]			#substr[1:len(substr)]
				print 'SUBSTR ', substr
				sum += int(num[pos]) - int(num[pos-5])
				#pos = pos + 1 -> no need as pos is already at next character
			#print substr[1:len(substr)], num[pos], pos
			if sum > max:
				max = sum
				ans = substr
		else:
			pos += 1 
			while pos+5 <= len(num): #find the first five with no zeroes
				substr = num[pos:pos+5]
				if '0' in substr:
					pos += substr.find('0')+1	
				else:
					sum = findSum(substr)
					if sum > max:
						max = sum
						ans = substr
					break
		print ' END substr ', substr, 'pos ', pos
		pos += 1

	print 'ans ', ans
	product = 1
	for digit in ans:
		product *= int(digit)
	print product
	"""
def findSum(str):
	sum = 0
	for i in str:
		sum += int(i)
	return sum
"""
	for i in range(0, len(num)):
		substr = num[i:i+5]
		if '0' not in substr:
			
			
	for j in range(len(num)-5):
		for index in range(5):
			product *= product * int(num[index+4]) / int(num[0+index-1])
			if max < product:
				max = product
	print max
"""
problemEight()