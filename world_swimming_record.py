
world_record = float(input())
lenght = float(input())
m_per_sec = float(input())

time = lenght * m_per_sec

slowdown = 12.5

tot_slowdown = int((lenght / 15 )) * slowdown
tot_slowdown = tot_slowdown

tot_time = time + tot_slowdown

diff = abs(world_record - tot_time)


if tot_time < world_record:
    print(f'Yes, he succeeded! The new world record is {tot_time:.2f} seconds.')

else:
    print(f'No, he failed! He was {diff:.2f} seconds slower.')


