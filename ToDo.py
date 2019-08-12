# -------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  8/10/2019
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   Vid, 8/10/19, Added code to complete assignment 5
# https://www.tutorialspoint.com/python/python_dictionary.htm
# -------------------------------------------------#

# -- Data --#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

objFileName = "C:\_PythonClass\Assignment05\Todo.txt"
strData = ""
dicRow = {}
lstTable = []
RowCount = 0

# -- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

# -- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program
# -------------------------------

# Step 1 - Load data from a file
# When the program starts, load each "row" of data
# in "ToDo.txt" into a python Dictionary.
# Add the each dictionary "row" to a python list "table"
FileRead = open(objFileName, "r")
for x in FileRead:
    task, priority = x.strip().split(",")
    dicRow[task.strip()] = priority.strip()
    lstTable.append(x.rstrip('\n'))

# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()  # adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        print(lstTable)
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        newTask = str(input("Please type out the next task here: "))
        newPriority = str(input("Please type out the priority of that task here: "))
        newItem = newTask + "," + newPriority
        lstTable.append(newItem)
        RowCount +=1
        print("The task list now is \n", lstTable)
        continue

    # Step 5 - Remove a new item to the list/Table
    elif (strChoice == '3'):
        DelDic = {}
        for y in lstTable:
            task, priority = y.strip().split(",")
            DelDic[task.strip()] = priority.strip()
        try:
            RemoveType = str(input("Enter name of task that you want to delete"))
            DelDic.pop(RemoveType)
            NewList = []
            for task in DelDic:
                NewItems = task + "," + DelDic[task]
                NewList.append(NewItems)
            lstTable=NewList
        except:
            print("Can only remove a task that exists. Please check entry for accuracy incl. case sensitivity")
        continue

    # Step 6 - Save tasks to the ToDo.txt file
    elif (strChoice == '4'):
        FileRead = open(objFileName, "w")
        for Item in lstTable:
            FileRead.write(Item)
            FileRead.write("\n")
        FileRead.close()
        continue
    elif (strChoice == '5'):
        break  # and Exit the program
