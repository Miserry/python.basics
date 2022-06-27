
number_of_tournaments = int(input())
current_points = int(input())
pts_won = 0
tours_won = 0

for tour in range(number_of_tournaments):
    place = input()
    if place == 'W':
        pts_won += 2000
        tours_won += 1
    elif place == 'F':
        pts_won += 1200
    elif place == 'SF':
        pts_won += 720

tot_points = current_points + pts_won
avg_points_won = int((tot_points - current_points)  / number_of_tournaments)
won_percent = tours_won / number_of_tournaments * 100

print(f'Final points: {tot_points}')
print(f'Average points: {avg_points_won}')
print(f'{won_percent:.2f}%')
