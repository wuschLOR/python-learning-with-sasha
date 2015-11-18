import random

pcnumber = random.randint(0,10)
print(pcnumber)

iattemt = range(3)

for i in iattemt:
  print('Attempt' , i)
  humannumber = int(input('?'))
  
  if pcnumber == humannumber:
	  print('you won!')
	  break
  elif pcnumber > humannumber:
	  print('too low')
  else:
	  print('too high')
	  

if pcnumber != humannumber:
	print('game over man GAME OVER')