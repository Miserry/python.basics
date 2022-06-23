
first_time = int(input('Enter: '))
second_time = int(input('Enter: '))
third_time = int(input('Enter: '))

total = first_time + second_time + third_time

minutes = total // 60

time = total%60

if time <= 9:
    print(f'{minutes}:0{time}')
else:
    print(f'{minutes}:{time}')