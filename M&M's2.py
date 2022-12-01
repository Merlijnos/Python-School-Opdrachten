import random 
aantal = int(input("Hoeveel M&M's wil je toevoegen aan de zak? "))
MnMs = ['oranje', 'blauw', 'groen', 'bruin','geel']
zak = {}
oranje = random.randint(0,aantal)
overige = aantal-oranje
blauw = random.randint(0,overige)
overige2 = overige-blauw
groen = random.randint(0,overige2)
overige3 = overige2-groen
bruin = random.randint(0,overige3)
overige4 = overige3-bruin
geel = overige4

if oranje > 0:
    zak['oranje']=oranje
if blauw > 0:
    zak['blauw']=blauw
if groen > 0:
    zak['groen']=groen
if bruin > 0:
    zak['bruin']=bruin
if geel > 0:
    zak['geel']=geel
print(zak)