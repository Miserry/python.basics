
##Here we need to calculate the sum of the vowels_points from the input,
##with the following conditions.

# a = 1
# e = 2
# i = 3
# o = 4
# u = 5

txt_input = input('Enter your word here: ')
sum = 0
for z in txt_input:

    if z == 'a':
        sum += 1
    elif z == 'e':
        sum += 2
    elif z == 'i':
        sum += 3
    elif z == 'o':
        sum += 4
    elif z == 'u':
        sum += 5

print(sum)









