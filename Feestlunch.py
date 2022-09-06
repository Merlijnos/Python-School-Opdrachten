a = 0.39
b = 17
c = 2.78
d = 2
e = 0.50
f = 3
g = 10.69

print('De prijs van de Croissants is:')
print(a*b)

print('De stokbroden kosten:')
print(c*d)

print('Je krijgt',e*f,'euro korting') 

print('De eindprijs is', (c*d + a*b) - e*f)

txt = 'De feestlunch kost je bij de bakker {} euro voor de'

txt2 = '{} croissantjes en de'

txt3 = '{} stokbroden als de 3 kortingsbonnen nog geldig zijn!'

print(txt.format(g))

print(txt2.format(b))

print(txt3.format(d))