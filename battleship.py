import random

# create dictionary
settings = {}
settings['tile'] = {'water' : '~',
                    'ship' : '~',
                    'miss' : '.',
                    'hit' : 'X'}
settings['grid'] = {'rownumber':9, 
                    'colnumber':9}

random.seed(5)

def draw_grid(battlefield):
    # draw the battlefield
    numberRow = ord('A')
    numberCol = 1

    # print out the numbers aboth the colums
    print (' ', ' ', end='')
    for col in battlefield[0]:
        print (numberCol, ' ', end='')
        numberCol = numberCol + 1
        
    print()

    # print every row with the coresponding letter in front 
    for row in battlefield:
        print (chr(numberRow), ' ', end='')
        numberRow = numberRow + 1
        
        for cell in row:
            print (settings['tile'][cell], ' ', end='')
            
        print()   
        
        
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
    #print(tile_index)
    #print(battlefield[tile_index[0]][tile_index[1]])

    if battlefield[tile_index[0]][tile_index[1]] == 'water':
        battlefield[tile_index[0]][tile_index[1]] = 'miss'
    
    if battlefield[tile_index[0]][tile_index[1]] == 'ship':
        battlefield[tile_index[0]][tile_index[1]] = 'hit'

    return(battlefield)


def get_valid_input(battlefield):
    answer_is_valid =  False
    itile = [0, 0]
    while not answer_is_valid:
        human_cell = input('Shoot at me HUMAN! ')
        print('')
        
        if len(human_cell) == 2:
            itile[0] = ord(human_cell[0])-ord('A')
            itile[1] = ord(human_cell[1])-ord('1')
            if (itile[0] < settings['grid']['rownumber'] and # change!!
                itile[1] < settings['grid']['rownumber'] and # change!!
                itile[0] >= 0 and 
                itile[1] >= 0 and
                (not crater_allready_there(battlefield, itile))
                ):
                answer_is_valid = True
            
    return(itile)


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
        
        print('ship_row',ship_row)
        print('ship_col',ship_col)
        
        #check for occupation
        occupation = []
        for tiles in (range(ship_size)):
            #occupation.append(tile_allready_occupied(battlefield, [ship_row,ship_col], 'ship'))
            #print(occupation)
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
    #print(iRow)
    grid.append([])
    for iCol in range(settings['grid']['colnumber']):
        #print(iCol)
        grid[iRow].append('water')
        

# debug
#print(grid)
#grid[1][1] = 'ship'
#grid[1][2] = 'hit'
##grid[2][1] = 'water'
#grid[2][2] = 'miss'
#print(grid)
# /debung


# create ships
grid = place_ship(grid ,  2)

turn=1
while not human_is_victorious(grid): 
    
    print('#########################')
    print('TURN:',turn)
    print('#########################')
    print('')
    
    turn = turn+1
    
    draw_grid(grid)
        
    human_cell_index = get_valid_input(grid)

    grid = change_grid_after_shooting(grid, human_cell_index)


if human_is_victorious(grid):
    print('THE WINNER IS YOU')
else:
    print('ALL YOUR BASE BELONG TO US')



            