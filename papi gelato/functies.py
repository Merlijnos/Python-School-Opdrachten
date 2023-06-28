def vraag_aantal_bolletjes(is_zakelijk=False):
    if is_zakelijk:
        while True:
            aantal_liters = input("Hoeveel liter ijs wilt u bestellen? ")
            try:
                aantal_liters = int(aantal_liters)
                if aantal_liters < 1:
                    print("Sorry, het aantal liters moet een positief getal zijn.")
                else:
                    return aantal_liters
            except ValueError:
                print("Sorry, dat is geen geldige invoer. Vul a.u.b. een positief getal in.")
    else:
        while True:
            aantal_bolletjes = input("Hoeveel bolletjes wilt u? ")
            try:
                aantal_bolletjes = int(aantal_bolletjes)
                if aantal_bolletjes < 1 or aantal_bolletjes > 8:
                    print("Sorry, u kunt alleen een waarde tussen 1 en 8 kiezen.")
                else:
                    return aantal_bolletjes
            except ValueError:
                print("Sorry, dat is geen geldige invoer. Vul a.u.b. een getal tussen 1 en 8 in.")

def vraag_bakje_of_hoorntje(aantal_bolletjes):
    if aantal_bolletjes > 4:
        print("U krijgt een bakje, omdat u meer dan 4 bolletjes heeft gekozen.")
        return "bakje"
    else:
        while True:
            bakje_of_hoorntje = input("Wilt u een hoorntje of een bakje? ")
            if bakje_of_hoorntje.lower() in ("hoorntje", "bakje"):
                return bakje_of_hoorntje.lower()
            else:
                print("Sorry, dat is geen geldige keuze. Kies 'hoorntje' of 'bakje'.")

def vraag_smaak(aantal_bolletjes):
    smaken = []
    for i in range(aantal_bolletjes):
        while True:
            smaak = input(f"Welke smaak wilt u voor bolletje nummer {i+1}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ")
            if smaak.lower() in ("a", "c", "m", "v"):
                if smaak.lower() == "a":
                    smaken.append("Aardbei")
                elif smaak.lower() == "c":
                    smaken.append("Chocolade")
                elif smaak.lower() == "m":
                    smaken.append("Munt")
                elif smaak.lower() == "v":
                    smaken.append("Vanille")
                break
            else:
                print("Sorry, dat is geen geldige keuze. Kies A, C, M of V.")
    return smaken

def vraag_topping(bakje_of_hoorntje):
    if bakje_of_hoorntje == "bakje" or bakje_of_hoorntje == "hoorntje":
        while True:
            topping = input("Wat voor topping wilt u? A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ")
            if topping.lower() in ("a", "b", "c", "d"):
                if topping.lower() == "a":
                    return ("Geen", 0)
                elif topping.lower() == "b":
                    return ("Slagroom", 0.50)
                elif topping.lower() == "c":
                    return ("Sprinkels", 0.30)
                elif topping.lower() == "d":
                    return ("Caramel Saus", 0.90)
            else:
                print("Sorry, dat is geen geldige keuze. Kies A, B, C of D.")
    else:
        return ("Geen", 0)

def print_receipt(bestellingen):
    print("\n------------------['Papi Gelato']------------------")
    total = 0
    total_scoops = 0
    total_liters = 0
    total_hoorntjes = 0
    total_bakjes = 0
    flavor_counts = {"Aardbei": 0, "Chocolade": 0, "Munt": 0, "Vanille": 0}
    topping_counts = {"Geen": 0, "Slagroom": 0, "Sprinkels": 0, "Caramel Saus": 0}
    for bestelling in bestellingen:
        if len(bestelling) == 4:
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
        else:
            aantal_liters, smaken = bestelling
            total_liters += aantal_liters
            total += aantal_liters * 9.80
            for smaak in smaken:
                flavor_counts[smaak.capitalize()] += aantal_liters
    for smaak, count in flavor_counts.items():
        if count > 0:
            if total_liters > 0:
                print(f"L.{smaak:<10} {count}L x 9.80   = €{count * 9.80:>5.2f}")
            else:
                print(f"B.{smaak:<10} {count} x 1.10    = €{count * 1.10:>5.2f}")
    if total_hoorntjes > 0:
        print(f"Hoorntje(s): {total_hoorntjes} x 1.25    = €{total_hoorntjes * 1.25:>5.2f}")
    if total_bakjes > 0:
        print(f"Bakje(s):    {total_bakjes} x 0.75    = €{total_bakjes * 0.75:>5.2f}")
    if total_liters > 0:
        print(f"Totaal:                   €{total:>5.2f} ({total_liters}L + {total_scoops}x)")
    else:
        print('                           ------ +')
        print(f"Totaal:                   €{total:>5.2f}.")