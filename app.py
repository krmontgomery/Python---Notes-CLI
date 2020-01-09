import os
from datetime import datetime
from colorama import Fore, Back, Style, init
import fileinput
from actions_dictionary import actionsDictionary

init(autoreset=False)

# ----------------- Assigning Function based on user input -----------------
def assignAction(action):
    if action == actionsDictionary['actions'][0]['action']: # If Create a File
        print(Fore.YELLOW)
        showall_inparent()
        print(Fore.YELLOW+'\n')
        folder_nam = str(input('Pick a folder: ')).lower().strip()
        folder_exists = indicate_if_folder_exists(folder_nam)
        if folder_exists == True:
            print(f'\n{Fore.GREEN}Folder ( {Fore.WHITE}{folder_nam}{Fore.GREEN} ) does exist.')
            print(Fore.YELLOW)
            folder_nam = str(input('Input new folder_name: '))
            if folder_nam.endswith('.txt') == True:
                folder_nam = folder_nam[:-4]
        else:
            print(f'\n{Fore.RED}Folder ( {Fore.WHITE}{folder_nam}{Fore.RED} ) does not exist.')
            main_function()
        create_file(folder_nam, folder_nam)
    elif action == actionsDictionary['actions'][3]['action']: # If writing to
        showall_inparent()
        print(Fore.YELLOW)
        folder_nam = str(input('\nPick a folder: ')).lower().strip()
        folder_exists = indicate_if_folder_exists(folder_nam)
        if folder_exists == True:
            print(Fore.YELLOW)
            chck_directory(folder_nam)#Prints out text files available
            print(f'\n{Fore.GREEN}Folder ( {Fore.WHITE}{folder_nam}{Fore.GREEN} ) does exist.')
            print(Fore.YELLOW)
            folder_nam = str(input('Write to which file? '))
            fileMatchList(folder_nam, folder_nam)#Finds if this is an existing file
            print(Fore.YELLOW)
            text = str(input('What is your message: '))
            text = 'Entry: ' + text
            if folder_nam.endswith('.txt') == True:
                folder_nam = folder_nam[:-4]
            write_to_file(folder_nam, folder_nam, text)
        else:
            print(f'\n{Fore.RED}Folder ( {Fore.WHITE}{folder_nam}{Fore.RED} ) does not exist.')
            main_function()
    elif action == actionsDictionary['actions'][2]['action']: # If reading a file
        # showall_inparent()
        show_folder_contents()
        print(Fore.YELLOW)
        folder_nam = str(input('\nPick a folder: ')).lower().strip()
        folder_exists = checkIffolder_exists(folder_nam)
        if folder_exists == True:
            chck_directory(folder_nam)
            print(Fore.YELLOW)
            folder_nam = str(input('Give a folder_name: ')).lower().strip()
            fileMatchList(folder_nam, folder_nam)
            print(Style.RESET_ALL)
            if folder_nam.endswith('.txt'):
                folder_nam = folder_nam[:-4]
            read_file(folder_nam, folder_nam)
        else:
            main_function()
    elif action == actionsDictionary['actions'][4]['action']:
        show_folders()
        print(Fore.YELLOW)
        folder_nam = str(input('Input a folder: '))
        folder_exists = indicate_if_folder_exists(folder_nam)
        if folder_exists == True:
            print(f'\n{Fore.GREEN}Folder ( {Fore.WHITE}{folder_nam}{Fore.GREEN} ) does exist.')
            chck_directory(folder_nam)
            print(Fore.YELLOW)
            folder_nam = str(input('Give a folder_name: ')).lower().strip()
            fileMatchList(folder_nam, folder_nam)
            print(Style.RESET_ALL)
            if folder_nam.endswith('.txt'):
                folder_nam = folder_nam[:-4]
            update_file_entry(folder_nam, folder_nam)
        else:
            print(f'\n{Fore.RED}Folder ( {Fore.WHITE}{folder_nam}{Fore.RED} ) does not exist.')
            main_function()
    elif action == actionsDictionary['actions'][5]['action']: # If deleting a file
        showall_inparent()
        print(Fore.YELLOW)
        folder_nam = str(input('Input a folder: '))
        folder_exists = indicate_if_folder_exists(folder_nam)
        if folder_exists == True:
            print(f'\n{Fore.GREEN}Folder ( {Fore.WHITE}{folder_nam}{Fore.GREEN} ) does exist.')
            chck_directory(folder_nam)
            print(Fore.YELLOW)
            folder_nam = str(input('Give a folder_name: ')).lower().strip()
            fileMatchList(folder_nam, folder_nam)
            print(Style.RESET_ALL)
            if folder_nam.endswith('.txt'):
                folder_nam = folder_nam[:-4]
            deleteFile(folder_nam, folder_nam)
    elif action == actionsDictionary['actions'][1]['action']:
        newfolder_name = str(input('New folder name: ')).lower().strip()
        indicator_var = indicate_if_folder_exists(newfolder_name)
        if indicator_var == True:
            print(f'\n{Fore.RED}Folder ( {Fore.WHITE}{newfolder_name}{Fore.RED} ) exists...')
            main_function()
        else:
            print(f'\n{Fore.GREEN}Folder ( {Fore.WHITE}{newfolder_name}{Fore.GREEN} ) did not exist.')
            createFolder(newfolder_name)
    elif action == actionsDictionary['actions'][6]['action']:
        show_folders()
        print('Which folder do you want to delete? ')
        deletefolder_name = str(input('Input a folder here: '))
        deleteFolder(deletefolder_name)
    elif action == actionsDictionary['actions'][7]['action']:
        print(Fore.YELLOW)
        print('Commands Available: ')
        for key in actionsDictionary.get('actions'):
            print(key['action'] + ' => ' + key['actiondesc'])
        main_function()
    elif action == actionsDictionary['actions'][8]['action']: # If exiting the program
        print(Fore.LIGHTBLUE_EX + '\nYou are exiting the application.\n')
        print(exit())
    else:
        print(Fore.LIGHTMAGENTA_EX+'\nCommand does not exist.') # Command not found
        main_function()

# -----------------------------------------------------------------

def chck_directory(folder): # Checking directory for text files
    print(Style.RESET_ALL)
    print(Fore.YELLOW + '\nChoose from files:')
    CWDFolderVar = get_cwd_string(folder)
    for file in os.listdir(f'{CWDFolderVar}'):
        if file.endswith('.txt'):
            print(Fore.WHITE + f'{file}')
    print('\n')

def fileMatchList(folder, zfile):
    CWDFolderVar = get_cwd_string(folder)
    folderFileList = os.listdir(f'{CWDFolderVar}')[:]
    if zfile.endswith('.txt') == True:
        if zfile not in folderFileList:
            print(Fore.RED+f'{zfile} was not found.')
            main_function()
        else:
            print(Fore.GREEN+f'You selected file ({Fore.WHITE} {zfile} {Fore.GREEN}).')
    else:
        zfile = zfile + '.txt'
        if zfile not in folderFileList:
            print(Fore.RED+f'{zfile} was not found.')
            main_function()
        else:
            print(Fore.GREEN+f'You selected file ({Fore.WHITE} {zfile} {Fore.GREEN}).')

def checkIffolder_exists(checkFolder):
    data = []
    print(Fore.WHITE+'\n<================================')
    for dir in next(os.walk('.'))[1]:
        print('\n'+Fore.CYAN+'/'+dir)
        data.append(dir)
    print(Fore.WHITE+'\n<================================')
        # data = '[' + ','.join(dir) + ']'
    # compareDir = str(input('Type in folder: ')).lower().strip()
    if checkFolder in data:
        return True
    else:
        return False

def indicate_if_folder_exists(checkFolder):
    data = []
    for dir in next(os.walk('.'))[1]:
        data.append(dir)
    if checkFolder in data:
        return True
    else:
        return False

def showall_inparent():
    '''Show all in parent. (possibly removing this function soon)'''
    print(Fore.WHITE+'\n<================================================')
    # for dirname, dirnames, folder_names in os.walk('.'):
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
        # for subdirname in two:
        #     print(Fore.CYAN + os.path.join(one, subdirname))

        for folder_name in three:
            print(Fore.CYAN + os.path.join(one, folder_name))  
        # Advanced usage:
        # editing the 'dirnames' list will stop os.walk() from recursing into there.
        if '.git' in two:
            # don't go into any .git directories.
            two.remove('.git')
    print(Fore.WHITE+'<================================================')  

def show_folders():
    '''This function will only display the subdirectories of the parent.'''
    print(Fore.WHITE+'\n<================================================')
    for one, two, three in os.walk('.'):
        if '.git' in two:
            two.remove('.git')
        if '__pycache__' in two:
            two.remove('__pycache__')
        for subdirname in two:
            print(Fore.CYAN + os.path.join(one, subdirname))
    print(Fore.WHITE+'<================================================')

def show_folder_contents():
    '''This is a function to display a top down view from each subdirectory.'''
    print(Fore.WHITE+'\n<================================================')
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
        if one == '.':
            one = print(Fore.LIGHTBLUE_EX + '***Folders Listed Below***')
        else:
            print(Fore.YELLOW + '<==============')
            print(f'{Fore.LIGHTWHITE_EX}{one}')
            print(Fore.YELLOW + '<================')
        for files in three:
            print(f'{Fore.WHITE}{files}')
    print(Fore.WHITE+'<================================================')
# ------------------------------------------------------------------

# ----------------- (App Actions) Functions -----------------
def create_file(folder, folder_name):
    print(Style.RESET_ALL)
    open(f'./{folder}/{folder_name}.txt','w')
    print(Fore.GREEN + f'\n/{folder}/{Fore.WHITE}{folder_name}.txt {Fore.GREEN}was created...')
    main_function()

def read_file(folder, folder_name):
    print(Style.RESET_ALL)
    if folder_name.endswith('.txt'):
        folder_name = folder_name[:-4]
    rf = open(f'./{folder}/{folder_name}.txt', 'r')
    eachLineOut = rf.readlines()
    for line in eachLineOut[:]:
        if line.startswith("Entry: "):
            print(Fore.GREEN)
            line = f'{line}'
            print(line)
        else:
            print(Fore.WHITE)
            line = f'{line}'
            print(line)
    print(Style.RESET_ALL)
    rf.close()
    main_function()

# Trying to find string to update
# Dynamically appending list item
def update_file_entry(folder, file):
    # Open file for reading
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
    codeToExec = f"""{inputstr} = 'Entry: (Updated) {whatToSay}' """
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
    main_function()


def write_to_file(folder, file, text):
    rf = open(f'./{folder}/{file}.txt', 'r')
    rf = rf.readlines()
    if rf == []:
        print(Style.RESET_ALL)
        NewEntryHeader = datetime.today().date()
        now = datetime.now()
        theTime = now.strftime('%I:%M %p')
        header = f'{NewEntryHeader} {theTime}'
        wf = open(f'./{folder}/{file}.txt', 'a')
        wf.write(f'{header}: \n{text}')
        print(Fore.BLUE + '\nYou wrote:')
        print(Fore.CYAN + f'\n{text}')
        print(Fore.BLUE + f'\nTo {file}.txt')
        wf.close()
    else:
        print(Style.RESET_ALL)
        NewEntryHeader = datetime.today().date()
        now = datetime.now()
        theTime = now.strftime('%I:%M %p')
        header = f'{NewEntryHeader} {theTime}'
        wf = open(f'./{folder}/{file}.txt', 'a')
        wf.write(f'\n{header}: \n{text}')
        print(Fore.BLUE + '\nYou wrote:')
        print(Fore.CYAN + f'\n{text}')
        print(Fore.BLUE + f'\nTo {file}.txt')
        wf.close()
    main_function()

def deleteFile(folder, file):
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
        file = str(input('Give a folder_name: ')).lower().strip()
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
def createFolder(passedDirName):
    newFolder = f'{passedDirName}/'
    newFolderVar = get_cwd_string(passedDirName)
    try:
        # Figure out how to get parent directory to be code generated.
        os.makedirs(f'{newFolderVar}')
        print(f'{Fore.GREEN}Directory {Fore.WHITE}{newFolder}{Fore.GREEN} has been created ')
    except FileExistsError:
        print(f'{Fore.RED}Directory {Fore.WHITE}{newFolder}{Fore.RED} already exists')
    main_function()

def deleteFolder(dirName):
    directory = f'{dirName}'
    parent = os.getcwd()
    path = os.path.join(parent, directory)
    os.rmdir(path)
    print(Fore.GREEN+f"\nDirectory '%s' has been removed successfully" %directory)
    main_function()

def get_cwd_string(folder):
    '''Getting the current working directory for which parent you will be working out of.'''
    currentWorkingDir = os.getcwd()
    currentfolder = f'{currentWorkingDir}/{folder}/'.replace('\\','/')
    # listFiles = os.listdir(currentfolder) 
    return currentfolder

# ----------------- give action to assign function -----------------
# Decide What you would like to do
def main_function():
    '''Main function for CLI Program.'''
    print(Style.RESET_ALL)
    print(Fore.YELLOW + 'What would you like to do?')
    print(Fore.YELLOW + 'Example Commands: /create_file /writeto /commands /exit')
    action = str(input('Input your action: ')).lower().strip()
    # decide what file we're going to do what with
    assignAction(action)  

# Also need to adjust create and write to files to take in another parameter
# The parameter being which directory...

if __name__ == "__main__":
    main_function()
