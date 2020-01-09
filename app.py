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
        folderNam = str(input('Pick a folder: ')).lower().strip()
        folderExists = indicateIfFolderExists(folderNam)
        if folderExists == True:
            print(f'\n{Fore.GREEN}Folder ( {Fore.WHITE}{folderNam}{Fore.GREEN} ) does exist.')
            print(Fore.YELLOW)
            fileNam = str(input('Input new filename: '))
            if fileNam.endswith('.txt') == True:
                fileNam = fileNam[:-4]
        else:
            print(f'\n{Fore.RED}Folder ( {Fore.WHITE}{folderNam}{Fore.RED} ) does not exist.')
            mainFunction()
        createFile(folderNam, fileNam)
    elif action == actionsDictionary['actions'][3]['action']: # If writing to
        showall_inparent()
        print(Fore.YELLOW)
        folderNam = str(input('\nPick a folder: ')).lower().strip()
        folderExists = indicateIfFolderExists(folderNam)
        if folderExists == True:
            print(Fore.YELLOW)
            chckDirectory(folderNam)#Prints out text files available
            print(f'\n{Fore.GREEN}Folder ( {Fore.WHITE}{folderNam}{Fore.GREEN} ) does exist.')
            print(Fore.YELLOW)
            fileNam = str(input('Write to which file? '))
            fileMatchList(folderNam, fileNam)#Finds if this is an existing file
            print(Fore.YELLOW)
            text = str(input('What is your message: '))
            text = 'Entry: ' + text
            if fileNam.endswith('.txt') == True:
                fileNam = fileNam[:-4]
            writeToFile(folderNam, fileNam, text)
        else:
            print(f'\n{Fore.RED}Folder ( {Fore.WHITE}{folderNam}{Fore.RED} ) does not exist.')
            mainFunction()
    elif action == actionsDictionary['actions'][2]['action']: # If reading a file
        # showall_inparent()
        show_folder_contents()
        print(Fore.YELLOW)
        folderNam = str(input('\nPick a folder: ')).lower().strip()
        folderExists = checkIfFolderExists(folderNam)
        if folderExists == True:
            chckDirectory(folderNam)
            print(Fore.YELLOW)
            fileNam = str(input('Give a filename: ')).lower().strip()
            fileMatchList(folderNam, fileNam)
            print(Style.RESET_ALL)
            if fileNam.endswith('.txt'):
                fileNam = fileNam[:-4]
            readFile(folderNam, fileNam)
        else:
            mainFunction()
    elif action == actionsDictionary['actions'][4]['action']:
        showFolders()
        print(Fore.YELLOW)
        folderNam = str(input('Input a folder: '))
        folderExists = indicateIfFolderExists(folderNam)
        if folderExists == True:
            print(f'\n{Fore.GREEN}Folder ( {Fore.WHITE}{folderNam}{Fore.GREEN} ) does exist.')
            chckDirectory(folderNam)
            print(Fore.YELLOW)
            fileNam = str(input('Give a filename: ')).lower().strip()
            fileMatchList(folderNam, fileNam)
            print(Style.RESET_ALL)
            if fileNam.endswith('.txt'):
                fileNam = fileNam[:-4]
            updateFileEntry(folderNam, fileNam)
        else:
            print(f'\n{Fore.RED}Folder ( {Fore.WHITE}{folderNam}{Fore.RED} ) does not exist.')
            mainFunction()
    elif action == actionsDictionary['actions'][5]['action']: # If deleting a file
        showall_inparent()
        print(Fore.YELLOW)
        folderNam = str(input('Input a folder: '))
        folderExists = indicateIfFolderExists(folderNam)
        if folderExists == True:
            print(f'\n{Fore.GREEN}Folder ( {Fore.WHITE}{folderNam}{Fore.GREEN} ) does exist.')
            chckDirectory(folderNam)
            print(Fore.YELLOW)
            fileNam = str(input('Give a filename: ')).lower().strip()
            fileMatchList(folderNam, fileNam)
            print(Style.RESET_ALL)
            if fileNam.endswith('.txt'):
                fileNam = fileNam[:-4]
            deleteFile(folderNam, fileNam)
    elif action == actionsDictionary['actions'][1]['action']:
        newFolderName = str(input('New folder name: ')).lower().strip()
        indicatorVar = indicateIfFolderExists(newFolderName)
        if indicatorVar == True:
            print(f'\n{Fore.RED}Folder ( {Fore.WHITE}{newFolderName}{Fore.RED} ) exists...')
            mainFunction()
        else:
            print(f'\n{Fore.GREEN}Folder ( {Fore.WHITE}{newFolderName}{Fore.GREEN} ) did not exist.')
            createFolder(newFolderName)
    elif action == actionsDictionary['actions'][6]['action']:
        showFolders()
        print('Which folder do you want to delete? ')
        deleteFolderName = str(input('Input a folder here: '))
        deleteFolder(deleteFolderName)
    elif action == actionsDictionary['actions'][7]['action']:
        print(Fore.YELLOW)
        print('Commands Available: ')
        for key in actionsDictionary.get('actions'):
            print(key['action'] + ' => ' + key['actiondesc'])
        mainFunction()
    elif action == actionsDictionary['actions'][8]['action']: # If exiting the program
        print(Fore.LIGHTBLUE_EX + '\nYou are exiting the application.\n')
        print(exit())
    else:
        print(Fore.LIGHTMAGENTA_EX+'\nCommand does not exist.') # Command not found
        mainFunction()

# -----------------------------------------------------------------

def chckDirectory(folder): # Checking directory for text files
    print(Style.RESET_ALL)
    print(Fore.YELLOW + '\nChoose from files:')
    CWDFolderVar = getCWDstring(folder)
    for file in os.listdir(f'{CWDFolderVar}'):
        if file.endswith('.txt'):
            print(Fore.WHITE + f'{file}')
    print('\n')

def fileMatchList(folder, zfile):
    CWDFolderVar = getCWDstring(folder)
    folderFileList = os.listdir(f'{CWDFolderVar}')[:]
    if zfile.endswith('.txt') == True:
        if zfile not in folderFileList:
            print(Fore.RED+f'{zfile} was not found.')
            mainFunction()
        else:
            print(Fore.GREEN+f'You selected file ({Fore.WHITE} {zfile} {Fore.GREEN}).')
    else:
        zfile = zfile + '.txt'
        if zfile not in folderFileList:
            print(Fore.RED+f'{zfile} was not found.')
            mainFunction()
        else:
            print(Fore.GREEN+f'You selected file ({Fore.WHITE} {zfile} {Fore.GREEN}).')

def checkIfFolderExists(checkFolder):
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

def indicateIfFolderExists(checkFolder):
    data = []
    for dir in next(os.walk('.'))[1]:
        data.append(dir)
    if checkFolder in data:
        return True
    else:
        return False    

def showall_inparent():
    print(Fore.WHITE+'\n<================================================')
    # for dirname, dirnames, filenames in os.walk('.'):
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

        for filename in three:
            print(Fore.CYAN + os.path.join(one, filename))  
        # Advanced usage:
        # editing the 'dirnames' list will stop os.walk() from recursing into there.
        if '.git' in two:
            # don't go into any .git directories.
            two.remove('.git')
    print(Fore.WHITE+'<================================================')  

def showFolders():
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
def createFile(folder, fileName):
    print(Style.RESET_ALL)
    open(f'./{folder}/{fileName}.txt','w')
    print(Fore.GREEN + f'\n/{folder}/{Fore.WHITE}{fileName}.txt {Fore.GREEN}was created...')
    mainFunction()

def readFile(folder, fileName):
    print(Style.RESET_ALL)
    if fileName.endswith('.txt'):
        fileName = fileName[:-4]
    rf = open(f'./{folder}/{fileName}.txt', 'r')
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
    mainFunction()

# Trying to find string to update
# Dynamically appending list item
def updateFileEntry(folder, file):
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
    mainFunction()


def writeToFile(folder, file, text):
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
    mainFunction()

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
            mainFunction()
        elif confirm == 'no':
            mainFunction()
    while file not in folder:#WTF lets fix this...
        print(Fore.LIGHTRED_EX + 'File does not exist.')
        chckDirectory(folder)
        print(Fore.YELLOW)
        file = str(input('Give a filename: ')).lower().strip()
        if os.path.exists(f'./{folder}/{file}.txt'):
            print(Back.RESET,Fore.RED)
            print('Are you sure you want to delete this file?')
            confirm = str(input('(yes/no): ').lower()).strip()
            if confirm == 'yes':
                os.remove(f'./{folder}/{file}.txt')
                print('\n')
                print(Fore.RED + file + '.txt was deleted..')
                mainFunction()
            elif confirm == 'no':
                mainFunction()        

# Directory/Folder CRUD
def createFolder(passedDirName):
    newFolder = f'{passedDirName}/'
    newFolderVar = getCWDstring(passedDirName)
    try:
        # Figure out how to get parent directory to be code generated.
        os.makedirs(f'{newFolderVar}')
        print(f'{Fore.GREEN}Directory {Fore.WHITE}{newFolder}{Fore.GREEN} has been created ')
    except FileExistsError:
        print(f'{Fore.RED}Directory {Fore.WHITE}{newFolder}{Fore.RED} already exists')
    mainFunction()

def deleteFolder(dirName):
    directory = f'{dirName}'
    parent = os.getcwd()
    path = os.path.join(parent, directory)
    os.rmdir(path)
    print(Fore.GREEN+f"\nDirectory '%s' has been removed successfully" %directory)
    mainFunction()

def getCWDstring(folder):
    currentWorkingDir = os.getcwd()
    currentfolder = f'{currentWorkingDir}/{folder}/'.replace('\\','/')
    # listFiles = os.listdir(currentfolder) 
    return currentfolder

# ----------------- give action to assign function -----------------
# Decide What you would like to do
def mainFunction():
    print(Style.RESET_ALL)
    print(Fore.YELLOW + 'What would you like to do?')
    print(Fore.YELLOW + 'Example Commands: /createfile /writeto /commands /exit')
    action = str(input('Input your action: ')).lower().strip()
    # decide what file we're going to do what with
    assignAction(action)  

# Also need to adjust create and write to files to take in another parameter
# The parameter being which directory...

if __name__ == "__main__":
    mainFunction()