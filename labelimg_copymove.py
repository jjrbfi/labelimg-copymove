#!/usr/bin/python3

import os, sys, fnmatch

action = sys.argv[1]
work_directory = sys.argv[2]
destination = sys.argv[3]

def organizate(xy):

	for file_name in os.listdir(work_directory):
		if file_name.endswith((".jpg")):
			file_txt = os.path.splitext(file_name)[0]+".txt" # Split the file extension from the main file and add .txt
			if (os.path.isfile(work_directory + file_txt)): # If the main file with the .txt extension is in the work_directory then...
				os.system(xy + " " + work_directory + file_name + " " + destination) # Copying the file with the .jpg extension
				os.system(xy + " " + work_directory + file_txt + " " + destination)  # Copying the file with the .txt extension

	os.system(xy + " " + work_directory +"classes.txt " + destination) # Adding the classes.txt file into the destination directory
	print("Done! :)")

if action == "-m":
	organizate("mv")
elif action == "-c":
	organizate("cp")
else:
	print("The options are:\n -c  copy\n -m  move")
