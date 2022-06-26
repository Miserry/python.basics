
num_tabs = int(input())
salary = int(input())

salary_cut = 0

for tab in range(num_tabs):
    website = input()
    if website == 'Facebook':
        salary -= 150
    elif website == 'Instagram':
        salary -= 100
    elif website == 'Reddit':
        salary -= 50

    if salary <= 0:
        print(f'You have lost your salary.')
        break
    elif tab == num_tabs -1:
        print(f'{salary}')




