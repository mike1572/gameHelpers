

''' This function converts a file into a list of english words; basically a dictionary'''
def dictionary(filename):
    # The first list receives all items from the file.
    list_of_words = []
    fobj = open(filename, 'r', encoding='utf-8')
    for i in fobj:
        i = i.lower()
        list_of_words.append(i)
        
    # The second list deletes the \n and is returned by the function.
    list_words = []
    for line in list_of_words:
        line = line.replace('\n', '')
        list_words.append(line)
    
    fobj.close()
    
    return list_words

''' This function defines the length of the word we are looking for'''
def word_length():
    length_of_word = int(input('How many letters does the word contain? '))
    return length_of_word

''' This function filters the list of words based on the length we are looking for'''
def length_seeked(list, number):
    list_of_words_with_same_length= []
    for i in range(len(list)):
        if len(list[i]) == number:
            list_of_words_with_same_length.append(list[i])
            
    return list_of_words_with_same_length
            
'''This function filters the list returned from the previous function based on letter rank'''
def filter_list(list, num):
    list_possible_words = []
    words_to_remove = []
    keys = []
    values = []
    for j in range(num):
        letter = input('What is the letter at rank {} ? '.format(j + 1) + '\nPress ENTER if you do NOT know: ')
        if len(letter) == 1 and  letter.isalpha() == True:
            letter= letter.lower()
            values.append(letter)
            keys.append(j)
            for i in range(len(list)):
                if letter == list[i][j] and list[i] not in list_possible_words:
                    list_possible_words.append(list[i])

    for i in range(len(list_possible_words)):
        for j in range(len(keys)):
            if list_possible_words[i][keys[j]] != values[j]:
                words_to_remove.append(list_possible_words[i])
    
    list_words = [x for x in list_possible_words if x not in words_to_remove]             
                   
    return list_words

dict = dictionary('english.txt')
list = ['blue', 'tabby', 'table', 'saube', 'saucy', 'saudi', 'sauna']
print('Welcome to the CrossWord Helper')
input('Press ENTER to continue ')
length = word_length()
solution = filter_list(length_seeked(dict, length), length)
print('Here is a list of possible words: ', solution)




