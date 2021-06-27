import shutil
#shell utilities

#shutil.copy('C:\Users\pzysk\OneDrive\Pulpit\python','C:\Users\pzysk\OneDrive\Pulpit\python_copy')
#shutil.copy('smth/eggs.txt', 'eggs2.txt')

#for one file
#shutil.copy('smth\eggs.txt','smth2')

#for the entire folder shutil.copytree()
#shutil.copytree('smth','smth_backup')

#shutil.move('smth_backup','smth')

#os.unlink(path) - file
#os.rmdir(path) - empty folder
#os.rmtree(path) - folder with content

import os
for filename in os.listdir():
    if filename.endswith('.txt'):
     #os.unlink(filename)
     print(filename)

#-------------send2trash-----------------------trash bin
import send2trash
baconFile = open('bacon.txt', 'a') # creates the file
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('bacon.txt')
#won't be able to take the files out of the trash bin

import os

for folderName, subfolders, filenames in os.walk(os.getcwd()):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('smth hereh')

#---------------------ZIP FILE-------------------------
import zipfile

exampleZip = zipfile.ZipFile('organizing files.zip')
print(type(exampleZip))
print(exampleZip.namelist())

#exampleZip.extractall()
exampleZip.close()

newZip = zipfile.ZipFile('new.zip', 'w') #could be a
newZip.write('amth.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()