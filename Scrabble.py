# Scrabble Helper
import random

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

'''This function takes in the letters provided by the user and the
    list of english words.'''
def find_word(letters, dictionary):
    # All letters are converted to lowercase.
    letters = letters.lower()
    
    # This loop filters every word in the list to see if the
    # lengths are the same.
    list_possible_choices = []
    for word in dictionary:
        if len(word) == len(letters):
            # We convert to two words into lists to better
            # compare their letters.
            # We start with 0 points at the beginning.
            word_letters = list(word)
            list_letters = list(letters)
            points = 0
            # This loop filters every letter in the word (list).
            for i in word_letters:
                # This loop filters every letter of the list with
                # letters provided by the user.
                for j in list_letters:
                    # If the letter is the same, 1 point is added
                    # and we replace the letters in the respective
                    # lists with symbols; also breaking from the loop.
                    if i == j:
                        points += 1
                        word_letters[word_letters.index(i)] = '-'
                        list_letters[list_letters.index(j)] = ' '
                        break
                # If the number of points is equal to the lenght of
                # the word found in the dictionary list,
                # meaning that all the letters correspond; we return that word.
                if points == len(word):
                    list_possible_choices.append(word)
    
    if list_possible_choices == []:
        return None
    else:
        choice = random.choice(list_possible_choices)
        print('Here is a list of all possible choices:', list_possible_choices)
        return choice
    

print('Welcome to the Scrabble Helper!')
print('Input letters and the machine will find a word to use')
dict = dictionary('english.txt')
print(dict)

letters = input('What are your letters? ')
word = find_word(letters, dict)
if word == None:
    print('You cannot form any word with the letters provided.')
else:
    print('You can choose any of them.')