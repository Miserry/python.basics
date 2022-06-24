
budget = float(input())
num_stats = int(input())
price_clothes = float(input())

decor = budget * 0.1
cost_clothes = num_stats * price_clothes

if num_stats > 150:
    cost_clothes *= 0.9

spent = decor + cost_clothes


deficit = spent - budget
excess = budget - spent


if spent > budget:
    print('Not enough money!')
    print(f'Wingard needs {deficit:.2f} leva more.')
elif spent <= budget:
    print('Action!')
    print(f'Wingard starts filming with {excess:.2f} leva left.')

