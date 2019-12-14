import os
import datetime
from colorama import Fore, Back, Style, init


init(autoreset=False)
actionsArray = ['create','write','delete', 'read', 'exit']
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
        text = str(input(Fore.YELLOW + 'What is your message: '))
        writeToFile(fileNam, text)
    elif action == actionsArray[2]: # If deleting a file
        chckDirectory()
        print(Fore.YELLOW)
        fileNam = str(input('Give a filename: ')).lower().strip()
        deleteFile(fileNam)
    elif action == actionsArray[3]: # If reading a file
        chckDirectory()
        print(Fore.YELLOW)
        fileNam = str(input('Give a filename: ')).lower().strip()
        print(Style.RESET_ALL)
        readFile(fileNam)
    elif action == actionsArray[4]: # If exiting the program
        print(Fore.LIGHTBLUE_EX + '\nYou are exiting the program.')
        print(exit())
    else:
        print('\nCommand does not exist.') # Command not found
        mainFunction()


# ----------------- List out existing files ------------------
def chckDirectory(): # Checking directory for text files
    print(Style.RESET_ALL)
    print(Fore.YELLOW + '\nChoose from files:')
    for file in os.listdir("C:/Users/User/Desktop/Notes_App/notes_folder"):
        if file.endswith('.txt'):
            print(Fore.WHITE + f'{file}')
    print('\n')
        

# ----------------- (App Actions) Functions -----------------
def createFile(fileName):
    print(Style.RESET_ALL)
    open(f'./notes_folder/{fileName}.txt','w')
    print(Fore.GREEN + f'\n{fileName}.txt was created...')
    mainFunction()

def readFile(fileName):
    print(Style.RESET_ALL)
    rf = open(f'./notes_folder/{fileName}.txt', 'r')
    print(Fore.GREEN + f'{rf.read()}')
    print(Style.RESET_ALL)
    rf.close()
    mainFunction()


def writeToFile(file, text):
    print(Style.RESET_ALL)
    NewEntryHeader = datetime.datetime.today()
    wf = open(f'./notes_folder/{file}.txt', 'a')
    wf.write(f'\n{NewEntryHeader}: \n{text}')
    print(Fore.CYAN + '\nYou wrote:')
    print(Style.RESET_ALL)
    print(Back.CYAN + Fore.BLACK + f'\n{text}')
    print(Style.RESET_ALL)
    print(Fore.CYAN + f'\nTo {file}.txt')
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
    print(Fore.YELLOW + 'Example Commands: (create/write/delete/exit/read)')
    action = str(input('Input your action: ')).lower().strip()
    # decide what file we're going to do what with
    assignAction(action)
        


mainFunction()
