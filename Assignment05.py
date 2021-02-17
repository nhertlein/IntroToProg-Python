# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# NHertlein,2.13.2021,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
FILE = 'ToDoList.txt'  # Constant string containing file name
PATH = 'C:\\_PythonClass\\Assignment05\\'  # Constant string containing file path
objFile = None  # An object that represents a file
strData = ''  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = """
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """  # A menu of user options
strChoice = ''  # A Capture the user option selection
intRowCount = 0  # Initial counter value

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(PATH + FILE, 'r')
for objRow in objFile:
    strData = objRow.split(',')
    dicRow = {'Task': strData[0], 'Priority': strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print(strMenu)
    strChoice = str(input('Which option would you like to perform? [1 to 5] - '))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print('Current list contents:')

        for objRow in lstTable:
            print(objRow['Task'] + ',' + str(objRow['Priority']))  # Prints single line no newline character
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        print('Make a new list entry:')
        strTask = input('Task: ')
        strTask = strTask[0].upper() + strTask[1:].lower()  # Playing with formatting
        while True:
            try:
                strPriority = input('Priority: ')
                intPriority = int(strPriority)
                break
            except:
                print('Priority must be an integer. Try again.')

        dicRow = {'Task': strTask, 'Priority': intPriority}
        lstTable.append(dicRow)

        print('The task', strTask, 'was saved to the list.')
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        while True:
            print('Enter a task to remove from the list: ')
            strTask = input('Remove Task: ').lower()

            intLstLen = len(lstTable)  # Get initial list length to compare to
            for objRow in lstTable:
                if strTask in objRow['Task'].lower():
                    del lstTable[intRowCount]
                    break  # Exit for loop
                else:
                    intRowCount += 1  # Increase counter to get row index

            if intRowCount == intLstLen:
                print(strTask, 'is not found in the list. Try again. \n')
                intRowCount = 0  # Reset counter
            else:
                break  # Exit while loop

        print(strTask, 'was removed from the list.')
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(PATH + FILE, 'w')
        for objRow in lstTable:
            objFile.write(objRow['Task'] + ',' + str(objRow['Priority']) + '\n')

        objFile.close()

        print(FILE, 'saved to directory', PATH)
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print('Exiting program.')
        break  # and Exit the program
