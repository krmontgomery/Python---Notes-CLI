'''This is a CRUD based CLI program.'''
from colorama import Fore, Style, init
from actions_dictionary import action_dictionary
from ifs import chck_directory, checkif_folder_exists
from ifs import indicate_if_folder_exists, file_match_list
from ifs import show_folders, show_folder_contents
from actions import create_file, create_folder, update_file_entry
from actions import delete_file, delete_folder, write_to_file, read_file

init(autoreset=False)

# ----------------------------------------------------------------------------
# Function that assigns order of operations given the user input
# ----------------------------------------------------------------------------
def assign_action(action):
    '''Depending on the action input, this function
     gives directions to perform the desired outcome.'''
    if disperse_action(action) == '/createfile': # If Create a File
        print(Fore.YELLOW)
        show_folders()
        print(Fore.YELLOW+'\n')
        folder_nam = str(input('Pick a folder: ')).lower().strip()
        folder_exists = indicate_if_folder_exists(folder_nam)
        if folder_exists is True:
            print(f'\n{Fore.GREEN}Folder ( {Fore.WHITE}{folder_nam}{Fore.GREEN} ) does exist.')
            print(Fore.YELLOW)
            file_nam = str(input('Input new file_name: '))
            if file_nam.endswith('.txt') is True:
                file_nam = file_nam[:-4]
        else:
            print(f'\n{Fore.RED}Folder ( {Fore.WHITE}{folder_nam}{Fore.RED} ) does not exist.')
            main_function()
        create_file(folder_nam, file_nam)
        main_function()
    elif disperse_action(action) == '/writeto': # If writing to
        show_folders()
        print(Fore.YELLOW)
        folder_nam = str(input('\nPick a folder: ')).lower().strip()
        folder_exists = indicate_if_folder_exists(folder_nam)
        if folder_exists is True:
            print(Fore.YELLOW)
            chck_directory(folder_nam)#Prints out text files available
            print(f'\n{Fore.GREEN}Folder ( {Fore.WHITE}{folder_nam}{Fore.GREEN} ) does exist.')
            print(Fore.YELLOW)
            file_nam = str(input('Write to which file? '))
            file_match_list(folder_nam, file_nam)#Finds if this is an existing file
            print(Fore.YELLOW)
            text = str(input('What is your message: '))
            text = 'Entry: ' + text
            if file_nam.endswith('.txt') is True:
                file_nam = file_nam[:-4]
            write_to_file(folder_nam, file_nam, text)
            main_function()
        else:
            print(f'\n{Fore.RED}Folder ( {Fore.WHITE}{folder_nam}{Fore.RED} ) does not exist.')
            main_function()
    elif disperse_action(action) == '/readfrom': # If reading a file
        show_folders()
        print(Fore.YELLOW)
        folder_nam = str(input('\nPick a folder: ')).lower().strip()
        folder_exists = checkif_folder_exists(folder_nam)
        if folder_exists is True:
            chck_directory(folder_nam)
            print(Fore.YELLOW)
            file_nam = str(input('Give a file_name: ')).lower().strip()
            file_match_list(folder_nam, file_nam)
            print(Style.RESET_ALL)
            if file_nam.endswith('.txt'):
                file_nam = file_nam[:-4]
            read_file(folder_nam, file_nam)
            main_function()
        else:
            main_function()
    elif disperse_action(action) == '/update':
        show_folders()
        print(Fore.YELLOW)
        folder_nam = str(input('Input a folder: '))
        folder_exists = indicate_if_folder_exists(folder_nam)
        if folder_exists is True:
            print(f'\n{Fore.GREEN}Folder ( {Fore.WHITE}{folder_nam}{Fore.GREEN} ) does exist.')
            chck_directory(folder_nam)
            print(Fore.YELLOW)
            file_nam = str(input('Give a file_name: ')).lower().strip()
            file_match_list(folder_nam, file_nam)
            print(Style.RESET_ALL)
            if file_nam.endswith('.txt'):
                file_nam = file_nam[:-4]
            update_file_entry(folder_nam, file_nam)
            main_function()
        else:
            print(f'\n{Fore.RED}Folder ( {Fore.WHITE}{folder_nam}{Fore.RED} ) does not exist.')
            main_function()
    elif disperse_action(action) == '/deletefile': # If deleting a file
        show_folders()
        print(Fore.YELLOW)
        folder_nam = str(input('Input a folder: '))
        folder_exists = indicate_if_folder_exists(folder_nam)
        if folder_exists is True:
            print(f'\n{Fore.GREEN}Folder ( {Fore.WHITE}{folder_nam}{Fore.GREEN} ) does exist.')
            chck_directory(folder_nam)
            print(Fore.YELLOW)
            file_nam = str(input('Give a file_name: ')).lower().strip()
            file_match_list(folder_nam, file_nam)
            print(Style.RESET_ALL)
            if file_nam.endswith('.txt'):
                file_nam = file_nam[:-4]
            delete_file(folder_nam, file_nam)
    elif disperse_action(action) == '/createdir':
        newfolder_name = str(input('New folder name: ')).lower().strip()
        indicator_var = indicate_if_folder_exists(newfolder_name)
        if indicator_var is True:
            print(f'\n{Fore.RED}Folder ( {Fore.WHITE}{newfolder_name}{Fore.RED} ) exists...')
            main_function()
        else:
            print(f'\n{Fore.GREEN}Folder ( {Fore.WHITE}{newfolder_name}{Fore.GREEN} ) did not exist.')
            create_folder(newfolder_name)
            main_function()
    elif disperse_action(action) == '/deletedir':
        show_folders()
        print(f'{Fore.YELLOW}Which folder do you want to delete?')
        delete_folder_name = str(input('Input a folder here: '))
        delete_folder(delete_folder_name)
    elif disperse_action(action) == '/commands':
        print(Fore.MAGENTA)
        print('Commands Available: ')
        for act in action_dictionary:
            each_action = action_dictionary[act]['action']
            each_desc = action_dictionary[act]['actiondesc']
            print('\n' + Fore.WHITE + each_action + '\n' + '-' + Fore.MAGENTA + each_desc)
        main_function()
    elif disperse_action(action) == '/exit': # If exiting the program
        print(Fore.LIGHTBLUE_EX + '\nYou are exiting the application.\n')
        print(exit())
    elif disperse_action(action) == '/showall':
        show_folder_contents()
        main_function()
    else:
        print(Fore.LIGHTMAGENTA_EX+'\nCommand does not exist.') # Command not found
        main_function()

# -----------------------------------------------------------------
# Dealing with actions
# -----------------------------------------------------------------
def does_action_exist(action):
    '''Decide if action entered is one that exists.'''
    actions_var = action_dictionary
    for act in actions_var:
        each_action = action_dictionary[act]['action']
        if action == each_action:
            return True

def disperse_action(action):
    '''If action exists, this function will return the same command in a string.'''
    my_action = action
    indicator = does_action_exist(my_action)
    if indicator is True:
        actions_var = action_dictionary
        for act in actions_var:
            our_action = action_dictionary[act]['action']
            if action == our_action:
                return our_action

# -----------------  -----------------
#   | Main Function
# ------------------------------------
# Decide What you would like to do
# ------------------------------------
def main_function():
    '''CLI Program main function.'''
    print(Style.RESET_ALL)
    print(Fore.YELLOW + 'What would you like to do?')
    print(Fore.YELLOW + 'Example Commands: /createfile /writeto /commands /exit')
    action = str(input('Input your action: ')).lower().strip()
    # decide what file we're going to do what with
    assign_action(action)

# Also need to adjust create and write to files to take in another parameter
# The parameter being which directory...

# ----------------------------------
# Run Program
# ----------------------------------
if __name__ == "__main__":
    main_function()
# ----------------------------------
