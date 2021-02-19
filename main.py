from functions_hangman import *
from time import sleep
from random import choice

dict_values = read_json()

def logo_forca():
    clear()
    print("\n\033[1;93m ------------------   HANGMAN   ------------------\033[0;00m\n")


while True:
    logo_forca()

    print("""OPTIONS TO 'HANGMAN':

    [ 1 ] Play
    [ 2 ] Add items
    [ 3 ] See all items
    """)
    option = int(input('<> OPTION CHOOSE: '))

    if option < 1 or option > 3: break
    
    # GAME
    elif option == 1:
        # SHOW INIT GAME:
        logo_forca()
        play_text = "\033[1;31m<> OPTION 1: Play Game\033[0;00m\n"
        print(play_text, '.'*40, '\n\n')

        print('< CHOOSE WORD... >')
        
        theme = choice(keys_dict(dict_values))
        word = choice(dict_values[theme])
        sleep(0.3)

        logo_forca()
        print(play_text, '.'*40, '\n\n')
        

        anon(word)
        
        # GAME...
        print(gameplay(word, theme))    
        sleep(6)
        logo_forca()
        
        continue


    # ADD_ITEMS
    elif option == 2:

        logo_forca()
        print("\033[1;35m<> OPTION 2: Add Items\033[0;00m")
        while True:
            
            # SHOW ALL KEYS:
            print(f"\n<>Currently, these keys are registered: ", end='')
            for k in keys_dict(dict_values):
                print(f'({k.upper()}) ----- ', end='')
            print()

            # INPUT KEY AND VALUE
            string = input("\n=> Type the KEY and VALUE <key, value>, please: ")
            
            # FIND KEY
            key = string[:string.find(',')].strip()
            
            # FIND VALUE
            value = string[string.find(',')+1:].strip()

            # IF KEY ALREADY EXISTS:
            if key in dict_values.keys():

                # VALUE NOT EXISTS:
                if value not in dict_values[key]:
                    dict_values[key].append(value)

                # VALUE EXISTS:
                else:
                    print(f"'{value}' ALREADY REGISTER IN KEY: {key}")
                    continue
            
            else:
                dict_values[key] = [value]

            print(f'\n\033[1;33m>> {value} ADDED!\033[0;00m')

            condicion = input("\n\n# Add more item? ").upper()

            print('\n', "-"*30)

            if condicion == 'N' or condicion == 'NO':
                break

        print("\033[1;32mItems added successfully!\033[0;00m")
        sleep(3.0)
        logo_forca()
        print("\033[1;35m<> OPTION 2: Add Items\033[0;00m")

        # WRITE IN THE ARQUIVE "dados.json"
        write_json(dict_values)
        continue
        
        
    elif option == 3:
        logo_forca()
        print("\033[1;34m<> OPTION 3: See Items\033[0;00m")
        show_dict(dict_values)
        sleep(10.0)
        continue