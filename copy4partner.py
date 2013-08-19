#!/usr/bin/python

# All of them imports
import os, easygui as eg, errno
from shutil import copytree, ignore_patterns

# Create a list (extList) of all the file extensions found in the source directory
def getFileExtList (dirPath, uniq=True,sorted=True):
	extList=list()
	for dirpath, dirnames, filenames in os.walk(dirPath):
		for file in filenames:
			fileExt=os.path.splitext(file)[-1]
			extList.append(fileExt)
			
	if uniq:
		extList=list(set(extList))
	if sorted:
		extList.sort()
	return extList

# Open a window to choose the location copying from
source_dir = eg.diropenbox(title='Choose Source Directory')

# allFileTypes is the list of all extensions in source_dir
# grabbed with function getFileExtList
allFileTypes = getFileExtList(source_dir)
# delete the blank file type
del allFileTypes[0]

# Open a window to choose the files to copy
copyList = eg.multchoicebox(msg='Select the file types to copy',
							choices=(allFileTypes))

# List comprehension adds the asterisk for glob
# while making an ignore list for copytree
ignoreList = [x for x in allFileTypes if x not in copyList]
print ignoreList
	

# Open a window to choose the destination directory
root_dir = eg.diropenbox(title='Choose Destination Directory')

dest_dir = os.path.join(root_dir, os.path.basename(source_dir))

# copytree everything from the source_dir to the dest_dir ignoring
# all files types not chosen from the list
copytree(source_dir, dest_dir, ignore=ignore_patterns(*ignoreList))