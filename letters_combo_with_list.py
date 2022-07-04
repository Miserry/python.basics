
letters1 = input()
letters2 = input()
letters3 = input()

letters =  letters1 + letters2 + letters3
combos = []
for letter1 in letters:
    for letter2 in letters:
        for letter3 in letters:
            if letters3 in letter1 or letters3 in letter2 or letters3 in letter3:
                continue
            combos.append(letter1+letter2+letter3)

print(combos, len(combos))





