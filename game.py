from random import randint, choice
from animals import animals_question
from geography import geography_question
from movies import movies_question
from music import music_question


def game(name):

    score = 0
    tries = 3
    question_cat_num = '0'

    while question_cat_num not in '12345':
        question_cat_num = str(input('What category of question do you want to answer?\n'
                                     '1 - Geography\n'
                                     '2 - Animals\n'
                                     '3 - Music\n'
                                     '4 - Movies\n'
                                     '5 - Random\n'))
        if question_cat_num not in '12345':
            print('You must choose one of the listed options\n')

    while tries > 0:

        if question_cat_num == '1':
            question_cat = geography_question
        elif question_cat_num == '2':
            question_cat = animals_question
        elif question_cat_num == '3':
            question_cat = music_question
        elif question_cat_num == '4':
            question_cat = movies_question
        elif question_cat_num == '5':
            question_cat = choice([geography_question, animals_question, music_question, movies_question])

        rand_questions = list(question_cat)
        rand_answer = list(question_cat.values())
        question_number = randint(0, (len(rand_questions) - 1))

        print(rand_questions[question_number])
        guess = input(str('\nWhat is your guess?\n'))

        while guess not in 'abcd':
            print('You should guess "a", "b", "c" or "d"')
            guess = input(str('What is your guess?\n'))

        if guess == rand_answer[question_number]:
            print('You got it!')
            score += 1
            tries -= 1
        else:
            print('Oh no! You got it wrong...')
            tries -= 1

        question_cat.pop(f'{rand_questions[question_number]}')

        if tries == 0:
            return score
        else:
            print(f'\nYou have {tries} more questions to answer')
            print(f'Your current score is {score}\n')
