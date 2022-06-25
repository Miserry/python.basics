
n = int(input())

odd = 0
even = 0

for i in range(n):
    num = int(input())
    if i%2 == 0:
        odd += num
    else:
        even += num

difference = abs(odd-even)
if odd == even:
    print(f'''Yes
Sum = {odd}
''')
else:
    print(f'''No
Diff = {difference}
''')


