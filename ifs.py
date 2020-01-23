'''Holds the various IFS functions.'''
import os
from colorama import Fore, Style, init

init(autoreset=False)

def chck_directory(folder): # Checking directory for text files
    '''Prints a list of files from a folder.'''
    print(Style.RESET_ALL)
    print(Fore.YELLOW + '\nChoose from files:')
    cwd_folder_var = get_cwd_string(folder)
    for file in os.listdir(f'{cwd_folder_var}'):
        if file.endswith('.txt'):
            print(Fore.WHITE + f'{file}')
    print('\n')

def checkif_folder_exists(check_folder):
    '''Checks to see if folder exists.'''
    data = []
    # print(Fore.WHITE+'\n<================================')
    for dir in next(os.walk('.'))[1]:
        # print('\n'+Fore.CYAN+'/'+dir)
        data.append(dir)
    # print(Fore.WHITE+'\n<================================')
        # data = '[' + ','.join(dir) + ']'
    # compareDir = str(input('Type in folder: ')).lower().strip()
    if check_folder in data:
        return True
    else:
        return False

def indicate_if_folder_exists(check_folder):
    '''Figure out if the input folder name exists.'''
    data = []
    for dir in next(os.walk('.'))[1]:
        data.append(dir)
    if check_folder in data:
        return True
    else:
        return False

def showall_inparent():
    '''Show all in parent. (possibly removing this function soon)'''
    print(Fore.WHITE+'\n<================================================')
    # for dir_name, dirnames, file_names in os.walk('.'):
    for one, two, three in os.walk('.'):
        # print(one)
        # print(two)
        # print(three)
        if '__pycache__' in two:
            two.remove('__pycache__')
        if '.gitignore' in three:
            three.remove('.gitignore')
        if 'carbon.png' in three:
            three.remove('carbon.png')
        if 'Pipfile' in three:
            three.remove('Pipfile')
        if 'README.md' in three:
            three.remove('README.md')
        if 'actions_dictionary.py' in three:
            three.remove('actions_dictionary.py')
        if 'app.py' in three:
            three.remove('app.py')
        if 'actions.py' in three:
            three.remove('actions.py')
        if 'ifs.py' in three:
            three.remove('ifs.py')
        # for subdirname in two:
        #     print(Fore.CYAN + os.path.join(one, subdirname))
        for file_name in three:
            print(Fore.CYAN + os.path.join(one, file_name))
        # Advanced usage:
        # editing the 'dirnames' list will stop os.walk() from recursing into there.
        if '.git' in two:
            # don't go into any .git directories.
            two.remove('.git')
    print(Fore.WHITE+'<================================================')

def show_folders():
    '''This function will only display the subdirectories of the parent.'''
    print(Fore.WHITE+'\n<================================================')
    print(f'{Fore.LIGHTMAGENTA_EX}**List of subdirectories**')
    print(f'{Fore.WHITE}<=========================')
    for one, two, three in os.walk('.'):
        if '.git' in two:
            two.remove('.git')
        if '__pycache__' in two:
            two.remove('__pycache__')
        for subdirname in two:
            print(Fore.CYAN + os.path.join(one, subdirname))
    print(Fore.WHITE+'<================================================')
    print('\n')

def show_folder_contents():
    '''This is a function to display a top down view from each subdirectory.'''
    print(Fore.LIGHTWHITE_EX+'\n<================================================')
    for one, two, three in os.walk('.'):
        if '.git' in two:
            two.remove('.git')
        if '__pycache__' in two:
            two.remove('__pycache__')
        if '.gitignore' in three:
            three.remove('.gitignore')
        if 'carbon.png' in three:
            three.remove('carbon.png')
        if 'Pipfile' in three:
            three.remove('Pipfile')
        if 'README.md' in three:
            three.remove('README.md')
        if 'actions_dictionary.py' in three:
            three.remove('actions_dictionary.py')
        if 'app.py' in three:
            three.remove('app.py')
        if 'actions.py' in three:
            three.remove('actions.py')
        if 'ifs.py' in three:
            three.remove('ifs.py')
        if one == '.':
            one = print(Fore.BLUE + '***Subdirectories and their files listed below***')
        else:
            print(Fore.LIGHTMAGENTA_EX + '<==============')
            print(f'{Fore.LIGHTWHITE_EX}{one}')
            print(Fore.LIGHTMAGENTA_EX + '<================')
        for files in three:
            print(f'{Fore.GREEN}{files}')
    print(Fore.LIGHTWHITE_EX+'<================================================')

def get_cwd_string(folder):
    '''Get current working directory in a string.'''
    current_working_dir = os.getcwd()
    currentfolder = f'{current_working_dir}/{folder}/'.replace('\\', '/')
    # listFiles = os.listdir(currentfolder)
    return currentfolder

# -----------------------------------------------------------------
def file_match_list(folder, zfile):
    '''Checks to see if the file matches the input from the user. Otherwise, Exit.'''
    from app import main_function
    cwd_folder_var = get_cwd_string(folder)
    folder_file_list = os.listdir(f'{cwd_folder_var}')[:]
    if zfile.endswith('.txt') is True:
        if zfile not in folder_file_list:
            print(Fore.RED+f'{zfile} was not found.')
            main_function()
        else:
            print(Fore.GREEN+f'You selected file ({Fore.WHITE} {zfile} {Fore.GREEN}).')
    else:
        zfile = zfile + '.txt'
        if zfile not in folder_file_list:
            print(Fore.RED+f'{zfile} was not found.')
            main_function()
        else:
            print(Fore.GREEN+f'You selected file ({Fore.WHITE} {zfile} {Fore.GREEN}).')
