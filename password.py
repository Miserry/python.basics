
username = input()
true_password = input()

try_password = input()
while try_password != true_password:
    try_password = input()

print(f'Welcome {username}!')

