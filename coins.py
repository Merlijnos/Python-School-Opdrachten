# name of student: Merlijn de Groot
# number of student: 99071140
# purpose of program: expand the program, so it'll use 2, 3 and 5 euro coins.
# function of program: calculating the change of the user.
# structure of program: I have used multiple if's, elif's and while.

toPay = int(float(input('Amount to pay: '))* 100) # This will ask the user how much they have to pay.
paid = int(float(input('Paid amount: ')) * 100) # This will ask the user how much they have already paid.
change = paid - toPay # This will check how much you will get back.

if change > 5: #If the change is more than 5 then you get paid in 5s
  coinValue = 500 #the price in cents
elif change > 3:
  coinValue = 300
elif change > 2:
  coinValue = 200
elif change > 0:
  coinValue = 50
else:
  print('Nothing to return')
while change > 0 and coinValue > 0: #This will check your return
    nrCoins = change // coinValue #Calculation for the amount of coins

    if nrCoins > 0: #if the number of coins is more than 0 it'll print the text below.
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #The total coins you have to return.
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #Asks the user how many coins he returned.
      change -= nrCoinsReturned * coinValue #calculation for the coins returned
      print('Number of coins returned: ' + str(nrCoinsReturned) + (' x ') + str(coinValue))

# comment on code below: Checks the total change value, if someone didnt pay enough of 1 type of coins it'll go one step down to a lower value coin.
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #This message will show you the amount you still have to return.
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')