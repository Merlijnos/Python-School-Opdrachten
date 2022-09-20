from distutils.log import error

print('------------------------------------------------')
print('    - Solicitatieformulier Circusdirecteur -    ')
print('------------------------------------------------')
print('Er worden zo een paar vragen gesteld.           ')
print('typ 1 voor ja en 2 voor nee.')
print('Beantwoord de vragen eerlijk en denk niet te moeilijk.')
print('Success! :)')
print('------------------------------------------------')
nee = 2
naam = input('Wat is uw naam? ')
print('Hallo ' + naam + '!')

print('Hoeveel jaar Heeft u praktijkervaring met dieren-dressuur, jongleren of praktijkervaring met acrobatiek?')
vraag1 = input()
if vraag1 == '2':
    raise ValueError('2 Jaar is niet genoeg, Jammer joh!')

print('Heeft u een MBO-4 diploma voor ondernemen?')
vraag2 = input()

print('Bent u in bezit van een geldig vrachtwagen bewijs?')
vraag3 = input()
if vraag3 == '2':
    raise ValueError('Ga dan maar fietsen, whahaha')

print('Bent u in bezit van een hoge hoed?')
vraag4 = input()

print('Bent u een man of een vrouw? Typ 1 man en 2 voor vrouw.')
manofvrouw = input()
if int(manofvrouw) < 2:
    print('Heeft u een snor van 10cm?')
    snorlengte = input()
else:
    print('Heeft u rood haar van 20cm?')
    roodhaar = input()

print('Wat is uw lengte?')
vraag6 = input()
    
print('Wat is uw lichaamsgewicht in kilos?')
vraag7 = input()
    
print('Heeft u het certificaat “Overleven met gevaarlijk personeel”?')
vraag8 = input()

print('heeft u een hond? ')
vraag9 = input()
if vraag9 == '2':
    raise TypeError('Er wordt nu een hond gestuurd naar uw adres.')

print('Kunt u springen?')
vraag10 = input()
if vraag10 == '2':
    raise TypeError('Koop eerst maar een trampoline en ga maar oefenen.')

print('Bent u moordlustig?')
vraag11 = input()
if vraag11 == '1':
    raise TypeError('112 wordt nu gebeld en staan in 5 Minuten voor de deur.')

if int(vraag1) > 2 and int(vraag2) < 2 and int(vraag3) < 2 and int(vraag4) < 2  and int(vraag6) > 150 and int(vraag7) > 90 and int(vraag8) < 2 and int(vraag9) < 2 and int(vraag10) < 2 and int(vraag11) > 1 and int(snorlengte) < 2 and int(roodhaar) < 2:
    print('U bent aangenomen!')
else:
    print('Helaas, u bent niet geschikt als circusdirecteur.')