#!/usr/bin/env python


import os

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

def printGroupList(grpList):
	count=1
	for item in grpList:
		print("%d) %s " % (count,item))
		count=count+1

def main():
	print("Check HDR data")
	currGroupList = []
	currGroupList = getGroupList()
	printGroupList(currGroupList)

if __name__=='__main__':
	main()
