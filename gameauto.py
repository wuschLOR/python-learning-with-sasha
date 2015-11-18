import random

pcnumber = random.randint(0,10)
print(pcnumber)

up = 10
lo = 0

iattemt = range(3)

for i in iattemt:
  print('Attempt' , i)
  mid = round((up + lo)/2)
  print('your number is: ' , mid)
  print('up ' , up)
  print('low ', lo )
  humannumber = mid
  if pcnumber == humannumber:
	  print('you won!')
	  break
  elif pcnumber > humannumber:
	  print('too low')
	  lo = mid+1
  else:
	  print('too high')
	  up = mid-1

if pcnumber != humannumber:
	print('game over man GAME OVER')