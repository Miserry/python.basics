
n = int(input())

sum1 = 0
sum2 = 0

for num in range(n):
    n1 = int(input())
    sum1 += n1
for num2 in range(n):
    n2 = int(input())
    sum2 += n2

difference = abs(sum1 - sum2)

if sum1 == sum2:
    print(f'Yes, sum = {sum1}')
else:
    print(f'No, diff = {difference}')