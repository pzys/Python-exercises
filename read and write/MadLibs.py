import re

sample = open('sample_text.txt')
sample_text = sample.read()
sample.close()

adjective = input('Enter an adjective: ')
noun = input('Enter a noun: ')
verb = input('Enter a verb: ')
noun2 = input('Enter a noun: ')

result = re.sub('ADJECTIVE', adjective, sample_text)
result = re.sub('NOUN', noun, result,1)
result = re.sub('VERB', verb, result)
result = re.sub('NOUN', noun2, result)

saved_file = open('changed_story.txt', 'w')
saved_file.write(result)
saved_file.close()