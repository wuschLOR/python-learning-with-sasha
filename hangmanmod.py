import copy

def solved(current_mask):
    counter = 0
    for icount in range(len(current_mask)):
        if current_mask[icount]=='*':
            counter = counter + 1
    
    return(counter==0)


# choose the word
wordstring  = 'cat'

print(wordstring)

# transform the wordstring to a character list
word = []
for iletter in (wordstring):
    word.append(iletter)


# create the wordmask
wordmask = copy.copy(word)
for iletter in range(len(wordmask)):
    wordmask[iletter] = '*'

#print(wordstring)
print(word)
print(wordmask)

attempts_left = 5
allready_chocion_letters=[] # list for userletters

while not solved(wordmask) & attempts_left > 0 :

    valid_attempt = False

    # tell the human the wordmask
    print('my word is:')
    for iprint in wordmask:
        print(iprint, end='')
        
    print()
        
        
    # ask for human input + evaluate
    adequat_length = False #
    while not adequat_length:
        user_letter = input('Give me a letter puny human!!! ')
        if len(user_letter) == 1:
            print('you gave me this letter: #', user_letter, '#')
            adequat_length = True
        else:
            print('#', user_letter, '#  is not one letter ... dude seriously ??? ')
            
            
    # change the wordmask
    for iletter in range(len(word)):
        if word[iletter] == user_letter:
            wordmask[iletter] = word[iletter]
            valid_attempt = True
            

    # remember the user_letter so that the stupid human tries the same letter a second time
    allready_chocion_letters.append(user_letter)
    
    
    # check if the attempt is valid
    if not valid_attempt:
        attempts_left = attempts_left -1
        
    print('attempts left', attempts_left)
    
    
if solved(wordmask):
    print('THE WINNER IS YOU')
else:
    print('GAME OVER')
    
    