
# choose the word
word  = 'cat'

print(word)

# create the wordmask
wordmask = []
for iletter in range(len(word)):
    wordmask.append('*')
    print(wordmask)



print('my word is')
print(word)
print(wordmask)
## ask for human input + evaluate if it's just one letter 
#adequat_length = False
#while not adequat_length:
    #user_letter = raw_input('Give me a letter puny human!!!')
    #print(user_letter)
    #if len(user_letter) == 1:
        #adequat_length = True


## evaluate 
#for iletter in range(len(word)):
    #if word[iletter] == user_letter:
        #print('letter is right')


## change the wordmask

#for iletter in range(len(word)):
    #if word[iletter] == user_letter:
       #print('I would changen shit but indexing doesnt works .... OMG !!!!')
    