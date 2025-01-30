list = [1,2,3,4,5,6,7,8,9]

for num in list:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")

list2 = [f"{num}st" if num == 1 else f"{num}nd" if num == 2 else f"{num}rd" if num == 3 else f"{num}th" for num in list]
print(*list2)