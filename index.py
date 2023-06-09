print('welcome to my car quiz!') 

play = input('Do you want to play it? ')

if play == "no": # see how to add n or N 
    quit()
else:
    print("let's begin!!! ")  

score = 0    


answer= input('how many cylinders does a Buggati Chiron have? ')  
if answer==  '16':
    print('correct')
    score += 1
else:
    print('incorrect, the answer is 16')


answer= input('what is the horsepower of Buggati Chiron? ')  
if answer==  '1500':
    print('correct')
    score += 1
else:
    print('incorrect, the answer is 1500')


answer= input('how many turbos does a Buggati Chiron have? ')  
if answer==  '4':
    print('correct')
    score += 1 
else:
    print('incorrect, the answer is 4')

answer=input('who owns Buggati? ')
if answer.lower()== 'volkswagen':
    print('correct')
    score += 1
else:
    print('incorrect, the answer is volkswagen')

print("You got " + str(score) + " questions correct")
print("Your score is " + str(score / 4 * 100) + "%")
print("Thank You for playing :) ")
