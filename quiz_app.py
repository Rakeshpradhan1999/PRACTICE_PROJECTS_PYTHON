print('Hi, welcome to the quiz game.')

confirmation = input('Would you like to play or quit the game? ')

if (confirmation.lower() != 'yes'):
    quit()

print('Let\'s play!')


class QuestionAnswer():
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


firstQs = QuestionAnswer('What does CPU stands for? ',
                         'Central processing unit')
secondQs = QuestionAnswer('What does RAM stands for? ', 'Random access memory')
allQuestions = [firstQs, secondQs]

score = 0
for qs in allQuestions:
    print('Q', qs.question)
    ans = input('Ans. ')
    if (ans.lower() == qs.answer.lower()):
        print('Correct!')
        score += 1
    else:
        print('Wrong answer!')

print(f'You got {score} out of {len(allQuestions)}')
print(f'You got {(score / len(allQuestions)) *100}% ')
