def welkom():
    print("Welkom bij Papi Gelato!")

def vraag_aantal_bolletjes():
    while True:
        aantal_bolletjes = input("Hoeveel bolletjes wilt u? ")
        if aantal_bolletjes.isdigit():
            aantal_bolletjes = int(aantal_bolletjes)
            if aantal_bolletjes >= 1 and aantal_bolletjes <= 3:
                bakje_of_hoorntje = input("Wilt u deze bolletjes in een hoorntje of een bakje? ")
                while bakje_of_hoorntje.lower() not in ["hoorntje", "bakje"]:
                    print("Sorry, dat snap ik niet...")
                    bakje_of_hoorntje = input("Wilt u deze bolletjes in een hoorntje of een bakje? ")
                return aantal_bolletjes, bakje_of_hoorntje
            elif aantal_bolletjes >= 4 and aantal_bolletjes <= 8:
                return aantal_bolletjes, "bakje"
            elif aantal_bolletjes > 8:
                print("Sorry, zulke grote bakken hebben we niet.")
            else:
                print("Sorry, dat snap ik niet...")
        else:
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
            else:
                print("Sorry, dat snap ik niet...")
    return bestellingen

def geef_ijs(aantal_bolletjes, bakje_of_hoorntje):
    if bakje_of_hoorntje == "hoorntje":
        print(f"Hier is uw hoorntje met {aantal_bolletjes} bolletje(s).")
    elif bakje_of_hoorntje == "bakje":
        print(f"Hier is uw bakje met {aantal_bolletjes} bolletje(s).")

def vraag_meer_bestellen():
    while True:
        meer_bestellen = input("Wilt u nog meer bestellen? ")
        if meer_bestellen.lower() == "ja":
            return True
        elif meer_bestellen.lower() == "nee":
            return False
        else:
            print("Sorry, dat snap ik niet...")

def print_receipt(bestellingen):
    total_price = 0
    total_bolletjes = 0
    total_bakjes = 0
    smaken_dict = {}
    print("Papi Gelato")
    print("------------------------------")
    for i, bestelling in enumerate(bestellingen):
        aantal_bolletjes, bakje_of_hoorntje, smaken = bestelling
        price = aantal_bolletjes * 1.25
        total_price += price
        total_bolletjes += aantal_bolletjes
        if bakje_of_hoorntje == "bakje":
            total_bakjes += 1
        for smaak in smaken:
            if smaak in smaken_dict:
                smaken_dict[smaak] += 1
            else:
                smaken_dict[smaak] = 1
    print(f"Aantal bolletjes: {total_bolletjes}\nBakjes: {total_bakjes}\nHoorntjes: {len(bestellingen) - total_bakjes}")
    print("Smaak(en):")
    for smaak, aantal_bolletjes in smaken_dict.items():
        print(f"- {aantal_bolletjes}x {smaak}")
    print(f"Totaal: {total_price:.2f} euro")