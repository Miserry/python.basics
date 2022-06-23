##If you want a typical clock, just enter (24) in the first range
## and (60) in the second range.

# for hour in range(9,11):
#     for minutes in range(0,15):
#         if hour < 10 and minutes < 10:
#             print(f'0{hour}:0{minutes}')
#         elif hour < 10:
#             print(f'0{hour}:{minutes}')
#         elif hour >= 10 and minutes >= 10:
#             print(f'{hour}:{minutes}')


##And now what i have learned today...
## The simplified version of the code above is formatting with '02d'.

for hour in range(9,11):
    for minutes in range(0,15):
        print(f'{hour:02d}:{minutes:02d}')