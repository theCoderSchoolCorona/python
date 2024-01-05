class player():
    def __init__(self,name1,role1,hp1,mp1,protection1,ap1,level) -> None:
        self.role = role1
        self.name = name1
        self.level = level
        self.hp = hp1
        self.mp = mp1
        self.protection = protection1
        self.ap = ap1
class Enemies():
    def __init__(self,hp1,attack1,lvl,den,name) -> None:
        self.name2 = name
        self.hp2 = hp1
        self.attack2 = attack1
        self.lvl = lvl
        self.den = den
    def enemy_action(self):
        print(f"Hello, I'am {self.name2}")
