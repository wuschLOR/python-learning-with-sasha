up = 10
lo = 0


iattemt = range(3)

for i in iattemt:
	mid = round((up + lo)/2)
	print('your number is: ' , mid)

	humanevaluation = input('input =, < , >')

	if humanevaluation == '=':
		print('I won')
	if humanevaluation == '<':
		up = mid-1
	if humanevaluation == '>':
		lo = mid+1

	print('up ' , up)
	print('low ', lo )