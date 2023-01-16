import random

def lootjesverdeler():
# Vraag hoeveel mensen er meedoen
    while True:
        try:
            Aantal = int(input("Hoeveel mensen doen er mee aan de lootjes verdeler? "))
            if Aantal < 3:
                print("Het spel kan alleen doorgaan als er minstens 3 mensen meedoen.")
                continue
            break
        except ValueError:
            print("Vul een geldig getal in.")

# Vraag om de namen van de spelers
    Namen = []
    for i in range(Aantal):
        Invullen = input("Vul de naam van speler {} in: ".format(i+1))
        Namen.append(Invullen)
        
# Kies de lootjes in een random volgorde uit
    random.shuffle(Namen)
    for i in range(Aantal):
        if Namen[i] == Namen[(i + 1) % Aantal]:
            random.shuffle(Namen)
            break

# Print wie elkaars lootje heeft
    for i in range(Aantal):
        print("{} heeft een cadeau voor {}".format(Namen[i], Namen[(i + 1) % Aantal]))

# Vraag of de gebruiker nog een keer wil spelen
while True:
    lootjesverdeler()
    NogEenKeer = input("Wilt u nog een keer spelen? (ja/nee) ").lower()
    if NogEenKeer != "ja":
        break
