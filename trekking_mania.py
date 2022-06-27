
number_of_groups = int(input())
mousalla_climbers = 0
monblan_climbers = 0
kilimandjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0
total_climbers = 0

for current_group in range(number_of_groups):
    current_number_of_climbers = int(input())
    if current_number_of_climbers <= 5:
        mousalla_climbers += current_number_of_climbers
    elif current_number_of_climbers <= 12:
        monblan_climbers += current_number_of_climbers
    elif current_number_of_climbers <= 25:
        kilimandjaro_climbers += current_number_of_climbers
    elif current_number_of_climbers <= 40:
        k2_climbers += current_number_of_climbers
    else:
        everest_climbers += current_number_of_climbers
    total_climbers += current_number_of_climbers

mousalla_percent = mousalla_climbers / total_climbers * 100
monblan_percent = monblan_climbers / total_climbers * 100
kilimandjaro_percent = kilimandjaro_climbers / total_climbers * 100
k2_percent = k2_climbers / total_climbers * 100
everest_percent = everest_climbers / total_climbers * 100

print(f'{mousalla_percent:.2f}%')
print(f'{monblan_percent:.2f}%')
print(f'{kilimandjaro_percent:.2f}%')
print(f'{k2_percent:.2f}%')
print(f'{everest_percent:.2f}%')

