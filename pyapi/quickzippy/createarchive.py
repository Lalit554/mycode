#!/usr/bin/env python3
import os
import zipfile

def zipdir(path, ziph): # function to search for all files within a directory, and add them to our ZIP
  for root, dirs, files in os.walk(path):
    for file in files:
      print(os.path.join(root,file))
      ziph.write(os.path.join(root, file)) ## adds files to our zipfileobject that was passed in

dir2zip = input("What directory are we archiving today? ")

  ## If the directory exists, then we can begin archiving it
if os.path.isdir(dir2zip):
  zippedfn = input("What should we call the finished archive? ") 
  ## zippedfn is the zipped file for the archive
  zipfileobj = zipfile.ZipFile(zippedfn, "w", zipfile.ZIP_DEFLATED) 
  # create a zip file object -- we are making a new zip file
  zipdir(dir2zip, zipfileobj) # call to our function
  zipfileobj.close()  ## This closes our archive - IMPORTANT!
else:
  print("Run the script again when you have a valid directory to zip.")

