print('Een pizza small kost u: €5')
print('Een pizza medium kost u: €7')
print('Een pizza large kost u: €10')
# Hierboven staan de Prijzen van de pizzas.
print('hoeveel small pizzas wilt u?')
try:
    small = float(input())
except:
    print('U moet een getal invoeren!')

print('hoeveel medium pizzas wilt u?')
try:
    medium = float(input())
except:
    print('U moet een getal invoeren!')

print('hoeveel large pizzas wilt u?')
try:
    large = float(input())
except:
    print('U moet een getal invoeren!')
# Hierboven staan de vragen met een invulvak.
smallprijs = float(5)
mediumprijs = float(7)
largeprijs = float(10)
# Hierboven staan de prijzen van de pizzas.
print('----------------------------------------')
print('Aantal pizzas: ' 'Small:',small,'Medium:', medium,'Large:',large)
print('Pizza small: €',small*smallprijs)
print('Pizza medium: €',medium*mediumprijs)
print('Pizza large: €',large*largeprijs)
print('Totaalprijs €',(small*smallprijs)+(medium*mediumprijs)+(large*largeprijs))
print('----------------------------------------')
# Dit is het bonnetje van alle pizzas bij elkaar en de prijzen.