## First the user's input is telling us how many numbers he is going to enter.
## Then he is actually entering his numbers and we have to calculate the sum of those.

n_of_numbers = int(input('How many numbers are coming?: '))
sum_of_the_numbers = 0

for i in range(1, n_of_numbers + 1):
    num = int(input('Enter your next number: '))
    sum_of_the_numbers += num
print(sum_of_the_numbers)