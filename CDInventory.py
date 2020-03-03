#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
#joeprado, 2020-Mar-02, Reviewed Script
#joeprado, 2020-Mar-02, Replaced inner data with dictionaries
#joeprado, 2020-Mar-03, Added functionality of loading existing data
#joeprado, 2020-Mar-03, Added functionality to delete an entry
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = []  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object 

# Get user Input
print('The Magic CD Inventory')
while True:
    # 1. Display menu allowing the user to choose:
    print('\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # Exit the program if the user chooses so
        break
    if strChoice == 'l':
        #Load data from text file 
        lstTbl.clear()  #Clear lstTbl to duplicate entries don't get written to the table. 
        objFile = open(strFileName, 'r') # Open the file in read mode
        for row in objFile:  #Read each row from text file 
            lstRow = row.strip().split(',') #Format string in to list with comma as seperator
            dicRow = {'ID':lstRow[0], 'CD Title':lstRow[1], 'Artist':lstRow[2]} #create keys and values for dictionary
            lstTbl.append(dicRow) #Append dictionary to list
        objFile.close() #promptly close text file
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ') #Request ID from user
        strTitle = input('Enter the CD\'s Title: ') #Request CD Title from user
        strArtist = input('Enter the Artist\'s Name: ') # Request Artist Name from user. 
        intID = int(strID) #Convert user ID to integer
        dicRow = {'ID':intID, 'CD Title':strTitle, 'Artist':strArtist} # Pair keys and values to create dictionary
        lstTbl.append(dicRow) #Append dictionary to list. 
    elif strChoice == 'i':
        # Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist') 
        for row in lstTbl: #Unpack dictionaries from list
            print(*row.values(), sep = ', ') #Unpack items from dictionary; only print values, seperated by comma
    elif strChoice == 'd':
        #Delete an entry of the user's choosing
        print('ID, CD Title, Artist')
        for row in lstTbl:  #Display the current data. 
            print(*row.values(), sep = ', ') #Unpack items from dictionary; only print values, seperated by comma
        deleteChoose = int(input('Which ID would you like to delete?:  '))#  user select an ID to delete. 
        rowNbr = -1  # set counter variable
        for row in lstTbl: #unpack dictionaries from list
            rowNbr = rowNbr+1 #increase counter variable by 1
            if row['ID'] == deleteChoose: #Find row where value for ID matches row user wants to delete
                del lstTbl[rowNbr] # Delete that row. 
                break 
    elif strChoice == 's':
        # Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a') #Open text file
        for row in lstTbl: #Unpack dictionaries from list
            strRow = '' 
            for item in row.values(): # Unpack only values from dictionary 
                strRow += str(item) + ',' #Create string of dictionary value seperated items by comma
            strRow = strRow[:-1] + '\n' # Remove ending comma
            objFile.write(strRow) #Write string to text file
        objFile.close() #Close Text File
    else:
        print('Please choose either l, a, i, d, s or x!') #user winds up here if he/she doesn't type in an accepted option 

