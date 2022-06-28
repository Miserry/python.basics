
account_balance = 0

deposit = input()


while deposit != 'NoMoreMoney':
    deposit = float(deposit)
    if deposit < 0:
        print(f'Invalid operation!')
        break
    account_balance += deposit
    print(f'Increase: {deposit:.2f}')
    deposit = input()



print(f'Total: {account_balance:.2f}')

