import random
import copy
import sys
import time
from collections import Counter
juF2 = 0
juI2 = 0
def Color():
    color = random.randint(1,4)
    if color == 1:
        f = "Heart"
    elif color == 2:
        f = "Spade"
    elif color == 3:
        f = "Diamond"
    elif color == 4:
        f = "Club"
    return f

def Card_Send_Machine(Ca):
    #Ca is Card Numbers
    Cards = {}
    b = 0
    n = "None"
    while len(Cards) < Ca:
        for i in range(1, 5):
        # One Push, X Cards
            a = random.randint(3,15)
            if a == 11:
                g = Color()
                n = "%s"%(g) + " Jack"
                b = {n:11}
            elif a == 12:
                g = Color()
                n = "%s"%(g) + " Queen"
                b = {n:12}
            elif a == 13:
                g = Color()
                n = "%s"%(g) + " King"
                b = {n:13}
            elif a == 14:
                g = Color()
                n = "%s"%(g) + " Ace"
                b = {n:15}
            elif a == 15:
                g = Color()
                n = "%s"%(g) + " 2"
                b = {n:16}
            else:
                g = Color()
                n = "%s"%(g) + " %s"%(a)
                b = {n:a}
            Cards.update(b)

            q = random.randint(1,54)
            if q == 16:
                b = {"JokerG":16}
                Cards.update(b)
            elif q == 17:
                b = {"JokerC":17}
                Cards.update(b)
    return Cards
#——————————————
CureCount = 3
ScoreF = 5
ScoreI = 5
Ice = []
Fire = []
class Robot:
    global Ice, Fire
    Cure = {}
    Curecard = {}
    def __init__(self, name, card, heart, group, pricenum, price):
        global Ice, Fire, Cure, Curecard
        self.name = name
        self.pricenum = pricenum
        self.price = price
        self.group = group
        self.card = Card_Send_Machine(card)
        self.Heart = heart




        if self.pricenum == 1:
            self.price = "No Gain."
        if self.pricenum == 2:
            self.price = "First Blood!"
        elif self.pricenum == 3:
            self.price = "Second Blood!"
        else:
            self.price = "Beast Blood!"
    def hurt(self):
        self.Heart -= 2

        print("Been Hurt")
        print("Health -2")
        print("Health:%s"% self.Heart)

    def cure(self):
        Cure = {}
        Curecard = {}
        for key, value in self.card.items():
            if "Heart" in key:
                Curecard[key] = value
                Cure.update(Curecard)
        #print(Cure)
        Z = []
        Zk = 0
        Zout = " "
        for i in Cure.values():
            Z.append(i)
        #print(Z)
        Zmin = min(Z)
        #print(Zmin)
        self.Heart += 2
        Zk = list(Cure.keys())[list(Cure.values()).index(Zmin)]
        if Zk != 0:
            self.card.pop(Zk)
        elif Zk == 0:
            print("Something Goes Wrong")
        print("━━━━━━")
        print(Zk)
        print("Been Cured")
        print("Health +2")
        print("Health:%s"% self.Heart)
        Z = []
        Cure = {}
        Curecard = {}

    def regroup(self):
        e = self.name in Fire
        p = self.name in Ice
        if e == True:
            self.group = "Fire"
        elif p == True:
            self.group = "Ice"
def DeGroup(Name):
    global Fire, Ice
    Player = [Name, "Bill", "Sara", "Jane", "Tony", "Mark"]
    random.shuffle(Player)
    Fire = []
    Ice = []
    for i in Player:
        if len(Player) > 3:
            Fire.append(i)
            Player.remove(i)
    Ice = Player
    return [Fire, Ice]
def One():
    B0 = " "
    print("Choose Your Enemy.")
    B0 = input("Write Down His Name:")
    if B0 == "Bill":
        BattleSys(C1,0)
    elif B0 == "Sara":
        BattleSys(C2,0)
    elif B0 == "Jane":
        BattleSys(C3,0)
    elif B0 == "Tony":
        BattleSys(C4,0)
    elif B0 == "Mark":
        BattleSys(C5,0)
    else:
        print("Wrong Name")
        One()
def AutoBattleSys(Cx, Cy):
    global C0, juF2, juI2
    S = 0
    K = 1
    Cxnum = 0
    Cynum = 0
    Cxcard0 = min(Cx.card, key=Cx.card.get)
    while S == 0:
        while K == 1:
            K = 2
            if len(Cx.card) > 3:
                Hfly = {}
                Hfly1 = {}
                time.sleep(1)
                print("%s's Epoch"% Cx.name)
                print(" ")
                time.sleep(1)
                for key, value in Cx.card.items():
                    if value > Cynum:
                        Hflykey = list(Cx.card.keys())[list(Cx.card.values()).index(value)]
                        # print Hflykey
                        Hfly1[Hflykey] = value
                        Hfly.update(Hfly1)
                        # print(Hfly)
                        # Change
                if Hfly == {}:
                    print("Can't Pay")
                    print("Pass")
                    Cx.hurt()
                    Lose1(Cx)
                    print("━━━━━━")
                    print("•┈┈┈┈┈•")
                    print(" ")
                    print(" ")
                    return
                else:
                    # print Hfly
                    CxOut = min(Hfly, key=Hfly.get)
                    Cxnum = Cx.card.get(CxOut)
                    Cx.card.pop(CxOut)
                    print("%s" %CxOut)
                    time.sleep(0.5)
                    print(" ")
                    print("┉┈")
                    print(" ")

            elif len(Cx.card) == 0:
                CxOut = max(Hfly, key=Hfly.get)
                Cxnum = Cx.card.get(CxOut)
                Cx.card.pop(CxOut)
                print("%s" %CxOut)
                if len(Cx.card) == 0:
                    print("He Has Won!")
                    Cxc = copy.deepcopy(Cx.name)
                    u = Cx.name in Fire
                    w = Cx.name in Ice
                    if u == True:
                        Fire.remove(Cx.name)
                        Fire.append("[Win]%s"% Cxc)
                        ScoreF += 15
                    elif w == True:
                        Ice.remove(Cx.name)
                        Ice.append("[Win]%s"% Cxc)
                        ScoreI += 15
                    return

            elif len(Cx.card) <= 3 and len(Cx.card) > 0:
                Hfly = {}
                Hfly1 = {}
                time.sleep(1)
                print("━━━━━━")
                print("%s's Epoch"% Cx.name)
                print(" ")
                time.sleep(1)
                for key, value in Cx.card.items():
                    if value > Cynum:
                        Hflykey = list(Cx.card.keys())[list(Cx.card.values()).index(value)]
                        # print Hflykey
                        Hfly1[Hflykey] = value
                        Hfly.update(Hfly1)
                        # print(Hfly)
                        # Change
                if Hfly == {}:
                    print("Can't Pay")
                    print("Pass")
                    Cx.hurt()
                    Lose1(Cx)
                    print("━━━━━━")
                    print("•┈┈┈┈┈•")
                    print(" ")
                    print(" ")
                    return
                else:
                # print Hfly
                    CxOut = max(Hfly, key=Hfly.get)
                    Cxnum = Cx.card.get(CxOut)
                    Cx.card.pop(CxOut)
                    print("%s" %CxOut)
                    print("━━━━━━")
                    if len(Cx.card) == 0:
                        print("He Has Won!")
                        Cxc = copy.deepcopy(Cx.name)
                        u = Cx.name in Fire
                        j = Cx.name in Ice
                        if u == True:
                            Fire.remove(Cx.name)
                            Fire.append("[Win]%s"% Cxc)
                            ScoreF += 15
                        elif j == True:
                            Ice.remove(Cx.name)
                            Ice.append("[Win]%s"% Cxc)
                            ScoreI += 15
                        print("━━━━━━")
                        return
        if Cy == C0:
            BattleSys(Cx, Cxnum)
            return

#inininin!
        while K == 2:
            K = 1
            if len(Cy.card) > 3:
                Hfly = {}
                Hfly1 = {}
                time.sleep(1)
                print("%s's Epoch"% Cy.name)
                print(" ")
                time.sleep(1)
                for key, value in Cy.card.items():
                    if value > Cxnum:
                        Hflykey = list(Cy.card.keys())[list(Cy.card.values()).index(value)]
                        # print Hflykey
                        Hfly1[Hflykey] = value
                        Hfly.update(Hfly1)
                        # print(Hfly)
                        # Change
                if Hfly == {}:

                    print("Can't Pay")
                    print("Pass")
                    Cy.hurt()
                    Lose1(Cy)
                    print("━━━━━━")
                    print("•┈┈┈┈┈•")
                    print(" ")
                    print(" ")
                    return
                else:
                    # print Hfly
                    CyOut = min(Hfly, key=Hfly.get)
                    Cynum = Cy.card.get(CyOut)
                    Cy.card.pop(CyOut)
                    print("%s" %CyOut)
                    print("━━━━━━")

            elif len(Cy.card) == 0:
                CyOut = max(Hfly, key=Hfly.get)
                Cynum = Cy.card.get(CyOut)
                Cy.card.pop(CyOut)
                print("%s" %CyOut)
                print("━━━━━━")
                if len(Cy.card) == 0:
                    print("He Has Won!")
                    Cyc = copy.deepcopy(Cy.name)

                    d = Cy.name in Fire
                    y = Cy.name in Ice
                    if d == True:
                        Fire.remove(Cy.name)
                        Fire.append("[Win]%s"% Cyc)
                        ScoreF += 15
                    elif y == True:
                        Ice.remove(Cy.name)
                        Ice.append("[Win]%s"% Cyc)
                        ScoreI += 15
                    print("━━━━━━")
                    print(" ")
                    return

            elif len(Cy.card) <= 3:
                Hfly = {}
                Hfly1 = {}
                time.sleep(1)
                print("━━━━━━")
                print("%s's Epoch"% Cy.name)
                print(" ")
                time.sleep(1)
                for key, value in Cy.card.items():
                    if value > Cxnum:
                        Hflykey = list(Cy.card.keys())[list(Cy.card.values()).index(value)]
                        # print Hflykey
                        Hfly1[Hflykey] = value
                        Hfly.update(Hfly1)
                        # print(Hfly)
                        # Change
                if Hfly == {}:
                    print("Can't Pay")
                    print("Pass")
                    Cy.hurt()
                    Lose1(Cy)
                    print("━━━━━━")
                    print("•┈┈┈┈┈•")
                    print(" ")
                    print(" ")
                    return
                else:
                    # print Hfly
                    CyOut = max(Hfly, key=Hfly.get)
                    Cynum = Cy.card.get(CyOut)
                    Cy.card.pop(CyOut)
                    print("%s" %CyOut)
                    print("━━━━━━")
                    if len(Cy.card) == 0:
                        print("He Has Won!")
                        Cyc = copy.deepcopy(Cy.name)

                        s = Cy.name in Fire
                        b = Cy.name in Ice
                        if s == True:
                            Fire.remove(Cy.name)
                            Fire.append("[Win]%s"% Cyc)
                            ScoreF += 15
                        elif b == True:
                            Ice.remove(Cy.name)
                            Ice.append("[Win]%s"% Cyc)
                            ScoreI += 15
                        print("━━━━━━")
                        print(" ")
                        return

def BattleSys(Cx, Enum):
    global Name, C0, CureCount, ScoreF, ScoreI, juF2, juI2

    Enemynum = Enum
    Outnum = 0
    K = 1
    q = 0
    z = 0
    t = 0
    while z == 0:
        while K == 1:
            K = 2
            if len(C0.card) > 0:

                if max(C0.card.values()) > Enemynum:
                    if CureCount > 0:
                        Choose = input("Attack Or Cured(%s)[A/C]:"%CureCount)
                    elif CureCount <= 0:
                        print("Attack, No Cured[A]")
                        Choose = "A"
                    if Choose == "A":
                        Out = input("Output Your Card(Or Pass):")
                        while t == 0:
                            Judge = Out in C0.card.keys()
                            if Judge == True:
                                if Outnum == 0:
                                    print("━━━━━━")
                                print("Your Epoch")
                                print(" ")
                                Outnum = C0.card.get(Out)
                                
                                if Outnum > Enemynum:
                                    if Outnum == 6:
                                        print("Bw.L: 'A Single Six, Retarded.'")
                                        print(" ")
                                    elif Outnum == 2:
                                        print("Bw.L: 'Treat Auntie With A Cup Of Cappuccino.'")
                                        print(" ")
                                    C0.card.pop(Out)
                                    print(Out)
                                    t = 1
                                else:
                                    print("Weaker Than His Card.")
                                    print("You Can Say Pass If You Can't Afford.")
                                    Out = input("Output Your Card(Or Pass):")
                            elif Judge == False:
                                if Outnum == 0:
                                    print("━━━━━━")
                                print("Your Epoch")
                                print(" ")
                                if Out == "Pass":
                                   C0.hurt()
                                   Lose1(Name)
                                   t = 1
                                else:
                                    print("The Right Pattern:")
                                    print("'Spade 8', 'Diamond Ace', 'JokerG'")
                                    print("Wrong Input,Write Again")
                                    Out = input("Output Your Card(Or Pass):")
                                    Judge = Out in C0.card.keys()
                            else:
                                print("WTF?")


                    else:
                        if CureCount > 0:
                            Choose = input("Cured(%s)[Y/N]:"%CureCount)
                            if Choose == "Y":
                                CureCount -= 1
                                C0.cure()
                            elif Choose == "N":
                                print("You Have Delay The Chance")
                                print("Pass")
                                pass
                        elif CureCount <= 0:
                            print("You Can't Cure")
                            print("Can't Afford")
                            print("Pass")
                            pass

            elif len(C0.card) == 0:
                print("You Have Win And Out")
                NameC = copy.deepcopy(Name)
                Name = "[Win]%s"% NameC
                
                r = Name in Fire
                m = Name in Ice
                if r == True:
                    ScoreF += 15
                    juF2 += 1
                elif m == True:
                    ScoreI += 15
                    juI2 += 1
        print("━━━━━━")
        print(" ")
        print("Your Card")
        print("══════")
        for i in C0.card.keys():
            print(i)
        print("══════")
        print(" ")

        while K == 2:
            K = 1
            t = 0
            if len(Cx.card) > 3:
                Hfly = {}
                Hfly1 = {}
                print("━━━━━━")
                print("%s Epoch"% Cx.name)
                print(" ")
                for key, value in Cx.card.items():
                    if value > Outnum:
                        Hflykey = list(Cx.card.keys())[list(Cx.card.values()).index(value)]
                        # print Hflykey
                        Hfly1[Hflykey] = value
                        Hfly.update(Hfly1)
                        # print(Hfly)
                        # Change
                if Hfly == {}:
                    print("Can't Pay")
                    print("Pass")
                    Cx.hurt()
                    Lose1(Cx)
                    return
                elif Hfly != 0:
                                # print Hfly
                    EnemyOut = min(Hfly, key=Hfly.get)
                    Enemynum = Cx.card.get(EnemyOut)
                    Cx.card.pop(EnemyOut)
                    print("%s" %EnemyOut)
                print(" ")
                print("┉┈")
                print(" ")
            elif len(Cx.card) == 0:
                print("━━━━━━")
                print("He Has Won!")
                al = Cx.name in Fire
                ap = Cx.name in Ice
                if al == True:
                    Fire.remove(Cx.name)
                    Fire.append("[Win]%s"% Cxc)
                    ScoreF += 15
                    juF2 += 1
                elif ap == True:
                    Ice.remove(Cx.name)
                    Ice.append("[Win]%s"% Cxc)
                    juI2 += 1
                    ScoreI += 15

                return

            elif len(Cx.card) <= 3:
                Hfly = {}
                Hfly1 = {}
                print("━━━━━━")
                print("%s Epoch"% Cx.name)
                print(" ")
                for key, value in Cx.card.items():
                    if value > Outnum:
                        Hflykey = list(Cx.card.keys())[list(Cx.card.values()).index(value)]
                        # print Hflykey
                        Hfly1[Hflykey] = value
                        Hfly.update(Hfly1)
                        # print(Hfly)
                        # Change
                    if Hfly == {}:
                        print("Can't Pay")
                        print("Pass")
                        Cx.hurt()
                        Lose1(Cx)
                        return
                    else:
                        # print Hfly
                        EnemyOut = max(Hfly, key=Hfly.get)
                        Enemynum = Cx.card.get(EnemyOut)
                        Cx.card.pop(EnemyOut)
                        print("%s" %EnemyOut)
                        print(" ")
                        print("┉┈")
                        print(" ")
                        if len(Cx.card) == 0:
                            print("━━━━━━")
                            print("He Has Won!")
                            Cxc = copy.deepcopy(Cx.name)

                            ep = Cx.name in Ice
                            ad = Cx.name in Fire
                            if ad == True:
                                Fire.remove(Cx.name)
                                Fire.append("[Win]%s"% Cxc)
                                ScoreF += 15
                                juF2 += 1
                            elif ep == True:
                                Ice.remove(Cx.name)
                                Ice.append("[Win]%s"% Cxc)
                                juI2 += 1
                                ScoreI += 15
                            print("━━━━━━")
                            return




def Lose1(Name):
    global ScoreF, ScoreI
    ag = Name in Fire
    dp = Name in Ice
    if ag == True:
        ScoreF -= 1
    elif dp == True:
        ScoreI -= 1
def Price(epoch):
    pass
def DeathTest(Cx):
    global juF, juI
    if Cx.Heart == 0:
        print("%s Have Dead"%Cx.name)
        a = Cx.name in Fire
        b = Cx.name in Ice
        if a == True:
            Fire.remove(Cx.name)
            Fire.append("[Lose]%s"% Cx.name)
            ScoreF -= 10
            juF += 1
        elif b == True:
            Ice.remove(Cx.name)
            Ice.append("[Lose]%s"% Cx.name)
            ScoreI -= 10
            juI += 1
        result = 1
    else:
        result = 0
    return result
def All(Cx):
    Mycard = " "
    Mycardnum = 0
    global public, C0, C1, C2, C3, C4, C5
    sl = 1
    if Cx == C0:
        while Cx == C0 and sl == 1:
            Pubcard = input("Output Your Card:")
            print(" ")
            ju = Pubcard in Cx.card.keys()
            if ju == True:
                sl = 0
            elif ju == False:
                print("Wrong Input, Input Again")
                sl = 1


    elif Cx != C0:
        Pubcard = max(Cx.card, key=Cx.card.get)
    PublicList = [C0, C1, C2, C3, C4, C5]
    PublicList.remove(Cx)
    Public = Pubcard
    print(Pubcard)
    print("━━━━━━")
    Hfly = {}
    Hflys = {}
    for i in PublicList:
        Pubcardnum = Cx.card.get(Pubcard)

        print("%s's Epoch"%i.name)
        print(" ")
        if Pubcardnum >= max(i.card.values()):
            i.hurt()
            Lose1(i)
            print("%s Health:%s"%(i.name, i.Heart))
            print("━━━━━━")
            pass
        elif Pubcardnum < max(i.card.values()):
            if i != C0:
                for key ,value in i.card.items():
                    if value > Pubcardnum:
                        Hflys[key] = value
                        Hfly.update(Hflys)
                Outcard = min(Hfly, key=Hfly.get)
                print(Outcard)
                print("━━━━━━")
                print(" ")
                i.card.pop(Outcard)
                return i
                #i take it down, the next epoch is i
            elif i == C0:
                k = 0

                Mycard = input("Output Your Card(Or Pass):")
                if Mycard == "Pass":
                    C0.hurt()
                    Lose1(C0)
                    pass
                else:
                    Mycardnum = C0.card.get(Mycard)

                while Mycardnum < Pubcardnum and k != 1 and Mycard != "Pass":
                    Mycard = input("Wrong Input, Input Again(Or Pass):")

                    if Mycard == "Pass":
                        k = 1
                        C0.hurt()
                        Lose1(C0)
                        pass
                    else:
                        Mycardnum = C0.card.get(Mycard)

                if Mycardnum > Pubcardnum:
                    C0.card.pop(Mycard)
                    print(Mycard)
                    print("━━━━━━")
                    print(" ")
                    print("══════")
                    for c in C0.card.keys():
                        print(c)
                    print("══════")
                    return
#Select Options
def Sel(Cx):
    Cy = 0
    global C0,C1,C2,C3,C4,C5
    Namedict = {C0:Name, C1:C1.name, C2:C2.name, C3:C3.name, C4:C4.name, C5:C5.name}
    if Cx.group == "Fire":
        random.shuffle(Ice)
        Cyname = Ice[1]
        Cy = list(Namedict.keys())[list(Namedict.values()).index(Cyname)]
    elif Cx.group == "Ice":
        random.shuffle(Fire)
        Cyname = Fire[1]
        Cy = list(Namedict.keys())[list(Namedict.values()).index(Cyname)]
    c = random.randint(1,4)
    if c == 1:
        print(" ")
        print("•┈┈┈┈┈•")
        print("[One Damage]")
        print("━━━━━━")

        AutoBattleSys(Cx, Cy)
    elif c == 2 or c == 3 or c == 4:
        print(" ")
        print("•┈┈┈┈┈•")
        print("[All Damage]")
        print("━━━━━━")

        print("%s's Epoch"%Cx.name)
        print(" ")
        All(Cx)
def Cardlist(C0):
    print(" ")
    print("Your Card")
    print("══════")
    for i in C0.card.keys():
        print(i)
    print("══════")
    print(" ")
def AutoCure(Cx):
    if Cx.Heart < 10:
        Cx.cure()
    else:
        return
#——————————————
Name = input("Give Me Your Name:")
C0 = Robot(Name, 15, 20, 0, 1, 0)
C1 = Robot("Bill", 15, 20, 0, 1, " ")
C2 = Robot("Sara", 15, 20, 0, 1, " ")
C3 = Robot("Jane", 15, 20, 0, 1, " ")
C4 = Robot("Tony", 15, 20, 0, 1, " ")
C5 = Robot("Mark", 15, 20, 0, 1, " ")
DeGroup(Name)
C0.regroup()
C1.regroup()
C2.regroup()
C3.regroup()
C4.regroup()
C5.regroup()
#——————————————
Cure1 = 3
Cure2 = 3
Cure3 = 3
Cure4 = 3
Cure5 = 3
#——————————————
public = 0
Double = False
#Public Kill
choose = input("Gun Or Porker:[G/P]")
if choose == "G":
    juF = 0
    juI = 0
    if Name == "Zack":
        Great = {"Spade Zack":18}
        C0.card.update(Great)
    print("[Game Start]")
    print("━━━━━━")
    print("Team Fire:")
    print(Fire)
    print("Score: %s"%ScoreF)
    print("━━━━━━")
    print("Team Ice:")
    print(Ice)
    print("Score: %s"%ScoreI)
    print("━━━━━━")

    # My Epoch
    M = 0
    Game = "Start"
    while Game == "Start":
        while M == 0:
            print(" ")
            print("Your Card")
            print("══════")
            for i in C0.card.keys():
                print(i)
            print("══════")
            print(" ")
            Choice = input("Beat One Man, Or Beat All Man:[O/A/P]")
            if Choice == "O":
                One()
                M = 1
            elif Choice == "A":
                All(C0)
                M = 1
            elif Choice == "P":
                A = input("Are You Sure To Pass:[Y/N]")
                if A == "Y":
                    M = 1
                    pass
                elif A == "N":
                    M = 0
        while Choice != "A" and Choice != "O" and Choice != "P":
            print("Wrong Input, Input Again")
            Choice = input("Beat One Man, Or Beat All Man:[O/A]")
            if Choice == "O":
                One()
            elif Choice == "A":
                All(C0)

        Sel(C1)
        if Cure1 > 0:
            AutoCure(C1)
            Cure1 -= 1
        DeathTest(C1)
        Sel(C2)
        if Cure2 > 0:
            AutoCure(C2)
            Cure2 -= 1
        DeathTest(C2)
        Sel(C3)
        if Cure3 > 0:
            AutoCure(C3)
            Cure3 -= 1
        DeathTest(C3)
        Sel(C4)
        if Cure4 > 0:
            AutoCure(C4)
            Cure4 -= 1
        DeathTest(C4)
        Sel(C5)
        if Cure5 > 0:
            AutoCure(C5)
            Cure5 -= 1
        DeathTest(C5)
        print("━━━━━━")

        print("Team Fire:")
        print(Fire)
        print("Score: %s"%ScoreF)
        print("━━━━━━")
        print("Team Ice:")
        print(Ice)
        print("Score: %s"%ScoreI)
        print("━━━━━━")
        print(" ")
        if juF >= 3:
            print("[Game End]")
            print("Fire Group Has Lost")
            print("[Winner Is Ice]")
            print("Team Fire:")
            print("Score: %s"%ScoreF)
            print("━━━━━━")
            sys.exit()
        if juI >= 3:
            print("[Game End]")
            print("Ice Group Has Lost")
            print("[Winner Is Fire]")
            print("Team Ice:")
            print("Score: %s"%ScoreI)
            print("━━━━━━")
            sys.exit()
        if juF2 + juF >= 3 or juI2 + juI >= 3:
            print("[Game End]")
            if juF2 - juF > juI2 - juI:
                print("Fire Group Is Winner")
            elif juF2 - juF < juI2 - juI:
                print("Ice Group Is Winner")
            elif juF2 - juF == juI2 - juI:
                print("Two Group Are Equle")
                print("Great Balance, Isn't It?")
        print("[Next Round]")
        print(" ")
        print("Your Card")
        print("══════")
        for i in C0.card.keys():
            print(i)
        print("══════")
        print(" ")


elif choose == "P":
    A = Card_Send_Machine(38)
    H = []
    H2 = []
    for i in range(15):
        H1 = A.popitem()
        Hk = list(H1)
        H2.append(Hk)
    H = dict(H2)
    Y = A
    print("[Game Start]")
    print(" ")
    print("Your Cards")
    print("══════")
    for i in Y.keys():
        print(i)
    print("══════")
    #---------------------------------------
    keyreal = 0
    #countdown = 1000
    epoch = 1
    wrong = 0
    Bombt = 3
    Bombth = 3
    while epoch == 1:
        k = random.randint(1,2)
        if k == 1:
            if wrong > 0:
                print("The Last Time's Card Name Was Wrong")
                print("And The Right One Should Be Like: 'Spade 5' ")
            print(" ")
            print("━━━━━━")
            print("You Go First")
            print(" ")
            C = input("Push out Your Card:")
            
            Cnum = Y.get(C)
            ju = C in Y.keys()
            if ju == True:
                Y.pop("%s" %C)
                epoch += 1
                wrong = 0
                k = 1

        elif k == 2:
            print(" ")
            print("━━━━━━")
            print("He Go First")
            print(" ")
            Cp = min(H, key=H.get)
            Cpnum = H.get(Cp)
            H.pop("%s" %Cp)
            print("%s" %Cp)
            # print H
            # Change
            epoch += 1

    while epoch > 1:
        key_list = []
        keylist = []
        valub = 0
        epoch += 1
        al = 1
        if k == 1:
            #al = 1
            #if countdown == 1:
                #al = random.randint = (0,5)
                #print("Count down: %d" % al)
            #if al == 0:
                #Ohla = 0
                #while Ohla < 1000:
                    #Ohla += 1
                    #print("Ohla")
                #print(" ")
                #print("He Died in Blood Pool")
                #print("Killer Quueem! You Win.")
                #sys.exit()
            k = 2
            Kills = []
            Kills = H.values()
            Killb = dict(Counter(Kills))
            Killv = Killb.values()
            if len(Killb) == 0:
                pass
            else:
                o = random.randint(1,3)
                if Double == True:
                    pass
                elif Double == False:
                    if o == 2:
                        print("━━━━━━")                        
                        Bombth -= 1
                        if Bombth <= 0:
                            Bombth = 0
                            Double = False
                            print("He Tried To Use Bomb, But Failed.")
                            print(" ")
                        elif Bombth > 0:
                            print("Boom! He destroyed Your Cards.")
                            print(" ")
                            Double = True
                            Dt = max(Killv)
                            if Dt == 1 or Dt == 0:
                                Double = False
                            else:
                                Cd = 0
            if Double == True:
                #
                keyHdea = []
                keyreal = 0
                values = H.values()
                keyb = dict(Counter(values))
                for key, value in keyb.items():
                    if value == Dt:
                        if key > Cd:
                            keylist.append(key)
                if len(keylist) > 0:
                    keyreal = min(keylist)                    
                    for i in range(1, Dt+1):
                        keyHdea = list(H.keys())[list(H.values()).index(keyreal)]
                        print(keyHdea)
                        H.pop(keyHdea)
                        Double = True
                        Cd = 0
                        k = 2

                elif len(keylist) == 0:
                    print("Can't Pay")
                    print("Pass")
                    Cp = min(H, key=H.get)
                    Cpnum = 0
                    Cd = 0
                    Double = False
                    epoch += 1
                    k = 2

                else:
                    print("Can't Pay")
                    print("Pass")
                    Cp = min(H, key=H.get)
                    Cpnum = 0
                    Cd = 0
                    Double = False
                    epoch += 1
                    k = 2

            elif Double == False:
                if len(H) > 3:
                    Hfly = {}
                    Hfly1 = {}
                    print("━━━━━━")
                    print("His Epoch")
                    print(" ")
                    for key, value in H.items():
                        if value > Cnum:
                            Hflykey = list(H.keys())[list(H.values()).index(value)]
                            # print Hflykey
                            Hfly1[Hflykey] = value
                            Hfly.update(Hfly1)
                            # print(Hfly)
                            # Change
                    if Hfly == {}:
                        print("Can't Pay")
                        print("Pass")
                        Cp = min(H, key=H.get)
                        Cpnum = 0
                        epoch += 1
                        k = 2
                    else:
                        # print Hfly
                        Cp = min(Hfly, key=Hfly.get)
                        Cpnum = H.get(Cp)
                        H.pop(Cp)
                        print("%s" %Cp)
                        epoch += 1
                        k = 2
                        LenH = len(H)
                        if LenH == 0:
                            print("He Wins!")
                            print("Oh, Such A Pity.")
                            sys.exit()
                elif len(H) <= 3:
                    Hfly = {}
                    Hfly1 = {}
                    print("━━━━━━")
                    print("His Epoch")
                    print(" ")
                    for key, value in H.items():
                        if value > Cnum:
                            Hflykey = list(H.keys())[list(H.values()).index(value)]
                            # print Hflykey
                            Hfly1[Hflykey] = value
                            Hfly.update(Hfly1)
                            # print(Hfly)
                            # Change
                    if Hfly == {}:
                        print("Can't Pay")
                        print("Pass")
                        Cp = min(H, key=H.get)
                        Cpnum = 0
                        epoch += 1
                        k = 2
                    else:
                        # print Hfly
                        Cp = max(Hfly, key=Hfly.get)
                        Cpnum = H.get(Cp)
                        H.pop(Cp)
                        print("%s" %Cp)
                        epoch += 1
                        k = 2
                        LenH = len(H)
            if len(H) == 0:
                print("He Wins!")
                print("Oh, Such A Pity.")
                sys.exit()
        elif k == 2:
            k = 1
            epoch += 1
            #al = 1
            #if countdown == 1:
                #al = random.randint(0, 5)
                #print("Count down: %d" % al)
            #if al == 0:
                #Ohla = 0
                #while Ohla < 1000:
                    #Ohla += 1
                    #print("OhLa")
                #print(" ")
                #print("You were Mudered, Death Body in the Bloody Pool")
                #print("Killer Quueem! He Win.")
                #sys.exit()
            Yfly = {}
            print("━━━━━━")
            print("Your Epoch")
            print(" ")
            print("Your Cards")
            
            print("══════")            
            for i in Y.keys():
                print(i)
            print("══════")
            Cm = max(Y.values())
            Cpm = max(H.values())
            if Double == False:
                if Cm > Cpnum:
                    if Bombt > 0:
                        C = input("Push Out Your Card(Or Pass)(Or Bomb[%s]):" % Bombt)
                        if C == "Bomb":
                            Bombt -= 1
                        elif C == "Wh1t3zZ":
                            Bombt = 100
                            C = input("Push Out Your Card(Or Pass)(Or Bomb[%s]):" % Bombt)
                    elif Bombt <= 0:
                        C = input("Push Out Your Card(Or Pass):")
                        Bombt = 0
                        while C == "Bomb":
                            print("You Just Use Up the Bombs.")
                            C = input("Push Out Your Card not Bomb(Or Pass):")
                    if C == "Wh1t3zZ":
                        print("Ok,You beat it Down By 17 Cards")
                        print("You Win! Gambing Ghost")
                        sys.exit()
                    elif C == "Pass":
                        k = 1
                    elif C == "Bomb":
                        k = 1
                        Double = True
                        Cnum = 0
                        print("The Bomb should be input as '3' or 'King' or 'Joker'")
                        Cd = input("Push Out Your Bomb:")
                        if Cd == "Jack":
                            Cd = 11
                        elif Cd == "Queen":
                            Cd = 12
                        elif Cd == "King":
                            Cd = 13
                        elif Cd == "Ace":
                            Cd = 14
                        elif Cd == "2":
                            Cd = 15
                        elif Cd == "Joker":
                            Cd = 16
                        #elif Cd == "Killer Queen":
                            #Cd = 17
                            #print("Bite The Dust!")
                            #countdown = 1
                        else:
                            Cd = int(Cd)
                        #if Cd == 17:
                            #Dt = 0
                            #Y.clear()
                            #asl = {"Killer Queen":19}
                            #Y.update(asl)
                        Dt = input("How Many Cards in One Bomb Pair:")
                        Dt = int(Dt)
                        Dfly = {}
                        Dfly1 = {}
                        Yt = copy.deepcopy(Y)
                        for key, value in Yt.items():
                            if value == Cd:
                                Dflykey = list(Y.keys())[list(Y.values()).index(value)]
                                Y.pop(Dflykey)
                                # print Hflykey
                                Dfly1[Dflykey] = value
                                Dfly.update(Dfly1)
                        if len(Dfly) > 1:
                            while len(Dfly) < Dt:
                                #
                                print("Wrong Enter, Please input Again")
                                Dt = input("How Many Cards in One Bomb Pair:")
                                Dt = int(Dt)
                                Yt = copy.deepcopy(Y)
                                for key, value in Yt.items():
                                    if value == Cd:
                                        Dflykey = list(Y.keys())[list(Y.values()).index(value)]
                                        Y.pop(Dflykey)
                                        # print Hflykey
                                        Dfly1[Dflykey] = value
                                        Dfly.update(Dfly1)
                            Dflycop = copy.deepcopy(Dfly)
                            for i in range(1, Dt+1):
                                Dfly.popitem()
                            if Cd > keyreal:
                                Dflyar = dict(Counter(Dflycop) -Counter(Dfly))
                                for key in Dflyar.keys():
                                    print(key)
                                Double = True
                                Y.update(Dfly)
                                k = 1
                            elif Cd <= keyreal:
                                Double = True
                                print("Wrong Bomb, Weaker Than His Bomb")
                                Y.update(Dflycop)
                                k = 2
                        Dflycop = copy.deepcopy(Dfly)
                        if len(Dflycop) == 1:
                            Double = False
                            Cnum = 0
                            k = 1
                    else:
                        Cnum = Y.get(C, "Not in Your Cards")
                        je = C in Y.keys()
                        if je == True:
                            if Cnum > Cpnum:
                                Y.pop(C)
                                print("%s" %C)
                                k = 1
                            elif Cnum <= Cpnum:
                                print("No Cheating.")
                                print("If You Can't Afford it, Just text 'Pass'")
                                C = input("Push The Right Card Name(or Pass):")
                                if C == "Pass":
                                    k = 1
                                else:
                                    Cnum = Y.get(C)
                                    if Cnum > Cpnum:
                                        Y.pop(C)
                                        print("%s" %C)
                                        k = 1
                                    else:
                                        print("Never Do Card Trick!")
                                        print("Next Time, Do Cheat with some Other Ways, OK?")
                                        sys.exit()
                        elif je == False:
                            if C == "Pass":
                                je = True
                                k = 1
                                C = C = min(Y, key=Y.get)
                                Cnum = 0
                            else:
                                print("Attention!")
                                print("Input Card like 'Spade Ace' or Pass")
                                C = input("Push The Right Card Name:")
                                Cnum = Y.get(C, "Not in Your Cards")
                                if C == "" or " ":
                                    je = False
                                else:
                                    je = C in Y.keys()
                                    if je == True:
                                        Cnum = Y.get(C)
                                        if Cnum > Cpnum:
                                            Y.pop(C)
                                            print("%s" %C)
                                            epoch += 1
                                            k = 1
                                        else:
                                            print("Weaker Than His Card, Boy Next Door!")
                                            print("You Have Been Beaten Down By Wilington")
                                            sys.exit()
                                    else:
                                        print("Too Much Mistakes")
                                        sys.exit()
                elif Cm <= Cpnum:
                    print("Can't Pay")
                    print("Pass")
                    C = min(Y, key=Y.get)
                    Cnum = 0
                    epoch += 1
                    k = 1
                LenY = len(Y)
                if LenY == 0:
                    print("━━━━━━")
                    print("You Win!")
                    print("Scores Beauty!")
                    print("━━━━━━")
                    sys.exit()

            elif Double == True:
                Cnum = 0
                Cd = input("Push Out Your Bomb(or Pass):")
                if Cd == "Pass":
                    k = 1
                    Double = False
                    Cd = 0
                    keyreal = 0
                else:
                    if Cd == "Jack":
                        Cd = 11
                    elif Cd == "Queen":
                        Cd = 12
                    elif Cd == "King":
                        Cd = 13
                    elif Cd == "Ace":
                        Cd = 14
                    elif Cd == "2":
                        Cd = 15
                    elif Cd == "Joker":
                        Cd = 16
                    #elif Cd == "Killer Queen":
                        #Cd = 17
                        #countdown = 1
                        #print("Bite The Dust!")
                        #Y.clear()
                        #asl = {"Killer Queen":19}
                        #Y.update(asl)
                    else:
                        Cd = int(Cd)
                    Dfly = {}
                    Dfly1 = {}
                    Yt = copy.deepcopy(Y)
                    Yb = copy.deepcopy(Y)
                    for key, value in Yt.items():
                        if value == Cd:
                            Dflykey = list(Y.keys())[list(Y.values()).index(value)]
                            Y.pop(Dflykey)
                            # print Hflykey
                            Dfly1[Dflykey] = value
                            Dfly.update(Dfly1)
                    if len(Dfly) > 1:
                        while len(Dfly) < Dt:
                            Y = Yb
                            print("Wrong Enter")
                            Cnum = 0
                            print("Throw Out Your Bomb Onto His Face!")
                            Cd = input("Push Out Your Bomb(or Pass):")
                            if Cd == "Pass":
                                k = 1
                                Double = False
                                Cd = 0
                                keyreal = 0
                            else:
                                if Cd == "Jack":
                                    Cd = 11
                                elif Cd == "Queen":
                                    Cd = 12
                                elif Cd == "King":
                                    Cd = 13
                                elif Cd == "Ace":
                                    Cd = 14
                                elif Cd == "2":
                                    Cd = 15
                                elif Cd == "Joker":
                                    Cd = 16
                                #elif Cd == "Killer Queen":
                                    #Cd =17
                                    #countdown = 1
                                    #print("Bite The Dust!")
                                    #Y.clear()
                                    #asl = {"Killer Queen":19}
                                    #Y.update(asl)
                                else:
                                    Cd = int(Cd)
                                Dfly = {}
                                Dfly1 = {}
                                Yt = copy.deepcopy(Y)
                                Yb = copy.deepcopy(Y)

                                for key, value in Yt.items():
                                    if value == Cd:
                                        Dflykey = list(Y.keys())[list(Y.values()).index(value)]
                                        Y.pop(Dflykey)
                                        # print Hflykey
                                        Dfly1[Dflykey] = value
                                        Dfly.update(Dfly1)

                        Dflycop = copy.deepcopy(Dfly)
                        for i in range(1, Dt+1):
                            Dfly.popitem()
                        if Cd > keyreal:
                            Dflyar = dict(Counter(Dflycop) - Counter(Dfly))
                            for key in Dflyar.keys():
                                print(key)
                            Double = True
                            Y.update(Dfly)
                            k = 1
                        elif Cd <= keyreal:
                            Double = True
                            print("Wrong Bomb, Weaker Than His Bomb")
                            Y.update(Dflycop)
                            k = 2
                            keyreal = 0
                    elif len(Dfly) <= 1:
                        print("Can't Pay")
                        print("Pass")
                        H.update(Dfly)
                        Cp = min(H, key=H.get)
                        Cpnum = 0
                        Double = False
                        Cnum = 0
                        keyreal = 0
                        epoch += 1
                        k = 1
else:
    print("Wrong Input")
    print("Please Input G or P")
    
           