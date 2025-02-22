import time  # Import the time module to create delay between each question, uses time.sleep()

#create a list of dictionaries
questions = [
    {
        'prompt': 'Which symbol is used for single-line comments in Python? ' ,
        'options': [ 'A. %' ,
                     'B. //' ,
                     'C. $' ,
                     'D. #'],
        'answer': 'D'
    },
    {
        'prompt': 'What does HTML stand for? ' ,
        'options': [ 'A. Hyperlink and Text Markup Language' ,
                     'B. High-Level Text Management Language' ,
                     'C. HyperText Markup Language' ,
                     'D. Home Tool Markup Language'],
        'answer': 'C'
    },
    {
        'prompt': 'What does “OOP” stand for in programming? ' ,
        'options': [ 'A. Object-Oriented Processing' ,
                     'B. Object-Oriented Programming' ,
                     'C. Optimal Object Protocol' ,
                     'D. Online Object Parsing'],
        'answer': 'B'
    },
    {
        'prompt': 'What is the main purpose of SQL? ',
        'options': ['A. Building web pages',
                    'B. Managing and querying databases',
                    'C. Writing operating systems',
                    'D. Controlling computer hardware'],
        'answer': 'B'
    },
    {
        'prompt': 'Which HTTP status code represents “Not Found”? ',
        'options': ['A. 404',
                    'B. 409',
                    'C. 444',
                    'D. 400'],
        'answer': 'A'
    }
]


score = 0
print("Welcome to my programming quiz!")

for question in questions:
        time.sleep(2)
        print("\n" + question['prompt'])

        for option in question['options']:
            print(option)

        choice = input('What is your chosen answer? ').upper()

        if choice == question['answer']:
            score += 1
            print('Correct! :D')


        else:
            print(f'Good try! The correct answer is {question["answer"]}')

if score >3:
    print(f"\nWell done! You got {score} questions correct :D!")

elif score ==3:
    print(f"\nNot bad! You got {score} questions correct!")

else:
    print(f"\nYour total score is {score}, better luck next time!")