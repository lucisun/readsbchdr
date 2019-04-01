#!/usr/bin/env python
# Tom Lucciano

import sys
import os

#############################################################
# function: getGroupList
# List groups available in current directory
#############################################################
def getGroupList():

	filenames= os.listdir (".") # get all files' and folders' names in the current directory
	result = []
	# loop through all the files and folders
	for filename in filenames:
   	# check whether the current object is a folder or not
		if os.path.isdir(os.path.join(os.path.abspath("."), filename)): 
			result.append(filename)

	result.sort()
	#print(result)
	return result

	#To save Folder names to a file.
	#f= open('list.txt','w')
	#for index,filename in enumerate(result):
    #	f.write("%s. %s \n"%(index,filename))

	#f.close()

#############################################################
# function: printGroupList
# get the group that user wants to explore
#############################################################
def printGroupList(grpList):
	count=1
	choiceDict = {}
	for item in grpList:
		print("%d) %s " % (count,item))
		choiceDict[count] = item
		count=count+1

	for x,y in choiceDict.items():
		print(x,y)

	mychoice = input("SELECT Group to view (by integer): ")
	#print(mychoice)
	if mychoice > count:
		print("That choice is not valid. Please choose an integer in range: ")
		for n in range(count):
			if n != 0:
				print(n),
		sys.exit(1)
	return choiceDict.get(mychoice)


#############################################################
# function: main
#############################################################
def main():
	print("Check HDR data")
	currGroupList = []
	currGroupList = getGroupList()
	groupChoice = printGroupList(currGroupList)
	#print("you got: ", groupChoice)


if __name__=='__main__':
	main()
