import os
import shutil

path = input('Enter the path you want to sort : ') # taking the path of the directory from the user
files = os.listdir(path) # retrieving all the file names in the form of list

for file in files:
    name, extn = os.path.splitext(file) # separating the name and the extension of the file
    extn = extn[1:] # removing the '.' from the extension
    if os.path.exists(path + '/' + extn):
        shutil.move(path + '/' + file, path + '/' + extn + '/' + file) # pushing the file to its respective directory named after its extension is the path exists
    else:
        os.makedirs(path + '/' + extn)
        shutil.move(path + '/' + file, path + '/' + extn) # if the directory doesn't exist then make a directory the push in the file

# note: os.makedirs() is required as it creates all the intermediate directories if they don't exist (just like mkdir -p in bash).

# but os.mkdir can't be used as can create a single sub-directory, and will throw an exception if intermediate directories that don't exist are specified.

