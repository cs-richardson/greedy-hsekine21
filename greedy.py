'''
Program that takes the amount of change from the user in US dollars and outputs
the least amount of coins to represent that change in quarters, nickels, dimes,
and pennies
'''
# Hina Sekine 

change = input("How much change is owed?: ")
# checks while there is more than 1 period and not just numbers 
while change.count('.') > 1 or (change.replace('.','')).isdigit() == False:
    change = input("How much change is owed?: ")

coins = [25, 10, 5, 1] # assuming there are only 4 types of coins 
calculate = round(100 * float(change)) # converts dollars to cents and rounds it down to $0.01  
changeCoinNum = 0 # number of coins 

# 25 cents 
changeCoinNum = changeCoinNum + (calculate // coins[0]) # adds # of coins
calculate = calculate % coins[0] # remaining cents

# 10 cents 
changeCoinNum = changeCoinNum + (calculate // coins[1]) # adds # of coins
calculate = calculate % coins[1] # remaining cents

# 5 cents 
changeCoinNum = changeCoinNum + (calculate // coins[2])# adds # of coins
calculate = calculate % coins[2] # remaining cents

changeCoinNum = changeCoinNum + calculate # 1 cent, adds # of coins


if changeCoinNum <= 1: # just english's plural / singular rules
    print('You need ' + str(changeCoinNum) + ' coin')
else:
    print('You need ' + str(changeCoinNum) + ' coins')  
    

