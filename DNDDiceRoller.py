#cerner_2^5_2019

import random

D = raw_input("Roll your dice Adventurer XnX (ex. 1d4 , 1d6 , 1d8 , 1d10 , 1d12 and 1d20.\n")

print(D)

diceAmount = D.split("d", 1)[0]

diceType = int(D.split("d", 2)[1])

for x in range(1, (int(diceAmount) + 1)):
    roll = random.randint(1,diceType)
    print('\n')    
    print( "Roll "+ str(x) +"  = " + str(roll))
    if diceType == 20:
        if roll == 20:
            print("NAT 20 BIG DAMAGE COMING")
        if roll == 1:
            print("Critical Fail")
        
        
    
    
