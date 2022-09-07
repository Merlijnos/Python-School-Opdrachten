a = 3
b = 7.45
c = 45
d = 5
e = 0.37
f = 3.33

print('De tickets kosten bij elkaar',a*b)
print('De VIP-VR_GAMESEAT kost', c/d*e)
print('De dag kostte in totaal', a*b + (c/d*e))

txt = 'Dit geweldige dagje-uit met {}'
txt2 = 'mensen in de Speelhal met {}'
txt3 = 'minuten VR kost je maar {} euro'

print(txt.format(a))
print(txt2.format(c))
print(txt3.format(f))


