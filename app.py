import os
from datetime import datetime
from colorama import Fore, Back, Style, init
import fileinput


init(autoreset=False)
actionsArray = ['/createfile','/writeto', '/readfrom', '/update', '/deletefile', '/createdir', '/deletedir','/commands', '/exit']
fileList = os.listdir('C:/Users/User/Desktop/Notes_App/notes_folder')[:]

# ----------------- Assigning Function based on user input -----------------
def assignAction(action):
    if action == actionsArray[0]: # If Create a File
        print(Fore.YELLOW)
        showFolders()
        print(Fore.YELLOW+'\n')
        folderNam = str(input('Pick a folder: ')).lower().strip()
        folderExists = checkIfFolderExists(folderNam)
        if folderExists == True:
            print(Fore.YELLOW)
            fileNam = str(input('New File Name: ')).lower().strip()
        else:
            mainFunction()
        createFile(folderNam, fileNam)
    elif action == actionsArray[1]: # If writing to
        showFolders()
        folderNam = str(input('Pick a folder: ')).lower().strip()
        folderExists = checkIfFolderExists(folderNam)
        if folderExists == True:
            print(Fore.YELLOW)
            chckDirectory(folderNam)#Prints out text files available
            print(Fore.YELLOW)
            fileNam = str(input('Which file to write to: ')).lower().strip()
            fileMatchList(folderNam, fileNam)#Finds if this is an existing file
            print(Fore.YELLOW)
            text = str(input('What is your message: '))
            text = 'Entry: ' + text
            if fileNam.endswith('.txt'):
                fileNam = fileNam[:-4]
            writeToFile(folderNam, fileNam, text)
        else:
            mainFunction()
    elif action == actionsArray[2]: # If reading a file
        showFolders()
        print(Fore.YELLOW)
        folderNam = str(input('\nPick a folder: ')).lower().strip()
        folderExists = checkIfFolderExists(folderNam)
        if folderExists == True:
            chckDirectory(folderNam)
            print(Fore.YELLOW)
            fileNam = str(input('Give a filename: ')).lower().strip()
            if fileNam != fileNam.endswith('.txt'):
                fileNam = fileNam + '.txt'
            fileMatchList(folderNam, fileNam)
            print(Style.RESET_ALL)
            readFile(folderNam, fileNam)
        else:
            mainFunction()
    elif action == actionsArray[3]:
        chckDirectory(folder)
        print(Fore.YELLOW)
        fileNam = str(input('Give a filename: ')).lower().strip()
        fileMatchList(fileNam)
        updateFileEntry(fileNam)
    elif action == actionsArray[4]: # If deleting a file
        chckDirectory(folder)
        print(Fore.YELLOW)
        fileNam = str(input('Give a filename: ')).lower().strip()
        fileMatchList(fileNam)
        deleteFile(fileNam)
    elif action == actionsArray[5]:
        newFolderName = str(input('New folder name: ')).lower().strip()
        indicatorVar = indicateIfFolderExists(newFolderName)
        if indicatorVar == True:
            print(f'\n{Fore.RED}Folder ( {Fore.WHITE}{newFolderName}{Fore.RED} ) exists...')
            mainFunction()
        else:
            print(f'\n{Fore.GREEN}Folder ( {Fore.WHITE}{newFolderName}{Fore.GREEN} ) did not exist.')
            createFolder(newFolderName)
    elif action == actionsArray[6]:
        print('Which folder do you want to delete? ')
        deleteFolderName = str(input('Input a folder here: '))
        deleteFolder(deleteFolderName)
    elif action == actionsArray[7]:
        print(Fore.YELLOW)
        print('Commands Available: ')
        for cmd in actionsArray[:]:
            print(Fore.CYAN)
            print(cmd)
        mainFunction()
    elif action == actionsArray[8]: # If exiting the program
        print(Fore.LIGHTBLUE_EX + '\nYou are exiting the program.')
        print(exit())
    else:
        print(Fore.LIGHTMAGENTA_EX+'\nCommand does not exist.') # Command not found
        mainFunction()

# ----------------- List out existing files ------------------
def chckDirectory(folder): # Checking directory for text files
    print(Style.RESET_ALL)
    print(Fore.YELLOW + '\nChoose from files:')
    for file in os.listdir(f"C:/Users/User/Desktop/Notes_App/{folder}/"):
        if file.endswith('.txt'):
            print(Fore.WHITE + f'{file}')
    print('\n')

def fileMatchList(folder, zfile):
    folderFileList = os.listdir(f'C:/Users/User/Desktop/Notes_App/{folder}')[:]
    if zfile.endswith('.txt'):
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

      
# ----------------- (App Actions) Functions -----------------
def createFile(folder, fileName):
    print(Style.RESET_ALL)
    open(f'./{folder}/{fileName}.txt','w')
    print(Fore.GREEN + f'\n/{folder}/{fileName}.txt was created...')
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
def updateFileEntry(file):
    # Open file for reading
    rf = open(f'./notes_folder/{file}.txt', 'r')
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
    rf = open(f'./notes_folder/{file}.txt', 'r')
    lines = rf.readlines()
    codeToExec = f"""{inputstr} = '{whatToSay}' """
    exec(codeToExec)
    rf.close()
    # Try to get newlines normal
    wf = open(f'./notes_folder/{file}.txt', 'w')
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
        wf = open(f'./{folder}/{file}.txt', 'a')
        wf.write(f'{NewEntryHeader}: \n{text}')
        print(Fore.BLUE + '\nYou wrote:')
        print(Fore.CYAN + f'\n{text}')
        print(Fore.BLUE + f'\nTo {file}.txt')
        wf.close()
    else:
        print(Style.RESET_ALL)
        NewEntryHeader = datetime.today().date()
        wf = open(f'./{folder}/{file}.txt', 'a')
        wf.write(f'\n{NewEntryHeader}: \n{text}')
        print(Fore.BLUE + '\nYou wrote:')
        print(Fore.CYAN + f'\n{text}')
        print(Fore.BLUE + f'\nTo {file}.txt')
        wf.close()
    mainFunction()

def deleteFile(file):
    print(Style.RESET_ALL)
    if os.path.exists(f'./notes_folder/{file}.txt'):
        print(Back.RESET,Fore.RED)
        print('Are you sure you want to delete this file?')
        confirm = str(input('(yes/no): ')).lower().strip()
        if confirm == 'yes':
            os.remove(f'./notes_folder/{file}.txt')
            print('\n')
            print(Fore.RED + file + '.txt was deleted..')
            mainFunction()
        elif confirm == 'no':
            mainFunction()
    while file not in fileList:
        print(Fore.LIGHTRED_EX + 'File does not exist.')
        chckDirectory()
        print(Fore.YELLOW)
        file = str(input('Give a filename: ')).lower().strip()
        if os.path.exists(f'./notes_folder/{file}.txt'):
            print(Back.RESET,Fore.RED)
            print('Are you sure you want to delete this file?')
            confirm = str(input('(yes/no): ').lower()).strip()
            if confirm == 'yes':
                os.remove(f'./notes_folder/{file}.txt')
                print('\n')
                print(Fore.RED + file + '.txt was deleted..')
                mainFunction()
            elif confirm == 'no':
                mainFunction()        

# Directory/Folder CRUD
def createFolder(passedDirName):
    newFolder = f'{passedDirName}/'
    try:
        os.makedirs(f'C:/Users/User/Desktop/Notes_App/{newFolder}')
        print(f'{Fore.GREEN}Directory {Fore.WHITE}{newFolder}{Fore.GREEN} has been created ')
    except FileExistsError:
        print(f'{Fore.RED}Directory {Fore.WHITE}{newFolder}{Fore.RED} already exists')
    mainFunction()

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

def showFolders():
    print(Fore.WHITE+'\n<================================')
    for dir in next(os.walk('.'))[1]:
        print('\n'+Fore.CYAN+'/'+dir)
    print(Fore.WHITE+'\n<================================')

def deleteFolder(dirName):
    directory = f'{dirName}'
    parent = 'C:/Users/User/Desktop/Notes_App'
    path = os.path.join(parent, directory)
    os.rmdir(path)
    print(Fore.GREEN+f"\nDirectory '%s' has been removed successfully" %directory)
    mainFunction()

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
