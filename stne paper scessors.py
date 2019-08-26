import random
import time
list = ["S","P","SC"]
comppoint = 0
yourpoint = 0

n=6
for j in range(7):
    print("enter your choice \n S-stone \n P-paper \n SC-secissor ")
    choice = input().upper()
    comp = random.choice(list)
    print(comp)

    if comp == choice:
        comppoint=comppoint+0
        yourpoint=yourpoint+0
    elif comp == "S" and choice == "SC":
        comppoint= comppoint+1
        print(f"its computer point as \nStone breaked scessiors")
    elif comp == "S" and choice == "P":
        yourpoint= yourpoint+1
        print(f"its your point as \nPaper rolled the stone in itself")
    elif comp == "P" and choice == "S":
        comppoint=comppoint+1
        print(f"its computer point as \nPaper rolled the stone in itself")
    elif comp == "P" and choice == "SC":
        yourpoint=yourpoint+1
        print(f"its your point as \nScessior cuted the paper")
    elif comp == "SC" and choice == "S":
        yourpoint=yourpoint+1
        print(f"its your point as \nStone breaked scessiors")

    elif comp == "SC" and choice == "P":
        comppoint=comppoint+1
        print(f"its computer point as \nScessior cuted the paper")

    print("No. of chances left",n-j)

    time.sleep(1)
print(f"yourpoints = {yourpoint}\ncomppoints = {comppoint}")
if comppoint>yourpoint:
    print("\nYou loose the game\n",comppoint-yourpoint,"\npoints")
elif comppoint<yourpoint:
    print("\nYou won the game\n",yourpoint-comppoint,"\npoints")
else:
    print("draw")



