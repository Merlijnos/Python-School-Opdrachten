import random
kleuren = ['harten ', 'klaveren ', 'schoppen ', 'ruiten ']
kaarten = [ '2', '3', '4', '5', '6', '7', '8', '9', '10','boer','vrouw','heer','aas']
joker = ['Joker','Joker']

for x in range (0,4):
    a = kleuren[x]
    for y in range(0,13):
        b = kaarten[y]
        ab = a + b
        joker.append(ab)

random.shuffle(joker)

for i in range(1,6):
    print(f'kaart {i}: {joker[i]}')
print(joker)