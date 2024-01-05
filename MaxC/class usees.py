class Fornite():
    members = ""
    def __init__(self,members):
        self.members = members
    def speak(self):
        print("im apart of family")
class Member(Fornite):
    def __init__(self, name):
        super().__init__(name)
    def adding(number,name,nameb):
        ou = (name,nameb,number)
p = input("first name")
o = input("last game")
i = input("number")

Member.adding(p,o,i)
print(Member)