def vraag_aantal_bolletjes(is_zakelijk=False):
    if is_zakelijk:
        while True:
            aantal_liters = input("Hoeveel liter ijs wilt u bestellen? ")
            try:
                aantal_liters = int(aantal_liters)
                if aantal_liters < 1:
                    print("Sorry dat is geen optie die we aanbieden...")
                else:
                    return aantal_liters
            except ValueError:
                print("Sorry dat is geen optie die we aanbieden...")
    else:
        while True:
            aantal_bolletjes = input("Hoeveel bolletjes wilt u? ")
            try:
                aantal_bolletjes = int(aantal_bolletjes)
                if aantal_bolletjes < 1 or aantal_bolletjes > 8:
                    print("Sorry dat is geen optie die we aanbieden...")
                else:
                    return aantal_bolletjes
            except ValueError:
                print("Sorry dat is geen optie die we aanbieden...")

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
                print("Sorry dat is geen optie die we aanbieden...")

def vraag_smaak(aantal_bolletjes):
    smaken = []
    for i in range(aantal_bolletjes):
        while True:
            smaak = input(f"Welke smaak wilt u voor nummer {i+1}? A) Aardbei, C) Chocolade of V) Vanille? ")
            if smaak.lower() in ("a", "c", "v"):
                if smaak.lower() == "a":
                    smaken.append("Aardbei")
                elif smaak.lower() == "c":
                    smaken.append("Chocolade")
                elif smaak.lower() == "v":
                    smaken.append("Vanille")
                break
            else:
                print("Sorry dat is geen optie die we aanbieden...")
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
                print("Sorry dat is geen optie die we aanbieden...")
    else:
        return ("Geen", 0)

def print_receipt(bestellingen):
    print("\n------------------['Papi Gelato']------------------")
    total = 0
    total_scoops = 0
    total_liters = 0
    total_hoorntjes = 0
    total_bakjes = 0
    flavor_counts = {}
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
                total += aantal_bolletjes * 0.95 + 0.75
            for smaak in smaken:
                if smaak not in flavor_counts:
                    flavor_counts[smaak] = 0
                flavor_counts[smaak] += 1
            topping_counts[topping[0]] += topping[1] * aantal_bolletjes
        else:
            aantal_liters, smaken = bestelling
            total_liters += aantal_liters
            total += aantal_liters * 9.80
            for smaak in smaken:
                if smaak not in flavor_counts:
                    flavor_counts[smaak] = 0
                flavor_counts[smaak] += aantal_liters
    for topping, price in topping_counts.items():
        if price > 0:
            if topping == "Geen":
                continue
            elif topping == "Slagroom":
                print(f"{topping:<10}    = €0.50")
                total += price * 0.50
            elif topping == "Sprinkels":
                print(f"{topping:<10}    = €{total_scoops * 0.30:>5.2f}")
                total += total_scoops * 0.30
            elif topping == "Caramel Saus":
                if total_hoorntjes > 0:
                    print(f"{topping:<10}    = €0.60")
                    total += price * 0.60
                elif total_bakjes > 0:
                    print(f"{topping:<10}    = €0.90")
                    total += price * 0.90
    for smaak, count in flavor_counts.items():
        if count > 0:
            if total_liters > 0:
                print(f"{smaak.capitalize():<10} {count}L x 9.80   = €{count * 9.80:>5.2f}")
            else:
                print(f"{smaak.capitalize():<10} {count} x 0.95    = €{count * 0.95:>5.2f}")
    if total_hoorntjes > 0:
        print(f"Hoorntje(s): {total_hoorntjes} x 1.25    = €{total_hoorntjes * 1.25:>5.2f}")
    if total_bakjes > 0:
        print(f"Bakje(s):    {total_bakjes} x 0.75    = €{total_bakjes * 0.75:>5.2f}")
    if total_liters > 0:
        print(f"Totaalprijs: €{total:.2f}")
    else:
        print(f"Totaalprijs: €{total:.2f}")
    print("------------------------")