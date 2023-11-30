import random
def paper():
    print("    ________")
    print("   / ------ /")
    print("  / ______ /")
    print(" / PAPER  /")
    print("/________/")
    
def rock():
    print("   ___________________")
    print("  /                   |")
    print(" /                   /")
    print(" \                  /")
    print(" /  R  O  C  K      \\")
    print("/                    \\")
    print("|                     \\")
    print("\_______          _____\\")
    print("        \        /")
    print("         \______/")

def sci():
    print("    ________       ________")
    print("   / ____   /     / ____   /")
    print("  / /    / /     / /    / / ")
    print(" / /___ / /     / /___ / /")
    print("/________/_____/________/")
    print("    \       |        /")
    print("     \  SCIS|SORS   /")
    print("      \     |      /")
    print("       \    |     / ")
    print("        \  |  |  /")
    print("         \  |   /")
    print("          \ |  /")
    print("           \| /")
def rpslogic(a,b):
    # 0 is win # 1 is lose # 2 is draw
    if a==b:
        return 2
    if (a==2 and b==1) or (a==3 and b==2) or (a==1 and b==3):
        return 0
    else:
        return 1
def rpsinit():
    cnt=0
    print("1 : ROCK")
    print("2 : PAPER")
    print("3 : SCISSOR")
    print("enter 1 or 2 or 3")
    di={1:"ROCK",2:"PAPER",3:"SCISSOR"}
    du={1:"ROCK",2:"PAPER",3:"SCISSOR"}
    
    p1s=0
    p2s=0    
    while cnt<5:
        
        p1=int(input("Enter your move : "))
        p2=random.randint(1,3)
        result=rpslogic(p1,p2)
        print("YOU : ",di[p1])
        
        print("COMPUTER : ",di[p2])
        
        if result==0:
            print("You have won this shot")
            p1s=p1s+1
        if result==1:
            print("You have lost this shot")
            p2s=p2s+1
        if result==2:
            print("This is a draw shot")
        cnt=cnt+1

    print("*SCOREBOARD*")
    print("YOU : ",p1s,end="\t")
    print("COMPUTER : ",p2s)
    if p1s<p2s:
        print("**LOST**")
        print("Better luck Next time")
    if p1s>p2s:
        print("**WON**")
    if p1s==p2s:
        print("DRAW")
        
        
rpsinit()
