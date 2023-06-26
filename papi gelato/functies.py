def vraag_aantal_bolletjes():
    while True:
        aantal_bolletjes = input("Hoeveel bolletjes wilt u? ")
        if not aantal_bolletjes.isnumeric():
            print("Sorry dat is geen geldig aantal, probeer het opnieuw...")
        elif int(aantal_bolletjes) > 8:
            print("Sorry, we hebben maar plaats voor 8 bolletjes op een hoorntje of in een bakje.")
        elif int(aantal_bolletjes) < 1:
            print("Sorry, u moet minimaal 1 bolletje bestellen.")
        else:
            return int(aantal_bolletjes)

def vraag_bakje_of_hoorntje(aantal_bolletjes=None):
    if aantal_bolletjes is None:
        aantal_bolletjes = vraag_aantal_bolletjes()
    if aantal_bolletjes > 8:
        print("Sorry, u kunt maximaal 8 bolletjes bestellen.")
        return vraag_bakje_of_hoorntje()
    elif aantal_bolletjes > 4:
        print("Dan krijgt u van mij een bakje met", aantal_bolletjes, "bolletjes.")
        return "bakje"
    else:
        while True:
            bakje_of_hoorntje = input("Wilt u deze bestellen in een hoorntje of een bakje? ")
            if bakje_of_hoorntje.lower() == "hoorntje":
                return "hoorntje"
            elif bakje_of_hoorntje.lower() == "bakje":
                return "bakje"
            else:
                print("Sorry dat snap ik niet...")

def vraag_smaak(aantal_bolletjes):
    smaken = []
    for i in range(aantal_bolletjes):
        while True:
            smaak = input(f"Welke smaak wilt u voor bolletje nummer {i+1}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ")
            if smaak.lower() == "aardbei" or smaak == "a":
                smaken.append("Aardbei")
                break
            elif smaak.lower() == "chocolade" or smaak == "c":
                smaken.append("Chocolade")
                break
            elif smaak.lower() == "munt" or smaak == "m":
                smaken.append("Munt")
                break
            elif smaak.lower() == "vanille" or smaak == "v":
                smaken.append("Vanille")
                break
            elif smaak == "":
                print("U heeft niets ingevoerd. Probeer het opnieuw.")
            else:
                print("Sorry dat snap ik niet...")
    return smaken

def vraag_topping(bakje_of_hoorntje):
    while True:
        topping = input("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ")
        if topping.lower() == "a":
            return ("Geen", 0)
        elif topping.lower() == "b":
            return ("Slagroom", 0.5)
        elif topping.lower() == "c":
            return ("Sprinkels", 0.3)
        elif topping.lower() == "d":
            if bakje_of_hoorntje == "hoorntje":
                return ("Caramel Saus", 0.6)
            elif bakje_of_hoorntje == "bakje":
                return ("Caramel Saus", 0.9)
        elif topping == "":
            print("U heeft niets ingevoerd. Probeer het opnieuw.")
        else:
            print("Sorry dat snap ik niet...")

def print_receipt(bestellingen):
    print("\n------------------['Papi Gelato']------------------")
    total = 0
    total_scoops = 0
    total_hoorntjes = 0
    total_bakjes = 0
    flavor_counts = {"Aardbei": 0, "Chocolade": 0, "Munt": 0, "Vanille": 0}
    topping_counts = {"Geen": 0, "Slagroom": 0, "Sprinkels": 0, "Caramel Saus": 0}
    for bestelling in bestellingen:
        aantal_bolletjes, bakje_of_hoorntje, smaken, topping = bestelling
        total_scoops += aantal_bolletjes
        if bakje_of_hoorntje == "hoorntje":
            total_hoorntjes += 1
            total += aantal_bolletjes * 1.25
        elif bakje_of_hoorntje == "bakje":
            total_bakjes += 1
            total += aantal_bolletjes * 1.10 + 0.75
        for smaak in smaken:
            flavor_counts[smaak.capitalize()] += 1
        topping_counts[topping[0]] += 1
        if topping[0] != "Geen":
            if topping[0] == "Sprinkels":
                print(f"Topping           = €{topping[1] * total_scoops:>5.2f}")
                total += topping[1] * total_scoops
            else:
                print(f"{topping[0]:<10}    = €{topping[1]:>5.2f}")
                total += topping[1]
    for smaak, count in flavor_counts.items():
        if count > 0:
            print(f"B.{smaak:<10} {count} x 1.10    = €{count * 1.10:>5.2f}")
    if total_hoorntjes > 0:
        print(f"Hoorntje(s): {total_hoorntjes} x 1.25    = €{total_hoorntjes * 1.25:>5.2f}")
    if total_bakjes > 0:
        print(f"Bakje(s):    {total_bakjes} x 0.75    = €{total_bakjes * 0.75:>5.2f}")
    print('                           ------ +')
    print(f"Totaal:                   €{total:>5.2f}.")