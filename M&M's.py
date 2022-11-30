import random 
lijst = []
MnMs = ['oranje','blauw','groen','bruin']
aantal = int(input("Hoeveel M&M's wil je toevoegen aan de zak? "))
for x in range (aantal):
    lijst.append(random.choices(MnMs))
print(lijst)
