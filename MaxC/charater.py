import random
class player():
    def __init__(self,name1,role1,hp1,mp1,protection1,ap1,level,currentxp,given_stats) -> None:
        self.role = role1
        self.name = name1
        self.level = level
        self.hp = hp1
        self.mp = mp1
        self.currentmp = mp1
        self.currenthp = hp1
        self.protection = protection1
        self.ap = ap1
        self.xp = currentxp
        self.stats = given_stats    
class Enemies():
    def __init__(self,hp1,attack1,lvl,den,name) -> None:
        self.name2 = name
        self.hp2 = hp1
        self.currenthp = hp1
        self.attack2 = attack1
        self.lvl = lvl
        self.den = den
    def enemy_action(self,player,plrdenfense):
        chance1 = None
        if self.currenthp >= 0:
            chance1 = random.randint(0,100)
        elif chance1 >= 95:
            print("enemies' skill issue, he missed lol")
        else:
            if plrdenfense == False:
                player.hp2 -= random.randint(self.attack2,self.attack2+5)
                if player.currenthp <= 0:
                    playerdied = True
                    return playerdied
            else:
                player.hp2 -= round(random.randint(self.attack2,self.attack2+5) / 2)