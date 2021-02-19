import json
from os import system, name
from time import sleep


def show_dict(dict_values):
    '''
    Funcion that returns the KEYS and VALUES of the dict formed by the json file
    '''

    print('-'*70, "\n CHAVES    |               VALORES ASSOCIADOS \n", '-'*70, '\n')
    for key, values in dict_values.items():
        print(f"<> {key.upper()} -> ", end='')
        for value in values:
            if value is not values[-1]:
                print(f"'{value}' -", end=' ')
            else:
                print(f"{value}")
        print('\n\n')


def read_json():
    '''
    Function that returns the json file
    '''
    with open('data.json', 'r', encoding='utf8') as file:
        return json.load(file)


def write_json(dict_dados):
    '''
    Function that sends local updates to the data.json file
    '''

    with open('data.json', 'w', encoding='utf8') as file:
        json.dump(dict_dados, file)


def clear(): 
    '''
    Function to clear the cmd / command prompt screen
    '''
    if name == 'nt': 
        system('cls') 

def keys_dict(dict):
    '''
    Function that return the KEYS of data.json
    '''
    
    keys_all = [] 
    for k in dict.keys():
        keys_all.append(k)
    return keys_all


# WRITE ANONYMOUS '__ __'
def anon(word):
    global palavra, letter_word, ocult

    palavra = word.upper()

    letter_word = [] # PEGARÁ CADA LETRA

    for let in range(len(word)):
        letter_word.append(palavra[let])

    ocult = []
    for cont in range(len(palavra)):
        
        # IF SPACE EMPTY
        if letter_word[cont] == ' ':
            ocult.append(' ')
        
        else:
            ocult.append('__')
    
    return ocult


def condition(l, w, a):
    '''
    Return if player WON or LOST
    '''
    w = w.upper()
    letra = ''
    for cont in range(len(w)):
        if w[cont] != ' ':
            letra += w[cont]

    # IF LETTER == COMPLETE WORD
    if l == w.upper():
        return False

    elif len(letra) == len(a):
        return False

    else:
        return True



def visual_game(cont, theme, life, ocult, wordused):

    '''
    Funciont that returns the visual game
    '''
    clear()
    print("\n\033[1;93m ------------------   HANGMAN   ------------------\033[0;00m\n", f'\n<()> THEME DE ROUND: \033[1;92m{theme.upper()}\033[0;00m')
    print(f'\n\033[1;31mLIFES = {life}\033[0;00m')
    print(f"{cont} ROUND --> ", "  ".join(ocult))
    print(f"{len(ocult)} LETTERS!")

    print(f'<<>> LETTERS USED: ', end='')

    for cont_w in range(len(wordused)):
        print(f'{wordused[cont_w]}  ', end='')
    print('\n', '-'*70)

            


def gameplay(word, theme):

    '''
    Gameplay the game!
    '''

    cont = 1
    life = 5
    words = letter = words_used = ''

    while life != 0:

        visual_game(cont, theme, life, ocult, words_used)
        
        # CONDITIONS TO WON
        if not condition(letter, word, words):
            print(f'\n\n<> AFTER {cont} ATTEMPTS, YOU FOUND OUT!')
            break

        letter = input(f"\n\n\> Type one letter: ").upper()

        # WHILE LETTER IS EMPTY:
        while letter == ' ':
            letter = input("\> Type one letter: ").upper()
        
        # IF LETTER ALREADY ADD IN LIST:
        if letter in ocult:
            visual_game(cont, theme, life, ocult, words_used)
            print(f'\033[1;91m"{letter}" ALREADY ADD!\033[0;00m')
            cont -= 1
            continue

        words_used += letter

        # IF THE LETTER IS FOUND 
        if letter in letter_word:
             
            visual_game(cont, theme, life, ocult, words_used)

            print(f'\033[1;92m \n{letter} FOUND\033[0;00m-> ', end='')
            
            contador = letter_word.count(letter)
                
            # ONLY ONE LETTER
            if contador == 1:
                position = letter_word.index(letter)
                ocult[position] = letter
                sleep(0.3)
                words += letter
                
            # MANY LETTER 
            else:
                for cont_letter in range(contador):
                    position = letter_word.index(letter)
                    ocult[position] = letter
                    letter_word[position] = letter.lower()
                    sleep(0.3)
                    words += letter
                        
        # IF LETTER NOT IN WORD
        else:
            if not condition(letter, word, words):
                print(f'\n\n<> AFTER {cont} ATTEMPTS, YOU FOUND OUT!')
                break
            life -= 1
            visual_game(cont, theme, life, ocult, words_used)
            print(f'\nLetter "{letter}" NOT FOUND! \n-1 LIFE')

            sleep(0.7)
        
        # CONT ROUNDS
        cont += 1

        
        

    # SYSTEM RETURN (WON / LOST)
    sleep(2.0)
    # IF LOST:
    if life == 0:
        clear()
        print("\n\033[1;93m ------------------   HANGMAN   ------------------\033[0;00m\n")
        print(f'\n<()> THEME DE ROUND: \033[1;92m{theme.upper()}\033[0;00m')
        print(f'\n\033[1;31mLIFES = {life}\033[0;00m')
        return f'\nTHIS WORD WAS \033[1;90m{word.upper()}\033[0;00m \n<()> You \033[1;36mLOST\033[0;00m'
    
    # IF WON
    else:
        clear()
        print("\n\033[1;93m ------------------   HANGMAN   ------------------\033[0;00m\n")
        print(f'\n<()> THEME DE ROUND: \033[1;92m{theme.upper()}\033[0;00m')
        print(f'\n\033[1;31mLIFES = {life}\033[0;00m')
        return f'\nTHIS WORD WAS \033[1;90m{word.upper()}\033[0;00m \n<()> You \033[1;32mWON\033[0;00m'