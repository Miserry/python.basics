player_name = input()
starting_points = 301
counter_success = 0
counter_unsuccess = 0
single = 1
double = 2
triple = 3

while starting_points != 0:
    command = input()
    if command == 'Retire':
        print(f"{player_name} retired after {counter_unsuccess} unsuccessful shots.")
        break
    points = int(input())

    if command == 'Triple':
        pts_per_shot = points * triple
        if pts_per_shot > starting_points:
            counter_unsuccess += 1
            continue
        starting_points -= pts_per_shot
        counter_success += 1

    elif command == 'Double':
        pts_per_shot = points * double
        if pts_per_shot > starting_points:
            counter_unsuccess += 1
            continue
        starting_points -= pts_per_shot
        counter_success += 1

    elif command == 'Single':
        pts_per_shot = points * single
        if pts_per_shot > starting_points:
            counter_unsuccess += 1
            continue
        starting_points -= pts_per_shot
        counter_success += 1

if starting_points == 0:
    print(f'{player_name} won the leg with {counter_success} shots.')




