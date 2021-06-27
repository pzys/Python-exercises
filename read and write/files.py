#automate the boring stuff with python
# chapter 8 - reading and writing

import os

print(os.path.join('usr','bin','spam'))
print(os.getcwd())

print(os.chdir(r'/'))
print(os.getcwd())

#os.makedirs('new_folder')

#308

path = 'C:\\Windows\\System32\\calc.exe'
os.path.basename(path)
os.path.dirname(path)
os.path.split(path)
print(path.split(os.path.sep))

os.path.getsize(path)
print(os.listdir(os.getcwd()))

os.path.exists(path)
os.path.isfile(path)
os.path.isdir(path)

##files
somefile = open('somefile.txt')
somefile_content_whole = somefile.read()
print(somefile_content_whole)
print('\nsome additional lines')
somefile.close()

somefile = open('somefile.txt', 'r') #r - reading as default
somefile_content_line = somefile.readlines()
print(somefile_content_line)
somefile.close()

somefile = open('somefile.txt', 'a') #a for append, w - for overwriting
somefile.write('\nbacon is holy')

# saving variables with shelve Module

import shelve
shelfFile = shelve.open('mydata')
cats = ['Tom','Cherry','Beni']
shelfFile['cats'] = cats
shelfFile.close()

#------------------

import pprint

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc':
'fluffy'}]

fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

print(type(pprint.pformat(cats)))