#!/usr/bin/env python
# Tom Lucciano

import sys
import os
from datetime import datetime

def cls():
	os.system(['clear','cls'][os.name == 'linux'])

def make_date_time(intime):
	#print("time: ", intime)
	convertTS = (datetime.fromtimestamp(int(intime)).strftime('%Y-%m-%d %H:%M:%S'))
	return convertTS


def getSBCList():

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

#############################################################
# function: printSBCList
# get the SBC that user wants to explore
#############################################################
def printSBCList(grpList):
	count=1
	choiceDict = {}
	for item in grpList:
		print("%d) %s " % (count,item))
		choiceDict[count] = item
		count=count+1

	for x,y in choiceDict.items():
		print(x,y)

	mychoice = input("SELECT SBC to view (by integer): ")
	#print(mychoice)
	if mychoice >= count or mychoice==0:
		print("That choice is not valid. Please choose an integer in range: ")
		for n in range(count):
			if n != 0:
				print(n),
		sys.exit(1)
	return choiceDict.get(mychoice)

#############################################################
# function: getGroupList
# List groups available in current directory
#############################################################
def getGroupList(sbc):
	print("sbc is: ", sbc)
	currDir = os.getcwd()
	print("cwd: ", currDir)
	dirPath=currDir + "/" + sbc
	print(dirPath)
	result = []
	filenames = os.listdir(dirPath) # get all files' and folders' names in the current directory
	# loop through all the files and folders
	for filename in filenames:
   	# check whether the current object is a folder or not
		#print(filename)
		if os.path.isdir(os.path.join(dirPath, filename)): 
			fullPath = dirPath + "/" + filename
			result.append(fullPath)


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

	#for x,y in choiceDict.items():
	#	print(x,y)

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
# Read system group
#############################################################
def printSystemGroup(systemDir):
	for filename in os.listdir(systemDir):
		if filename.endswith(".csv"):
			fullFilePath = os.path.join(systemDir,filename)
			#print("FILE: ", filename)
			#print("FULLPATH: ", fullFilePath)
			dFile = open(fullFilePath,"r")
			for aline in dFile:
				fields = aline.split(",")
				#print("FIELDS: ", fields)
				if fields[0] != "TimeStamp":
					cpu = fields[1]
					memutil = fields[2]
					health = fields[3]
					numsessions = fields[5]
					cps = fields[6]
					fTimeStamp=fields[0]
					#print("TIMESTAMP: ", fTimeStamp),
					convertTS = make_date_time(fTimeStamp)
					print("DATE TIME: ", convertTS),
					#print("FILE: ", fullFilePath)
					print("CPU: ",cpu),
					print("MEMORY UTIL: ", memutil),
					print("Sessions: ", numsessions),
					print("CPS: ",cps)
			dFile.close()

#############################################################
# read thru the directory files
#############################################################
def readDirFiles(myDir):
	if "system" in myDir:
		print("Directory files to read: ", myDir)
		printSystemGroup(myDir)


#############################################################
# function: main
#############################################################
def main():
	print("Check HDR data")
	currGroupList = []
	currSBCList = []
	currSBCList = getSBCList()
	sbcChoice = printSBCList(currSBCList)
	print("SBC CHOICE: ", sbcChoice)
	currGroupList = getGroupList(sbcChoice)
	groupChoice = printGroupList(currGroupList)
	print("you got: ", groupChoice)
	readDirFiles(groupChoice)

if __name__=='__main__':
	main()


