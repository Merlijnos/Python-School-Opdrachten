def welkom():
    print("Welkom bij Papi Gelato! Hieronder ziet u onze beschikbare smaken:")

def vraag_aantal_bolletjes():
    while True:
        aantal_bolletjes = input("Hoeveel bolletjes wilt u? ")
        if aantal_bolletjes.isdigit():
            aantal_bolletjes = int(aantal_bolletjes)
            if aantal_bolletjes >= 1 and aantal_bolletjes <= 3:
                return aantal_bolletjes, "hoorntje"
            elif aantal_bolletjes >= 4 and aantal_bolletjes <= 8:
                return aantal_bolletjes, "bakje"
            elif aantal_bolletjes > 8:
                print("Sorry, zulke grote bakken hebben we niet.")
            else:
                print("Sorry, dat snap ik niet...")
        else:
            print("Sorry, dat snap ik niet...")

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