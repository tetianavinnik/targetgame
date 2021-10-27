from typing import List
import string
import random
import operator
import copy


def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    alphabet = list(string.ascii_uppercase.strip(' '))
    list_of_letters = []
    mini_list = []
    playground = []
    num = 0
    while num != 3:
        for i in range(3):
            letter = random.choice(alphabet)
            list_of_letters.append(letter.lower())
            mini_list.append(letter)
        playground.append(mini_list)
        mini_list = []
        num += 1
    print(playground)
    return playground


def get_words(diction: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    if len(letters) == 3:
        list_of_letters = []
        for k in range(3):
            for i in range(3):
                list_of_letters.append(letters[k][i].lower())
        letters = list_of_letters
    main_letter = letters[4]
    grid_tpl_lst = []
    letters = sorted(letters)
    letters_copy = copy.deepcopy(letters)
    while letters != []:
        for num in letters:
            number_of_letter = letters.count(num)
            tpl_letter = (num, number_of_letter)
            index_letter = letters.index(num)
            del letters[index_letter:index_letter+number_of_letter]
            grid_tpl_lst.append(tpl_letter)
    grid_tpl_lst = sorted(grid_tpl_lst, key=operator.itemgetter(0))

    possible_words = []
    with open(diction, 'r') as file:
        file1 = file.readlines()
        for line in file1:
            line = line.lower()
            if '\n' in line:
                line = line.replace('\n', '')
            count = 0
            if len(line) < 4:
                count += 1
            for num in line:
                if num not in letters_copy:
                    count += 1
            if main_letter not in line:
                count += 1
            if count == 0:
                possible_words.append(line)

        possible_words_list = copy.deepcopy(possible_words)
        for word in possible_words:
            letters_in_line_tpl = []
            lst_line = list(word)
            lst_line = sorted(lst_line)
            lst_line_copy = copy.deepcopy(lst_line)
            while lst_line != []:
                for num in lst_line:
                    if num in lst_line:
                        number_of_letter = lst_line.count(num)
                        tpl_line = (num, number_of_letter)
                        index_letter = lst_line.index(num)
                        del lst_line[index_letter:index_letter+number_of_letter]
                        letters_in_line_tpl.append(tpl_line)
                        lst_line = sorted(lst_line)

            for rank in letters_copy:
                if rank not in lst_line_copy:
                    letters_in_line_tpl.append((rank, 0))
            letters_in_line_tpl = sorted(letters_in_line_tpl,
                                         key=operator.itemgetter(0))
            t_count = 0
            while t_count != len(letters_in_line_tpl)-2:
                if letters_in_line_tpl[t_count] == letters_in_line_tpl[t_count+1]:
                    del letters_in_line_tpl[t_count]
                t_count += 1
                if t_count == len(letters_in_line_tpl)-2:
                    break
            for h_count in range(len(grid_tpl_lst)):
                if grid_tpl_lst[h_count][1] < letters_in_line_tpl[h_count][1]:
                    if word in possible_words_list:
                        possible_words_list.remove(word)
    return possible_words_list


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    try:
        user_list = []
        m_count = 0
        while m_count != 1:
            inp_word = input()
            user_list.append(inp_word)
    except KeyboardInterrupt:
        return user_list


def get_pure_user_words(user_words: List[str], letters: List[str],
                        words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list
    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pure_lst = []
    for i in user_words:
        if i not in words_from_dict:
            pure_lst.append(i)
    for num in pure_lst:
        if len(num) < 4:
            pure_lst.remove(num)
        else:
            if letters[4] not in num:
                pure_lst.remove(num)
            else:
                for k in num:
                    if k not in letters:
                        if num in pure_lst:
                            pure_lst.remove(num)

    grid_tpl_lst = []
    letters = sorted(letters)
    letters_copy = letters.copy()
    while letters != []:
        for num in letters:
            number_of_letter = letters.count(num)
            tpl_letter = (num, number_of_letter)
            index_letter = letters.index(num)
            del letters[index_letter:index_letter+number_of_letter]
            grid_tpl_lst.append(tpl_letter)
    grid_tpl_lst = sorted(grid_tpl_lst, key=operator.itemgetter(0))

    possible_words_list = copy.deepcopy(pure_lst)
    for word in pure_lst:
        letters_in_line_tpl = []
        lst_line = list(word)
        lst_line = sorted(lst_line)
        lst_line_copy = copy.deepcopy(lst_line)
        while lst_line != []:
            for num in lst_line:
                if num in lst_line:
                    number_of_letter = lst_line.count(num)
                    tpl_line = (num, number_of_letter)
                    index_letter = lst_line.index(num)
                    del lst_line[index_letter:index_letter+number_of_letter]
                    letters_in_line_tpl.append(tpl_line)
                    lst_line = sorted(lst_line)

        for r_count in letters_copy:
            if r_count not in lst_line_copy:
                letters_in_line_tpl.append((r_count, 0))
        letters_in_line_tpl = sorted(letters_in_line_tpl,
                                     key=operator.itemgetter(0))
        t_count = 0
        while t_count != len(letters_in_line_tpl)-2:
            if letters_in_line_tpl[t_count] == letters_in_line_tpl[t_count+1]:
                del letters_in_line_tpl[t_count]
            t_count += 1
            if t_count == len(letters_in_line_tpl)-2:
                break
        for h_count in range(len(grid_tpl_lst)):
            if grid_tpl_lst[h_count][1] < letters_in_line_tpl[h_count][1]:
                if word in possible_words_list:
                    possible_words_list.remove(word)

    return possible_words_list


def results():
    """
    Return points, pure words and not used words.
    """
    letters = generate_grid()
    dictionary_words = get_words("en.txt", letters)
    user_words = get_user_words()
    not_dictionary_words = get_pure_user_words(user_words,
                                               letters, dictionary_words)
    missing_words = []
    for p_count in dictionary_words:
        if p_count not in user_words:
            missing_words.append(p_count)
    right_words = []
    for p_count in dictionary_words:
        if p_count in user_words:
            right_words.append(p_count)
    points = len(right_words)
    with open('result.txt', 'w') as output_file:
        output_file.write(str(points) + '\n')
        for i in missing_words:
            output_file.write(i + '\n')
        for num in not_dictionary_words:
            output_file.write(num + '\n')

    print(points)
    print(missing_words)
    print(not_dictionary_words)
