import random as r

alien_color = ["green", 'yellow', 'red']
color = alien_color[r.randint(0,2)]

if color == 'green':
    print("Player earned 5 points!")
elif color == 'yellow':
    print("Player earned 10 points!")
elif color == 'red':
    print("Player earned 15 points!")