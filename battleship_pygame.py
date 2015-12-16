import random
import pygame

pygame.init()

# create dictionary
settings = {}
settings['title'] = 'Battleship'
settings['tile'] = {'water' : pygame.Color('blue'),
                    'ship'  : pygame.Color('grey'),
                    'miss'  : pygame.Color('black'),
                    'hit'   : pygame.Color('red')}
settings['tile_print'] = {'water' : pygame.Color('blue'),
                          'ship'  : pygame.Color('blue'),
                          'miss'  : pygame.Color('black'),
                          'hit'   : pygame.Color('red')}
settings['grid'] = {'rownumber':5, 
                    'colnumber':5,
                    'allsize':80}

settings['frame'] = {'linewidth' : 2,
                     'color' : pygame.Color('white')
                     }

random.seed(5)

def draw_grid(battlefield):
    # draw the battlefield
    
    irow = -1
    for row in battlefield:
        irow = irow + 1
        icol = -1
        for cell in row:
            icol = icol + 1
            # doing the celldimentions (L left, R top , W width, H height)
            celdim = (irow * settings['grid']['allsize'],
                      icol * settings['grid']['allsize'], 
                      settings['grid']['allsize'],  
                      settings['grid']['allsize'])
            
            # drawing on the screen
            pygame.draw.rect(windowsurface, settings['tile_print'][cell], celdim)
            pygame.draw.rect(windowsurface, settings['frame']['color'], celdim , settings['frame']['linewidth'])
            print irow, icol, celdim , cell

       
def crater_allready_there(battlefield, tile_index):
    # check if the tile was allready victem of the angry HUMAN
    if (battlefield[tile_index[0]][tile_index[1]] == 'miss' or
        battlefield[tile_index[0]][tile_index[1]] == 'hit'):
        allready_fired = True
    else:
        allready_fired = False
        
    return(allready_fired)


def tile_allready_occupied(battlefield, tile_index, conditon_array):
    # check for 
    if battlefield[tile_index[0]][tile_index[1]] in conditon_array:
        allready_occupied = True
    else:
        allready_occupied = False
        
    return(allready_occupied)
    
    
def change_grid_after_shooting(battlefield, tile_index):
    # change one tile to a new value
    #print tile_index
    #print battlefield[tile_index[0]][tile_index[1]]

    if battlefield[tile_index[0]][tile_index[1]] == 'water':
        battlefield[tile_index[0]][tile_index[1]] = 'miss'
    
    if battlefield[tile_index[0]][tile_index[1]] == 'ship':
        battlefield[tile_index[0]][tile_index[1]] = 'hit'

    return(battlefield)


def place_ship(battlefield, ship_size):
    
    # per dafault the position isn't valid 
    position_is_valid = False
    
    # as long the position is not valid loop
    while not position_is_valid:
        # make ortiantaion decission
        ship_oriantations = ['vertical', 'horizontal']
        random_orientation = random.sample(ship_oriantations, 1)
        
        # calculate valid tiles
        if random_orientation == 'vertical':
            row_limit = settings['grid']['rownumber'] - ship_size     # change!!
            col_limit = settings['grid']['rownumber'] - 1             # change!!
        else:
            row_limit = settings['grid']['rownumber'] - 1             # change!!
            col_limit = settings['grid']['rownumber'] - ship_size     # change!!
            
        # chose staringpoint
        ship_row = random.randint(0, row_limit)
        ship_col = random.randint(0, col_limit)
        
        #print 'ship_row',ship_row
        #print 'ship_col',ship_col
        
        #check for occupation
        occupation = []
        for tiles in (range(ship_size)):
            #occupation.append(tile_allready_occupied(battlefield, [ship_row,ship_col], 'ship'))
            #print occupation
            occupation=False
            
        if occupation == False:
            position_is_valid = True
            
    # lay out the ship
    for iship in range(ship_size):
        
        battlefield[ship_row][ship_col] = 'ship'
        
        # move the row or the col based on the orientation
        if random_orientation == 'vertical':
            ship_row =  ship_row + 1
        else:
            ship_col =  ship_col + 1
        
        
    return(battlefield)


def human_is_victorious(battlefield):
    ships_left = False
    for row in battlefield:
        if 'ship' in row:
            ships_left =  ships_left + 1

    return(ships_left == False)


################################################################################

## create grid 
# row first
# then cols

grid = []
for iRow in range(settings['grid']['rownumber']):
    #print iRow
    grid.append([])
    for iCol in range(settings['grid']['colnumber']):
        #print iCol
        grid[iRow].append('water')
        

# debug
#print grid
#grid[1][1] = 'ship'
#grid[1][2] = 'hit'
##grid[2][1] = 'water'
#grid[2][2] = 'miss'
#print grid
# /debung


# create ships
grid = place_ship(grid,  2)
grid = place_ship(grid,  3)
grid = place_ship(grid,  2)

windowsurface = pygame.display.set_mode(
    (settings['grid']['colnumber']*settings['grid']['allsize'],
                  settings['grid']['rownumber']*settings['grid']['allsize']),
    0,
    32)
pygame.display.set_caption(settings['title'])



turn=1
while not human_is_victorious(grid): 


    
    print '#########################'
    print 'TURN:',turn
    print '#########################'
    print ''
    
    turn = turn + 1
    
    draw_grid(grid)
    
    pygame.display.update() # flip
    
    for event in pygame.event.get():
        # exit condition when Alt F4
        if event.type == pygame.QUIT:
            GameOver=True
            
        # mouse pressed condition    
        if pygame.mouse.get_pressed()[0] == 1:
            mouse_pos = pygame.mouse.get_pos()
            print "pressed" , mouse_pos
            
            human_cell_index = [0 , 1]
            human_cell_index[0] = mouse_pos[0] / settings['grid']['allsize']
            human_cell_index[1] = mouse_pos[1] / settings['grid']['allsize']
            print "pressed" , human_cell_index
            
            grid = change_grid_after_shooting(grid, human_cell_index)
            

if human_is_victorious(grid):
    print 'THE WINNER IS YOU'
else:
    print 'ALL YOUR BASE BELONG TO US'

            