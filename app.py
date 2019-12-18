import os
from datetime import datetime
from colorama import Fore, Back, Style, init
import fileinput


init(autoreset=False)
actionsArray = ['/crtfile','/writeto', '/rdfrom', '/updtentry', '/dltfile','/commands', '/exit']
fileList = os.listdir('C:/Users/User/Desktop/Notes_App/notes_folder')[:]

# ----------------- Assigning Function based on user input -----------------
def assignAction(action):
    if action == actionsArray[0]: # If Create a File
        print(Fore.YELLOW)
        fileNam = str(input('Give a filename: ')).lower().strip()
        createFile(fileNam)
    elif action == actionsArray[1]: # If writing to
        chckDirectory()
        print(Fore.YELLOW)
        fileNam = str(input('Give a filename: ')).lower().strip()
        fileMatchList(fileNam)
        print(Fore.YELLOW)
        text = str(input('What is your message: '))
        text = 'Entry: ' + text
        if fileNam.endswith('.txt'):
            fileNam = fileNam[:-4]
        writeToFile(fileNam, text)
    elif action == actionsArray[2]: # If reading a file
        chckDirectory()
        print(Fore.YELLOW)
        fileNam = str(input('Give a filename: ')).lower().strip()
        fileMatchList(fileNam)
        print(Style.RESET_ALL)
        readFile(fileNam)
    elif action == actionsArray[3]:
        chckDirectory()
        print(Fore.YELLOW)
        fileNam = str(input('Give a filename: ')).lower().strip()
        fileMatchList(fileNam)
        updateFileEntry(fileNam)
    elif action == actionsArray[4]: # If deleting a file
        chckDirectory()
        print(Fore.YELLOW)
        fileNam = str(input('Give a filename: ')).lower().strip()
        fileMatchList(fileNam)
        deleteFile(fileNam)
    elif action == actionsArray[5]:
        print(Fore.YELLOW)
        print('Commands Available: ')
        for cmd in actionsArray[:]:
            print(Fore.CYAN)
            print(cmd)
        mainFunction()
    elif action == actionsArray[6]: # If exiting the program
        print(Fore.LIGHTBLUE_EX + '\nYou are exiting the program.')
        print(exit())
    else:
        print(Fore.LIGHTMAGENTA_EX+'\nCommand does not exist.') # Command not found
        mainFunction()

# ----------------- List out existing files ------------------
def chckDirectory(): # Checking directory for text files
    print(Style.RESET_ALL)
    print(Fore.YELLOW + '\nChoose from files:')
    for file in os.listdir("C:/Users/User/Desktop/Notes_App/notes_folder/"):
        if file.endswith('.txt'):
            print(Fore.WHITE + f'{file}')
    print('\n')

def fileMatchList(zfile):
    if zfile != zfile.endswith('.txt'):
        zfile = zfile + '.txt'
    print(Fore.WHITE+zfile)
    if zfile not in fileList:
        print(Fore.RED+'File was not found.')
        mainFunction()
    else:
        print(Fore.GREEN+'File was correctly selected.')

        
# ----------------- (App Actions) Functions -----------------
def createFile(fileName):
    print(Style.RESET_ALL)
    open(f'./notes_folder/{fileName}.txt','w')
    print(Fore.GREEN + f'\n{fileName}.txt was created...')
    mainFunction()

def readFile(fileName):
    print(Style.RESET_ALL)
    rf = open(f'./notes_folder/{fileName}.txt', 'r')
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


def writeToFile(file, text):
    rf = open(f'./notes_folder/{file}.txt', 'r')
    rf = rf.readlines()
    if rf == []:
        print(Style.RESET_ALL)
        NewEntryHeader = datetime.today().date()
        wf = open(f'./notes_folder/{file}.txt', 'a')
        wf.write(f'{NewEntryHeader}: \n{text}')
        print(Fore.BLUE + '\nYou wrote:')
        print(Fore.CYAN + f'\n{text}')
        print(Fore.BLUE + f'\nTo {file}.txt')
        wf.close()
    else:
        print(Style.RESET_ALL)
        NewEntryHeader = datetime.today().date()
        wf = open(f'./notes_folder/{file}.txt', 'a')
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

# ----------------- give action to assign function -----------------
# Decide What you would like to do
def mainFunction():
    print(Style.RESET_ALL)
    print(Fore.YELLOW + 'What would you like to do?')
    print(Fore.YELLOW + 'Example Commands: /crtfile /writeto /commands /exit')
    print(Fore.WHITE)
    action = str(input('Input your action: ')).lower().strip()
    # decide what file we're going to do what with
    assignAction(action)  

mainFunction()
