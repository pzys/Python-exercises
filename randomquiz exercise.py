#page 322

import random
import os

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
try:
    os.mkdir('quizes')
except OSError as error:
    print(error)

for quizNum in range(35):
    quiz_name = 'quiz'+str(quizNum+1)+'.txt'
    quiz = open(os.path.join('quizes', quiz_name),'w')
    quiz_answers = open(os.path.join('quizes',quiz_name+"_answer"),'w')
    quiz_answers.write("Answers for the quiz: " + quiz_name + "\n")

    quiz.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quiz.write('\n\n')

    states = list(capitals.keys())
    capital_cities = list(capitals.values())
    random.shuffle(states)

    for i in range(len(states)):
        quiz.write("\n\n"+str(i+1)+". What is the capital of "+states[i]+"?")



        answers = [capitals[states[i]]]
        while len(answers)<4:
            wrong_answer = capital_cities[random.randint(0,49)]
            if wrong_answer not in answers:
                answers.append(wrong_answer)
        random.shuffle(answers)
        option ='ABCD'

        quiz_answers.write('\n'+str(i+1)+". "+option[answers.index(capitals[states[i]])])

        for j in range(len(answers)):
            quiz.write("\n"+" "*10+option[j]+'. '+answers[j])
            
quiz.close()
quiz_answers.close()

