import random
x = input("Start a new game? (Answer 'Yes' or 'No)")

weapon = ["Green","Blue","Purple","Gold","Red"]
if x == "Yes":
    print("So first, we will give you a weapon so that you can fight with an NPC.")
    print("There are different kinds of weapon qualities.")
    print("Green is the worst, and then blue, purple, gold, and the red is the best.")
    print("Good luck!")
    def warrior():
        return random.randrange(0,5)
    def NPC():
        return random.randrange(0,5)
    r1 = warrior()
    r2 = NPC()
    print("Fighting...")
    if r1 > r2:
        print("You just defeat an enemy\'s {r1} weapon with {r2} weapon!".format(r1=weapon[r2],r2=weapon[r1]))
    else:
        print("HAHA,you lose! You lose with your {r1} weapon against enemy\'s {r2} weapon. Loser!".format(r1=weapon[r1],r2=weapon[r2]))
else:
    print("Bruh")