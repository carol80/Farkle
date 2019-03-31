##########  DICE  Game   ###########
import random


#-------------values entry-------------
dice=[]
tap=0
rem=0
#n=5
deck=0
deckx=0
scoreboard=[]
def roll(n):
    # Needs implementing!
    # Tip: random.randint(min, max) can be used to generate random numbers
    values = []
    i=0
    while i<n :
        values.append(random.randint(1, 6))
        i+=1
    return values




#-------------SCORE--------------
def score(dice):
    # You need to write this method
    length=len(dice)
    item=sorted(dice)
    #import pdb; pdb.set_trace()
    if dice==[]:return 0
    else:
        result=0
        result1=0
        result2=0
        flag=length 
        i=0
        while i < length:
            if length>=3:
                if i+1<=length and i+2<length: 
                    if item[i]==item[i+1] and item[i+1]==item[i+2]:
                        if item[i]==1:
                            result1+=1000
                            flag=i
                            break
                        else:
                            result1+= item[i]*100
                            flag=i
                            break
            if item[i] == 1:
                result1+=100

            if item[i] == 5:
                result1+=50    

            else:
                result1+=0

            i+=1    

    #checking after the triplet
        flag+=3
        if flag > length:
            return result1
        else:
            while flag < length:

                if item[flag] == 1:
                    result2+=100

                if item[flag] == 5:
                    result2+=50    

                else:
                    result2+=0

                flag+=1    

            result=result1+result2
            return result

#--------------FUNCTION 3------------
player=[]
def Dice_func3(n):
    if n==0:
        return 0
    else:
        dice=roll(n)
        i=0
        while i<n:
            print(dice[i]),
            i+=1
        print()

        val=score(dice)
        print("Your score for this round is:",val)
        if val==0:
            player.append(0)
            print("Sorry!!Better luck next time")
            return 0
        else:
            x=int(input("Do you want to continue??(1/0)"))
            if x==0:
                player.append(val)
                return 0
            else:
                rem=Dice_func2(dice)            #for the proceeding throws!!!#
                if rem==n:
                    player.append(val)
                    Dice_func3(rem)
                    return 0
                else:
                    player.append(val)
                    tap=n-rem
                    Dice_func3(tap)
                    return 0

#--------------FUNCTION 2------------

def Dice_func2(n):
    length=len(n)
    item=sorted(n)
    #import pdb; pdb.set_trace()
    result=0
    result1=0
    result2=0
    flag=length 
    i=0
    while i < length:
        if length>=3:
            if i+1<=length and i+2<length: 
                if item[i]==item[i+1] and item[i+1]==item[i+2]:
                    if item[i]==1:
                        result1+=3
                        flag=i
                        break
                    else:
                        result1+=3
                        flag=i
                        break
        if item[i] == 1:
            result1+=1

        if item[i] == 5:
            result1+=1    

        else:
            result1+=0

        i+=1    

    #checking after the triplet
    flag+=3
    if flag > length:
        return result1
    else:
        while flag < length:

            if item[flag] == 1:
                result2+=1

            if item[flag] == 5:
                result2+=1    

            else:
                result2+=0

            flag+=1    

        result=result1+result2
        return result



#--------------FUNCTION 1------------

def Dice_func1(n):
    dice=roll(n)
    i=0
    while i<n:
        print(dice[i]),
        i+=1
    print()

    val=score(dice)
    print ("Your score for this round is:",val)
    if val<300:
        print("Ooopss!!!!!!!Your Turn is over")
        player.append(0)
        return 0
    else:
        x=int(input("Do you want to continue??(1/0)"))
        if x==0:
            player.append(val)
            return 0
        else:
            rem=Dice_func2(dice)            #for the proceeding throws!!!#
            if rem==5:
                player.append(val)
                Dice_func3(rem)
                return 0
            else:
                player.append(val)
                tap=n-rem
                Dice_func3(tap)
                return 0



    
#--------------FUNCTION 4------------

def Dice_func4():
    Dice_func1(5)
    x=0
    fin=0
    t=len(player)
    if player[t-1]==0:
        fin=0
        while t>0:
            #print player[x],
            del player[x]
            t+=-1
    else:
        while t>0:
            fin+=player[x]
            #print player[x],
            del player[x]
            t+=-1
    return fin






#------------MAIN CLASS-------------
class Dice_Game():
    no=0 
    fin=0
    no=int(input("Enter Number of player: "))
    i=0
    if no < 2:
        print("Need minimum of 2 players to play the Game")
    else:
        num=no
        while num>0:
            scoreboard.append(0)
            num-=1

        while deck==0:
            i=0
            while i < no:
                print()
                print()
                print()
                print ("Player", i+1,"'s Turn")
                fin=Dice_func4()
                print()
                scoreboard[i]+=fin
                print ("Player", i+1,"'s total score is:",scoreboard[i])
                if scoreboard[i]>=1000:
                    deck=1
                    deckx=i
                    break
                else:
                    deck=0
                i+=1        
        if deck==1:
            print() 
            print()
            print()
            print ("========= FINAL ROUND =========")
            num=0
            while num<no:
                if num==deckx:
                    pass
                else:
                    print ()
                    print()
                    print()
                    print ("Player", num+1,"'s Turn")
                    fin=Dice_func4()
                    print()
                    print()
                    scoreboard[num]+=fin
                    print ("Player", num+1,"'s Total score is:",scoreboard[num])
                num+=1    
        y=0
        max=0
        print()
        print()
        print()
        print ("SCORE")
        while y<no:
            print ("Player",y+1,":",scoreboard[y])
            if scoreboard[y]>scoreboard[max]:
                max=y
            y+=1
        
        print ()
        print()
        print()
        print()
        print ("!!!!!!!!!!!WINNER!!!!!!!!!!!!")
        print()
        print  (          "PLAYER : ",max+1)
        print()
        print  (          "SCORE:",scoreboard[max])
