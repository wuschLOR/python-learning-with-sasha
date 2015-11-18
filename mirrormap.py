import pygame
pygame.init()


maze=[]
for iRow in range(20):
	maze.append([])
	for iColum in range(20):
		maze[iRow].append('wall')
		
	

maze[2][2] = 'path'
#print(maze)

		

windowsurface=pygame.display.set_mode((400,400),0,32)
pygame.display.set_caption('Mirrowmaze level editor')

#pygame.drawrect()

GameOver=False
while not GameOver:

	for iRow in range(20):
		for iColum in range(20):
			celdim = (iColum*20, iRow*20, 20, 20)
			if maze[iColum][iRow] == 'wall':
			    pygame.draw.rect(windowsurface, pygame.Color('orange'), celdim)
			else:
				pygame.draw.rect(windowsurface, pygame.Color('grey'), celdim)
				
			
	pygame.display.update()
		
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			GameOver=True

pygame.quit()
