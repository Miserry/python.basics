
btc_count = int(input())
yuan_count = float(input())
commission = float(input())

eur_bgn = 1.95
btc_bgn = 1168
usd_bgn = 1.76
yuan_usd = 0.15


bg1 = btc_count * btc_bgn
bg2 = yuan_count * yuan_usd * usd_bgn

tot_eur = (bg1 + bg2) / eur_bgn
after_commission = tot_eur * commission / 100
eur_left = tot_eur - after_commission
print(f'{eur_left:.2f}')


