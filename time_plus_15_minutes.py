
#Goal is to print out the hour input from the user and add 15 minutes to it.



hour_init = int(input('Enter hour: '))
minutes_init = int(input('Enter minutes: '))

add_min = 15
min = 60
hour = hour_init * min
tot_min = hour + minutes_init + add_min

end_hour = tot_min//60
end_min = tot_min%60

#Converting hour 24 to hour 0.
if end_hour > 23:
    end_hour = 0
#Adding a decimal place, when the minutes are simple digits ->
# if less than 10, it will look like "12:09", instead of "12:9".
if end_min<9:
    print(f'{end_hour}:0{end_min}')
else:
    print(f'{end_hour}:{end_min}')










