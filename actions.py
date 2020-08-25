'''Module holds the different action functions for the CLI program.'''
import os
from datetime import datetime
from colorama import Fore, Back, Style, init
from ifs import chck_directory, get_cwd_string

init(autoreset=False)

# ----------------- (App Actions) Functions ------------------
# ------------------------------------------------------------
def create_file(folder, file_name):
    '''Create a file.'''
    print(Style.RESET_ALL)
    open(f'./{folder}/{file_name}.txt','w')
    print(Fore.GREEN + f'\n/{folder}/{Fore.WHITE}{file_name}.txt {Fore.GREEN}was created...')

def read_file(folder, file_name):
    '''Read from a specific file.'''
    print(Style.RESET_ALL)
    if file_name.endswith('.txt'):
        file_name = file_name[:-4]
    rf = open(f'./{folder}/{file_name}.txt', 'r')
    eachLineOut = rf.readlines()
    for line in eachLineOut[:]:
        if line.startswith("Entry: "):
            print(Fore.GREEN)
            line = f'{line.rstrip()}'
            print(line + Fore.LIGHTYELLOW_EX+'\n<================================================')
        else:
            line = f'{Fore.WHITE}{line}'
            print('\n' + line + Fore.LIGHTYELLOW_EX+'<----------------------')
            # print(Fore.LIGHTYELLOW_EX+'<----------------------')
    print(Style.RESET_ALL)
    rf.close()

# Trying to find string to update
# Dynamically appending list item
def update_file_entry(folder, file):
    '''Update a file entry.'''
    rf = open(f'./{folder}/{file}.txt', 'r')
    listItems = rf.readlines()#store in variable
    rf.close()
    counter = -1
    for i in listItems:
        newlist = []
        counter += 1
        newlist.append(i)
        newvar = f'\n{Fore.CYAN}{i} {Fore.WHITE}To update this entry type in => lines[{str(counter)}]'
        print(f'{newvar}')
    print(Fore.YELLOW)
    inputstr = str(input('\nWhich item to update? ')).lower().strip()
    whatToSay = str(input('Update with? ')).lower().strip()
    rf = open(f'./{folder}/{file}.txt', 'r')
    lines = rf.readlines()
    codeToExec = f"""{inputstr} = "Entry: (Updated) {whatToSay}" """
    exec(codeToExec)
    rf.close()
    # Try to get newlines normal
    wf = open(f'./{folder}/{file}.txt', 'w')
    lines = [line.rstrip('\n') for line in lines]
    lines = [line + '\n' for line in lines]
    wf.writelines(lines)
    wf.close()
    print(Fore.CYAN)
    print(f'\nYou updated entry to: {whatToSay}')


def write_to_file(folder, file, text):
    '''Make an entry to a file.'''
    rf = open(f'./{folder}/{file}.txt', 'r')
    rf = rf.readlines()
    if rf == []:
        print(Style.RESET_ALL)
        new_entry_header = datetime.today().date()
        now = datetime.now()
        the_time = now.strftime('%I:%M %p')
        header = f'{new_entry_header} {the_time}'
        wf = open(f'./{folder}/{file}.txt', 'a')
        wf.write(f'{header}: \n{text}')
        print(Fore.BLUE + '\nYou wrote:')
        print(Fore.CYAN + f'\n{text}')
        print(Fore.BLUE + f'\nTo {file}.txt')
        wf.close()
    else:
        print(Style.RESET_ALL)
        new_entry_header = datetime.today().date()
        now = datetime.now()
        the_time = now.strftime('%I:%M %p')
        header = f'{new_entry_header} {the_time}'
        wf = open(f'./{folder}/{file}.txt', 'a')
        wf.write(f'\n{header}: \n{text}')
        print(Fore.BLUE + '\nYou wrote:')
        print(Fore.CYAN + f'\n{text}')
        print(Fore.BLUE + f'\nTo {file}.txt')
        wf.close()

def delete_file(folder, file):
    from app import main_function
    '''Delete a specific file.'''
    print(Style.RESET_ALL)
    if os.path.exists(f'./{folder}/{file}.txt'):
        print(Back.RESET,Fore.RED)
        print('Are you sure you want to delete this file?')
        confirm = str(input('(yes/no): ')).lower().strip()
        if confirm == 'yes':
            os.remove(f'./{folder}/{file}.txt')
            print('\n')
            print(Fore.RED + file + '.txt was deleted..')
            main_function()
        elif confirm == 'no':
            main_function()
    while file not in folder:#WTF lets fix this...
        print(Fore.LIGHTRED_EX + 'File does not exist.')
        chck_directory(folder)
        print(Fore.YELLOW)
        file = str(input('Give a file_name: ')).lower().strip()
        if os.path.exists(f'./{folder}/{file}.txt'):
            print(Back.RESET,Fore.RED)
            print('Are you sure you want to delete this file?')
            confirm = str(input('(yes/no): ').lower()).strip()
            if confirm == 'yes':
                os.remove(f'./{folder}/{file}.txt')
                print('\n')
                print(Fore.RED + file + '.txt was deleted..')
                main_function()
            elif confirm == 'no':
                main_function()

# Directory/Folder CRUD
def create_folder(passed_dir_name):
    '''Create a folder inside parent directory.'''
    new_folder = f'{passed_dir_name}/'
    new_folder_var = get_cwd_string(passed_dir_name)
    try:
        # Figure out how to get parent directory to be code generated.
        os.makedirs(f'{new_folder_var}')
        print(f'{Fore.GREEN}Directory {Fore.WHITE}{new_folder}{Fore.GREEN} has been created ')
    except FileExistsError:
        print(f'{Fore.RED}Directory {Fore.WHITE}{new_folder}{Fore.RED} already exists')

def delete_folder(dir_name):
    '''Delete a specific folder. '''
    directory = f'{dir_name}'
    parent = os.getcwd()
    path = os.path.join(parent, directory)
    os.rmdir(path)
    print(Fore.GREEN+f"\nDirectory '%s' has been removed successfully" %directory)