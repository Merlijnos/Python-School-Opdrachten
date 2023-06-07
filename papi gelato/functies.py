def print_welcome_message():
    print("Welkom bij Papi Gelato!")

def vraag_bestellingen():
    aantal_bolletjes = int(input("Hoeveel bolletjes wilt u? "))
    bakje_of_hoorntje = vraag_bakje_of_hoorntje(aantal_bolletjes)
    smaken = vraag_smaak(aantal_bolletjes)
    return [(aantal_bolletjes, bakje_of_hoorntje, smaken)]

def vraag_meer_bestellingen(bestellingen):
    while True:
        meer_bestellingen = input("Wilt u nog meer bestellingen plaatsen? (ja/nee): ")
        if meer_bestellingen.lower() == "ja":
            bestellingen += vraag_bestellingen()
        else:
            print_receipt(bestellingen)
            break
    return bestellingen

def print_receipt(bestellingen):
    print("\n------------------['Papi Gelato']------------------")
    total = 0
    total_scoops = 0
    total_hoorntjes = 0
    total_bakjes = 0
    flavor_counts = {"Aardbei": 0, "Chocolade": 0, "Munt": 0, "Vanille": 0}
    for bestelling in bestellingen:
        aantal_bolletjes, bakje_of_hoorntje, smaken = bestelling
        total_scoops += aantal_bolletjes
        if bakje_of_hoorntje == "hoorntje":
            total_hoorntjes += 1
            total += aantal_bolletjes * 1.25
        elif bakje_of_hoorntje == "bakje":
            total_bakjes += 1
            total += aantal_bolletjes * 1.10 + 0.75
        for smaak in smaken:
            flavor_counts[smaak.capitalize()] += 1
    for smaak, count in flavor_counts.items():
        if count > 0:
            print(f"B.{smaak:<10} {count} x 1.10    = €{count * 1.10:>5.2f}")
    if total_hoorntjes > 0:
        print(f"Hoorntje(s): {total_hoorntjes} x 1.25    = €{total_hoorntjes * 1.25:>5.2f}")
    if total_bakjes > 0:
        print(f"Bakje(s):    {total_bakjes} x 0.75    = €{total_bakjes * 0.75:>5.2f}")
    print('                           ------ +')
    print(f"Totaal:                    €{total:>5.2f}.")

def vraag_bakje_of_hoorntje(aantal_bolletjes):
    while True:
        if 4 <= aantal_bolletjes <= 8:
            print("Dan krijgt u van mij een bakje met", aantal_bolletjes, "bolletjes.")
            bakje_of_hoorntje = "bakje"
        else:
            bakje_of_hoorntje = input("Wilt u deze bolletjes in een hoorntje of een bakje? ")
        if bakje_of_hoorntje.lower() not in ["hoorntje", "bakje"]:
            print("Sorry, dat snap ik niet...")
            continue
        return bakje_of_hoorntje.lower()

def vraag_smaak(aantal_bolletjes):
    smaken = []
    for i in range(1, aantal_bolletjes+1):
        while True:
            smaak = input(f"Welke smaak wilt u voor bolletje nummer {i}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ")
            if smaak.lower() not in ["a", "c", "m", "v"]:
                print("Sorry, dat snap ik niet...")
                continue
            if smaak.lower() == "a":
                smaken.append("Aardbei")
            elif smaak.lower() == "c":
                smaken.append("Chocolade")
            elif smaak.lower() == "m":
                smaken.append("Munt")
            elif smaak.lower() == "v":
                smaken.append("Vanille")
            break
    return smaken