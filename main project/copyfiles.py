import shutil
import os
source  = os.listdir("/media/alfred/Personal/main project/sample_input/")
dest = "/media/alfred/Personal/main project/out/"
for files in source:
	#if files.endswith(".txt"):
	#print (files)
	shutil.copy(source,dest)
