import time
import math
from termcolor import colored
from data import JOURNEY_IN_DAYS
from data import COST_FOOD_HUMAN_COPPER_PER_DAY
from data import COST_FOOD_HORSE_COPPER_PER_DAY
from data import COST_TENT_GOLD_PER_WEEK
from data import COST_HORSE_SILVER_PER_DAY
from data import COST_INN_HUMAN_SILVER_PER_NIGHT
from data import COST_INN_HORSE_COPPER_PER_NIGHT
##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float: # 10 copper = 1 silver
    return round(amount / 10, 2)

def silver2gold(amount:int) -> float: # 5 silver = 1 gold
    return round(amount / 5, 2)

def copper2gold(amount:int) -> float: # 50 copper = 1 gold
    return round(amount / 50, 2)

def platinum2gold(amount:int) -> float: # 1 platinum = 25 gold
    return round(amount * 25, 2)

def getPersonCashInGold(personCash:dict) -> float:
    return platinum2gold(personCash['platinum']) + personCash['gold'] + silver2gold(personCash['silver']) + copper2gold(personCash['copper'])

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int(0.4), horses:int(0.3)) -> float:
    Human = copper2gold(COST_FOOD_HUMAN_COPPER_PER_DAY * people) * JOURNEY_IN_DAYS
    Horse = copper2gold(COST_FOOD_HORSE_COPPER_PER_DAY * horses) * JOURNEY_IN_DAYS
    return round(Human + Horse, 2)

##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    persons= []
    for person in list:
        if person[key] == value:
            persons.append(person)
    return persons

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends:list) -> int:
    return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends:list) -> list:
    sharewith = getShareWithFriends(friends)
    return getAdventuringPeople(sharewith)
    
##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people / 3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    return (silver2gold((horses * COST_HORSE_SILVER_PER_DAY) * (JOURNEY_IN_DAYS))) + ((tents * COST_TENT_GOLD_PER_WEEK ) * math.ceil( JOURNEY_IN_DAYS / 7))

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
     return ', '.join([f"{item['amount']}{item['unit']} {item['name']}" for item in items])

def getItemsValueInGold(items:list) -> float:
    total_gold = 0
    for item in items:
        if item['price']['type'] == 'gold':
            total_gold += item['amount'] * item['price']['amount']
        elif item['price']['type'] == 'silver':
            total_gold += silver2gold(item['amount'] * item['price']['amount'])
        elif item['price']['type'] == 'copper':
            total_gold += copper2gold(item['amount'] * item['price']['amount'])
        elif item['price']['type'] == 'platinum':
            total_gold += platinum2gold(item['amount'] * item['price']['amount'])
    return total_gold
    
##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    total_gold = 0
    for person in people:
        total_gold += getPersonCashInGold(person['cash'])
    return total_gold

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    InterestingInvestors = []
    for index in range(0,len(investors)):
        if investors[index]['profitReturn'] <= 10:
            InterestingInvestors.append(investors[index])
    return InterestingInvestors

def getAdventuringInvestors(investors:list) -> list:
    investorslessthantenpercent=getInterestingInvestors(investors)
    investorsfollowing = []
    for investor in investorslessthantenpercent:
        if investor['adventuring']==True:
            investorsfollowing.append(investor)
    return investorsfollowing

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    totaalbedrag=0
    totalinvestors=len(getAdventuringInvestors(investors))
    gearprice=getItemsValueInGold(gear)*totalinvestors
    tentcost=totalinvestors*COST_TENT_GOLD_PER_WEEK*2
    foodcost=totalinvestors*COST_FOOD_HUMAN_COPPER_PER_DAY*JOURNEY_IN_DAYS
    foodcostpaard=totalinvestors*COST_FOOD_HORSE_COPPER_PER_DAY*JOURNEY_IN_DAYS
    horsecost=totalinvestors*COST_HORSE_SILVER_PER_DAY*JOURNEY_IN_DAYS
    foodcostingold=copper2gold(foodcost)
    foodcosthorseingold=copper2gold(foodcostpaard)
    horsecostingold=silver2gold(horsecost)
    totaalbedrag+=tentcost+foodcostingold+foodcosthorseingold+horsecostingold+gearprice
    return round(totaalbedrag,2)

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    people_cost = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people
    horses_cost  = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    totalcost = people_cost + horses_cost
    return math.floor(leftoverGold / totalcost)
    
def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    people_cost = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people
    horses_cost  = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    totalcost = round(nightsInInn * (people_cost + horses_cost) , 2)
    return totalcost

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()