import shelve
import os

files = os.listdir(os.getcwd())
print(files)

shelfFile = shelve.open('mydata')
print(type(shelfFile))
shelfFile['cats']
print(list(shelfFile.keys()))
shelfFile.close()