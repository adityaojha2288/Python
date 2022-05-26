from number_game_art import logo
import random
print(logo)
print("Welcome to the number guessing game!")
print("I am thinking a number between 1 to 100")
a =input("Choose Difficulty: Type 'Easy' or 'Hard': ")
numbers = []
for i in range(1,101):
    numbers.append(i)
guess = random.choice(numbers)
if a.lower() == 'easy':
    attempts = 10
elif a.lower() =='hard':
    attempts = 10
else:
    print("Type the correct option")
for j in range(attempts+1):
    ans= int(input("Make a guess:"))
    if ans ==guess:
        print(f'You Got it! The ans is {ans}')
        break
    elif ans > guess:
        print('Too high')
        print('Guess again')
        attempts -=1
        
    elif ans < guess:
        print('Too low')
        print('Guess again')
        attempts-=1
    if attempts == 0:
        print("You have failed try again!")
        break

