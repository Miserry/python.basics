
num_of_numbers = int(input())

blank = []

for num in range(num_of_numbers):
    number = int(input())
    blank.append(number)

print(f'Max number: {max(blank)}')

print(f'Min number: {min(blank)}')