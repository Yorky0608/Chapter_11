usernames = ["Yorkshire06", "MyNsmes", "Popeletvt", "qwertyuiop[]", '1qaz2wsx', 'admin']

for user in usernames:
    if user == 'admin':
        print("Welcome admin, would you like to see the logs?")
    else:
        print(f"Hello {user}, nice to see you again.")