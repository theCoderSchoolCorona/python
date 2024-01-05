import charater
import random
import json
roles = {"Wizard":[85,880,55,25],"Assualt":[100,110,65,75],"Medic":[85,550,65,35],"Tank":[350,125,500,55],"Mr.69":[99999999999999,999999999999999,999999999999999,999999999999999]}
eneimess = {"slime":[5,3,1,1],"Microsoft":[10,6,3],"Apple":[25,25,8,1],"dargon":[550,95,45,350],"mom":[15000,85000000,800,550000]}
usr_choice = input("choice a name:")
abc = None
YouFightingTo = None
eneimeslen = len(eneimess)
fighted = 1
allenemies = list(eneimess.keys())
    

while 0 == 0:
    usr_role_choice = input("choice ur role, including wizard, assualt, medic, tank or load a save")
    usr_role_choice = usr_role_choice.capitalize()
    if not usr_role_choice == "laod" and (usr_role_choice in roles):
        abc = charater.player(usr_choice,usr_role_choice,roles[usr_role_choice][0],roles[usr_role_choice][1],roles[usr_role_choice][2],roles[usr_role_choice][3],1)
        break
    else:
        print("try again")

while True:
    action = input("action: attack, eat, reset, shop, exit")
    if action == "attack":
        Targetenemies = random.randint(0,eneimeslen - 1)
        targetname = allenemies[Targetenemies]
        if eneimess[targetname][2] <= abc.player(abc.level):
            print(f"you're fighting {Targetenemies}!")
            
            YouFightingTo = charater.Enemies(eneimess[targetname[1]],eneimess[targetname[1]],eneimess[targetname[1]],eneimess[targetname[1]],targetname)
            actions = ["Denfense", "Attack", "Magic Attack", "Escape From Tarkov"]
            fighting = input("Denfense, Attak, Magic Attack, Escape from tarkov")
            fighting = fighting.capitalize()
            if fighting == "Denfense":
                pass
            elif fighting == "Attack":
                pass
            elif fighting == "Magic Attack":
                pass
            elif fighting == "Escape from tarkov":
                print("bruh")
                break
            else YouFightingTo. 
        
    if action == "exit":
        exit()