import os, sys

##########################################################################################################
##																										##
## This python script allows you to find all files of a certain file extension, ie .c, .py, .txt etc	##
## and move from one folder to another by specifying the following:										##
## python transfer.py <file extension> <source directory> <destination directory>						##
##																										##
##########################################################################################################

if len(sys.argv) < 4:
	print "\nFormat should be as follows: python transfer.py <file extension> <source directory> <destination directory>\n"

elif len(sys.argv) == 4:
		
	file_ext = sys.argv[1]
	source_dir = sys.argv[2]													#source directory to move files from
	destination_dir = sys.argv[3]												#destination directory to move files into

	x = os.listdir(source_dir)													#gets a list of all items in the source directory

	for element in x:
		print element
		if element.endswith(file_ext):
			os.rename(source_dir+"/%s"%element, destination_dir+"/%s"%element)	#moves the file from the source to destination directory
