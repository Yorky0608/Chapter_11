test = "Yes"

print("Does test.lower() == yes? I think True")
print(test.lower() == 'yes')

print("Does test.lower() == Yes? I think False")
print(test.lower() == 'Yes')

fruit = 'apple'

print("Does fruit == 'apple'? I think True")
print(fruit == 'apple')

print("Does fruit == 'pinapple'? I think False")
print(fruit == 'pinapple')

test = 20

print("Does test == 20? I think True")
print(test == 20)

print("Does test == '20'? I think False")
print(test == 00)

print("Does test > 20? I think True")
print(test > 20)

print("Does test < '20'? I think False")
print(test < 00)

print("Does test >= 20? I think True")
print(test >= 20)

print("Does test <= '20'? I think False")
print(test <= 00)

print("Does test == 20 and test == int('20')? I think True")
print(test == 20 and test == int('20'))

print("Does test == 20 and test == '00'? I think False")
print(test == 20 and  test == '00')

print("Does test == 20 or test == int('20')? I think True")
print(test == 20 or test == int('20'))

print("Does test == 20 or test == '00'? I think False")
print(test == 20 or  test == '00')

list = ["Carl", "Pearl", "Ivy"]
person = "Carl"

if person in list:
    print(f"{person} was in the list.")

if person not in list:
    print(f"{person} was not in the list.")