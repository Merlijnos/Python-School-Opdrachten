def welkom():
    print("Welkom bij Papi Gelato!")

def vraag_aantal_bolletjes():
    while True:
        aantal_bolletjes = input("Hoeveel bolletjes wilt u? ")
        if aantal_bolletjes.isdigit():
            aantal_bolletjes = int(aantal_bolletjes)
            if 1 <= aantal_bolletjes <= 3:
                bakje_of_hoorntje = input("Wilt u deze bolletjes in een hoorntje of een bakje? ")
                while bakje_of_hoorntje.lower() not in ["hoorntje", "bakje"]:
                    print("Sorry, dat snap ik niet...")
                    bakje_of_hoorntje = input("Wilt u deze bolletjes in een hoorntje of een bakje? ")
                return aantal_bolletjes, bakje_of_hoorntje
            elif 4 <= aantal_bolletjes <= 8:
                return aantal_bolletjes, "bakje"
            elif aantal_bolletjes > 8:
                print("Sorry, zulke grote bakken hebben we niet.")
        print("Sorry, dat snap ik niet...")

def vraag_smaak(aantal_bolletjes):
    smaken = {"A": "Aardbei", "C": "Chocolade", "M": "Munt", "V": "Vanille"}
    bestellingen = []
    for i in range(1, aantal_bolletjes+1):
        while True:
            smaak = input(f"Welke smaak wilt u voor bolletje nummer {i}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ")
            if smaak.upper() in smaken:
                bestellingen.append(smaken[smaak.upper()])
                break
            print("Sorry, dat snap ik niet...")
    return bestellingen

def geef_ijs(aantal_bolletjes, bakje_of_hoorntje):
    print(f"Hier is uw {bakje_of_hoorntje} met {aantal_bolletjes} bolletje(s).")

def vraag_meer_bestellen():
    while True:
        meer_bestellen = input("Wilt u nog meer bestellen? ")
        if meer_bestellen.lower() in ["ja", "nee"]:
            return meer_bestellen.lower() == "ja"
        print("Sorry, dat snap ik niet...")

def print_receipt(bestellingen):
    total_price = 0
    total_bolletjes = 0
    total_bakjes = 0
    total_hoorntjes = 0
    smaken_dict = {}
    print("Papi Gelato\n------------------------------")
    for bestelling in bestellingen:
        aantal_bolletjes, bakje_of_hoorntje, smaken = bestelling if isinstance(bestelling, tuple) else (bestelling, "bakje" if bestelling >= 4 else "hoorntje", [])
        price = aantal_bolletjes * 1.25
        total_bolletjes += aantal_bolletjes
        if bakje_of_hoorntje == "bakje":
            total_bakjes += 1
            total_price += price
        else:
            total_hoorntjes += 1
            hoorntjes_price = total_hoorntjes * 1.25
            for smaak in smaken:
                smaken_dict[smaak] = smaken_dict.get(smaak, 0) + 1
                hoorntjes_price += 1.10
            total_price += hoorntjes_price
    if total_bakjes > 0:
        print(f"Bakjes: {total_bakjes} x €{total_bakjes * 0.75:.2f}")
        if total_hoorntjes > 0:
            print(f"Hoorntjes: {total_hoorntjes} x €{total_hoorntjes * 1.25:.2f}")
    elif total_hoorntjes > 0:
        print(f"Hoorntjes: {total_hoorntjes} x €{total_hoorntjes * 1.25:.2f}")
    for smaak, aantal_bolletjes in smaken_dict.items():
        print(f"- {aantal_bolletjes} {smaak} x €1.10 = €{aantal_bolletjes * 1.10:.2f}")
    print(f"Totaal prijs: €{total_price:.2f}")