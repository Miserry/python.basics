
actor = input()
points_tot = float(input())
num_jury = int(input())

for num in range(num_jury):
    name_jury = input()
    pts_jury = float(input())
    grade = len(name_jury) * pts_jury / 2
    points_tot += grade
    if points_tot > 1250.5:
        print(f'Congratulations, {actor} got a nominee for leading role with {points_tot:.1f}!')
        break

diff = abs(points_tot - 1250.5)
if points_tot <= 1250.5:
    print(f'Sorry, {actor} you need {diff:.1f} more!')





