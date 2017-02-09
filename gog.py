from random import randint

jackpot = randint(1,100)

points = 99 #He will take atleast one guess, as mentioned in rules :P
fl = 0
#print(jackpot)
while True:
    while True:
        num = int(input("Your Guess Please : "))
        if num>=1 and num<=100:
            break
        else:
            print("Between 1-100 Dude!")
    if num == jackpot:
        break
    else:
        points-=1
    if points < 0:
        print("I can't take it anymore :'(")
        fl = 1
        break
    diff = jackpot - num
    if diff > 25:
        print("Your guess is too low")
    elif diff > 0:
        print("Your guess is low")
    elif diff < -25:
        print("Your guess is too high")
    else:
        print("Your guess is high")
if fl == 0:        
    if points > 90:
        print("Bro fly to Vegas! "+str(points)+" Points!!")
    elif points > 50:
        print("Yaa Whatever "+str(points)+" Points")
    else:
        print("Where were we?! "+str(points)+" Points")
        
        
        
 
    
