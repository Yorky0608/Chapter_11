import random as r

alien_color = ["green", 'yellow', 'red']
random_num = r.randint(0,2)

if alien_color[random_num] == 'green':
    print("Player earned 5 points!")
else:
    print("Player earned 10 points!")