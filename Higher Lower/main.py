from Game_art import *
from game_data import data
import random
p1 = random.randint(0, len(data))
name1 = data[p1]['name']
descp1 = data[p1]['description']
c1 = data[p1]['country']
f1 = data[p1]['follower_count']
score = 0
print(p1)
for i in range(0, 100):
    name1 = data[p1]['name']
    descp1 = data[p1]['description']
    c1 = data[p1]['country']
    f1 = data[p1]['follower_count']
    p2 = random.randint(0, len(data))
    print(logo)
    print(f"Compare A :{name1}, a {descp1} from {c1}")
    print(vs)
    print(
        f"Against B :{data[p2]['name']}, a {data[p2]['description']} from {data[p2]['country']}")
    ans = input("Who has More Followers A or B: ")
    if ans == 'a':
        if f1 > data[p2]['follower_count']:
            score += 1
            print(f'You Won. Your Current Score is {score}')
            p1 =p2
            print(p1)
        elif f1< data[p2]['follower_count']:
            print(f"You Lose!Your Current Score is {score}")
            break
    elif ans == 'b':
        if f1 > data[p2]['follower_count']:
            print(f'You Lose!.Your Current Score is {score}')
            break
        elif f1 < data[p2]['follower_count']:
            score += 1
            print(f"You Won!..Your Current Score is {score}")
            p1 = p2
