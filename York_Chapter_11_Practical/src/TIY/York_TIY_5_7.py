import random as r

fruit_list = ['apple', 'pineapple', 'pear', 'orange', 'banana', 'plum']
fruit = fruit_list[r.randint(0,5)]

if 'apple' in fruit_list:
    print("There is an apple in the list.")
else:
    print("There is no apple in the list.")

if 'apple' in fruit_list:
    print("There is an apple in the list.")
if 'grape' in fruit_list:
    print("There is an grape in the list.")
if 'orange' in fruit_list:
    print("There is an orange in the list.")

if 'apple' == fruit:
    print("There is an apple in the list.")
elif 'pineapple' == fruit:
    print("There is an pineapple in the list.")
elif 'pear' == fruit:
    print("There is an pear in the list.")
elif 'banana' == fruit:
    print("There is an banana in the list.")
elif 'orange' == fruit:
    print("There is an orange in the list.")
elif 'plum' == fruit:
    print("There is an plum in the list.")
else:
    print(f"There is no {fruit} in this list")