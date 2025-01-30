current_users = ["Yorky", "Gracia", "Paris", "Conno", "Chabbs"]
new_users = ["Jackson", "Jaxson", "Sam", "Paris", "Chabbs"]


for new_user in new_users:
    count = 0
    for old_user in current_users:
        if new_user == old_user or new_user.upper() == old_user or new_user.lower() == old_user or new_user.title() == old_user:
            print(f"Please make another username. {old_user} is already in use.")
            count += 1
    if count != 1:
        print(f"{new_user} is available to use.")
            #Not finished yet