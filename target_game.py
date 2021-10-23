from typing import List
import string
import random
import operator

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    alphabet = list(string.ascii_uppercase.strip(' '))
    list_of_letters = []
    mini_list = []
    playground = []
    n = 0
    while n != 3:
        for i in range(3):
            letter = random.choice(alphabet)
            list_of_letters.append(letter.lower())
            mini_list.append(letter)
        playground.append(mini_list)
        mini_list = []
        n += 1
    print(playground)
    return list_of_letters

#generate_grid()


def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    main_letter = letters[4]
    grid_tpl_lst = []
    letters = sorted(letters)
    letters_copy = letters.copy()
    while letters != []:
        for n in letters:
            number_of_letter = letters.count(n)
            tpl_letter = (n, number_of_letter)
            index_letter = letters.index(n)
            del letters[index_letter:index_letter+number_of_letter]
            grid_tpl_lst.append(tpl_letter)
    grid_tpl_lst = sorted(grid_tpl_lst, key=operator.itemgetter(0))

    possible_words = []
    with open(f, 'r') as file:
        for i in file:
            line = file.readline()
            if '\n' in line:
                line = line.replace('\n', '')
            count = 0
            if len(line) < 4:
                count += 1
            for n in line:
                if n not in letters_copy:
                    count += 1
            if main_letter not in line:
                count += 1
            if count == 0:
                possible_words.append(line)
        print(possible_words)

        possible_words_list = possible_words.copy()
        for word in possible_words:
            letters_in_line_tpl = []
            lst_line = list(word)
            lst_line = sorted(lst_line)
            lst_line_copy = lst_line.copy()
            while lst_line != []:
                for n in lst_line:
                    if n in lst_line:
                        number_of_letter = lst_line.count(n)
                        tpl_line = (n, number_of_letter)
                        index_letter = lst_line.index(n)
                        del lst_line[index_letter:index_letter+number_of_letter]
                        letters_in_line_tpl.append(tpl_line)
                        lst_line = sorted(lst_line)
            for r in letters_copy:
                if r not in lst_line_copy:
                    letters_in_line_tpl.append((r, 0))
            letters_in_line_tpl = sorted(letters_in_line_tpl, key=operator.itemgetter(0))        
            t = 0
            while t != len(letters_in_line_tpl)-2:
                if letters_in_line_tpl[t] == letters_in_line_tpl[t+1]:
                    del letters_in_line_tpl[t]
                t += 1
                if t == len(letters_in_line_tpl)-2:
                    break
            for h in range(len(grid_tpl_lst)):
                if grid_tpl_lst[h][1] < letters_in_line_tpl[h][1]:
                    possible_words_list.remove(word)
    
    print(possible_words_list)
    


get_words('en.txt', generate_grid())

def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    pass


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass


def results():
    pass
