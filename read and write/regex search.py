import os
import re

files = os.listdir()
name = 'changed_story.txt'

txt_files = []
for file in files:
    if file[-4:] == '.txt':
        txt_files.append(file)

searched_phrase = input('Searched phrase: ')
searched_regex = re.compile(searched_phrase)

for txt in txt_files:
    file = open(txt)
    file_content = file.readlines()
    for line in file_content:
        if(len(re.findall(searched_regex,line))!=0):
            print(line)
    file.close()


