# What i have missed with this exercise....

days = int(input())
money = 0
all_money = 0
days_win = 0
days_lose = 0

for day in range(1, days + 1):
    money = 0
    won_games = 0
    lose_games = 0

    command = input() #we can enter sport or a Finish here.
    while command != "Finish":

        result = input() # win or lose.

        if result == "win":
            money += 20
            won_games += 1
        elif result == "lose":
            lose_games += 1
        command = input() # here we ask for the sport again, because on row 12 it is outside the while loop.

        if command == "Finish":
            if won_games > lose_games:
                days_win += 1
                money *= 1.1
                all_money += money
            else:
                days_lose += 1
                all_money += money

if days_win > days_lose:
    all_money += all_money * 0.2
    print(f"You won the tournament! Total raised money: {all_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {all_money:.2f}")