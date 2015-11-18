# create dictionary
settings = {}
settings['tile'] = {'water' : '~',
                    'ship' : '~',
                    'miss' : '.',
                    'hit' : 'X'}
settings['grid'] = {'rownumber':9, 
                    'colnumber':9}

def draw_grid(two_d_array):
    # draw the grid
    numberRow = ord('A')
    numberCol = 1

    # print out the numbers aboth the colums
    print (' ', ' ', end='')
    for col in grid[0]:
        print (numberCol, ' ', end='')
        numberCol = numberCol + 1
        
    print()

    # print every row with the coresponding letter in front 
    for row in grid:
        print (chr(numberRow), ' ', end='')
        numberRow = numberRow + 1
        
        for cell in row:
            print (settings['tile'][cell], ' ', end='')
            
        print()   
        
        
def crater_allready_there(two_d_array, tile_index):
    # check if the tile was allready victem of the angry HUMAN
    if (two_d_array[tile_index[0]][tile_index[1]] == 'miss' or
        two_d_array[tile_index[0]][tile_index[1]] == 'hit'):
        allready_fired = True
    else:
        allready_fired = False
        
    return(allready_fired)
    
    
def change_grid(two_d_array, tile_index):
    # change one tile to a new value
    #print(tile_index)
    #print(two_d_array[tile_index[0]][tile_index[1]])

    if two_d_array[tile_index[0]][tile_index[1]] == 'water':
        two_d_array[tile_index[0]][tile_index[1]] = 'miss'
    
    if two_d_array[tile_index[0]][tile_index[1]] == 'ship':
        two_d_array[tile_index[0]][tile_index[1]] = 'hit'

    return(two_d_array)


def get_valid_input(two_d_array):
    valid =  False
    itile = [0, 0]
    while not valid:
        human_cell = input('Shoot at me HUMAN!')
        
        if len(human_cell) == 2:
            itile[0] = ord(human_cell[0])-ord('A')
            itile[1] = ord(human_cell[1])-ord('1')
            if (itile[0] < settings['grid']['rownumber'] and 
                itile[1] < settings['grid']['rownumber'] and 
                itile[0] >= 0 and 
                itile[1] >= 0 and
                (not crater_allready_there(two_d_array, itile))
                ):
                valid = True
            
    return(itile)


def did_the_human_win():
    return(False)


## create grid 
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

turn=1
while did_the_human_win: 
    print(turn)
    turn = turn+1
    
    draw_grid(grid)
        
    human_cell_index = get_valid_input(grid)

    grid = change_grid(grid, human_cell_index)


if did_the_human_win:
    print('THE WINNER IS YOU')
else:
    print('ALL YOUR BASE BELONG TO US')



            