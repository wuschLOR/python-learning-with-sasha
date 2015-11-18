import pygame
pygame.init()

settings={}
settings['Title'] = 'Mirrowmaze level editor'
settings['Maze']={'Rownumber':4, 
				  'Colnumber':4,
				  'Cellwidth':20,
				  'Cellheigth':25}
settings['wall']={'color':pygame.Color('orange')}
settings['path']={'color':pygame.Color('grey')}
settings['cursor']={'color': pygame.Color('red'),
					'linewidth':[]} 

cursor={}
cursor['iCol'] = 0
cursor['iRow'] = 0

L = cursor['iCol']*settings['Maze']['Cellwidth']
T = cursor['iRow']*settings['Maze']['Cellheigth']
W = settings['Maze']['Cellwidth']
H = settings['Maze']['Cellheigth']
cursor_rect = (L,T,W,H)
print(cursor_rect)

# create the maze grid #########################################################
maze=[]
for iRow in range(settings['Maze']['Rownumber']):
	maze.append([])
	for iColum in range(settings['Maze']['Colnumber']):
		maze[iRow].append('wall')
		
	

maze[2][2] = 'path'
print(maze)


windowsurface = pygame.display.set_mode((settings['Maze']['Colnumber']*settings['Maze']['Cellwidth'],settings['Maze']['Rownumber']*settings['Maze']['Cellheigth']),0,32)
pygame.display.set_caption(settings['Title'])

#pygame.drawrect()

GameOver=False
# repeat until gameover is triggered
while not GameOver:
    
    # drawing the grid with colors
	for iRow in range(settings['Maze']['Rownumber']): #for every row
		for iColum in range(settings['Maze']['Colnumber']): # for every colum
            # doing the celldimentions (L left, R top , W width, H height)
			celdim = (iColum*settings['Maze']['Cellwidth'], iRow*settings['Maze']['Cellheigth'], settings['Maze']['Cellwidth'], settings['Maze']['Cellheigth'])
			# drawing on the screen
			pygame.draw.rect(windowsurface, settings[maze[iColum][iRow]]['color'], celdim)

	pygame.display.update() # flip
    
    # exit condition when Alt F4
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			GameOver=True



pygame.quit()
