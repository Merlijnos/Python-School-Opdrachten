# Lijst met beschikbare smaken
beschikbare_smaken = ["vanille", "aardbei", "chocolade", "mango"]

# Functie om te controleren of de smaak beschikbaar is
def smaak_beschikbaar(smaak):
    return smaak.lower() in beschikbare_smaken

# Functie om de bestelling op te nemen
def bestelling_opnemen():
    print("Welkom bij Papi Gelato! Hieronder ziet u onze beschikbare smaken:")
    print(beschikbare_smaken)
    
    # Stap 1
    while True:
        aantal_bolletjes = input("Hoeveel bolletjes wilt u? ")
        if aantal_bolletjes.isdigit():
            aantal_bolletjes = int(aantal_bolletjes)
            if aantal_bolletjes >= 1 and aantal_bolletjes <= 3:
                # Stap 2
                while True:
                    bakje_of_hoorntje = input(f"Wilt u deze {aantal_bolletjes} bolletje(s) in een hoorntje of een bakje? ")
                    if bakje_of_hoorntje.lower() == "hoorntje":
                        print(f"Hier is uw hoorntje met {aantal_bolletjes} bolletje(s).")
                        break
                    elif bakje_of_hoorntje.lower() == "bakje":
                        # Stap 3
                        while True:
                            smaak = input("Welke smaak wilt u? ")
                            if smaak_beschikbaar(smaak):
                                print(f"Hier is uw bakje met {aantal_bolletjes} bolletje(s) van {smaak} smaak.")
                                break
                            else:
                                print("Sorry, die smaak hebben we niet. Kies een andere smaak.")
                        break
                    else:
                        print("Sorry, dat snap ik niet...")
            elif aantal_bolletjes >= 4 and aantal_bolletjes <= 8:
                print(f"Dan krijgt u van mij een bakje met {aantal_bolletjes} bolletjes.")
            elif aantal_bolletjes > 8:
                print("Sorry, zulke grote bakken hebben we niet.")
            else:
                print("Sorry, dat snap ik niet...")
        else:
            print("Sorry, dat snap ik niet...")

        # Stap 4
        meer_bestellen = input("Wilt u nog meer bestellen? ")
        if meer_bestellen.lower() == "ja":
            continue
        elif meer_bestellen.lower() == "nee":
            print("Bedankt en tot ziens!")
            break
        else:
            print("Sorry, dat snap ik niet...")

# Bestelling opnemen
bestelling_opnemen()
