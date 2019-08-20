#-------------------------------------------------#
# Title: Working with Classes & objects
# Dev:   Vid
# Date:  Aug 17, 2019
# ChangeLog: (Who, When, What)
#   RRoot, 09/16/2017, Created Script
#   Vid,   08/18/2019, Modified with classes
#-------------------------------------------------#

#-- Data --#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

#-- Processing --#
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
# Execute program

# Step 8
# Exit program
#-------------------------------1


class ToDo(object):
    objFileName = "C:\_PythonClass\Assignment06\Todo.txt"
    strData = ""
    dicRow = {}
    lstTable = []
    strChoice = ""

    def read_file(self):
        # Step 1
        # When the program starts, load the any data you have
        # in a text file called ToDo.txt into a python Dictionary.
        objFile = open(ToDo.objFileName, "r")
        for line in objFile:
            ToDo.strData = line.split(",")  # readline() reads a line of the data into 2 elements
            ToDo.dicRow = {"Task": ToDo.strData[0].strip(), "Priority": ToDo.strData[1].strip()}
            ToDo.lstTable.append(ToDo.dicRow)
        objFile.close()

    def display_menu(self):
        # Step 2
        # Display a menu of choices to the user
        #while (True):
        print("""
        Menu of Options
        1) Show current data
        2) Add a new item.
        3) Remove an existing item.
        4) Save Data to File
        5) Exit Program
        """)

    def display_items(self):
        # Step 3
        # Show the current items in the table
        print("******* The current items ToDo are: *******")
        for row in ToDo.lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")

    def add_items(self):
    # Step 4
    # Add a new item to the list/Table
        strTask = str(input("What is the task? - ")).strip()
        strPriority = str(input("What is the priority? [high|low] - ")).strip()
        ToDo.dicRow = {"Task":strTask,"Priority":strPriority}
        ToDo.lstTable.append(ToDo.dicRow)
        print("Current Data in table:")
        for ToDo.dicRow in ToDo.lstTable:
            print(ToDo.dicRow)
        # 4a Show the current items in the table
        ToDo.display_items(self)
        return(ToDo.lstTable)

    def remove_items(self):
        # Step 5
        # Remove a new item to the list/Table
        #5a-Allow user to indicate which row to delete
        strKeyToRemove = input("Which TASK would you like removed? - ")
        blnItemRemoved = False #Creating a boolean Flag
        intRowNumber = 0
        while(intRowNumber < len(ToDo.lstTable)):
            if(strKeyToRemove == str(list(dict(ToDo.lstTable[intRowNumber]).values())[0])): #the values function creates a list!
                del ToDo.lstTable[intRowNumber]
                blnItemRemoved = True
            #end if
            intRowNumber += 1
        #end for loop
        #5b-Update user on the status
        if(blnItemRemoved == True):
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")

        #5c Show the current items in the table
        print("******* The current items ToDo are: *******")
        ToDo.display_items(self)

    def save_to_list(self):
        # Step 6
        # Save tasks to the ToDo.txt file
        #5a Show the current items in the table
        ToDo.display_items(self)
        #5b Ask if they want save that data
        if("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):
            objFile = open(ToDo.objFileName, "w")
            for ToDo.dicRow in ToDo.lstTable:
                objFile.write(ToDo.dicRow["Task"] + "," + ToDo.dicRow["Priority"] + "\n")
            objFile.close()
            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")

# Step 7 execute the program

d = ToDo()
d.read_file()
d.display_menu()
#d.reset_to_menu()

while(True):
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()  # adding a new line
    if (strChoice.strip() == '1'):
        d.display_items()
        d.display_menu()
        continue
    elif (strChoice.strip() == '2'):
        d.add_items()
        d.display_menu()
        continue
    elif (strChoice == '3'):
        d.remove_items()
        d.display_menu()
        continue
    elif (strChoice == '4'):
        d.save_to_list()
        d.display_menu()
        continue
    elif (strChoice == '5'):
        print("Goodbye")
        break