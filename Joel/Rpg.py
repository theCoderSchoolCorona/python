#importing from character.py
from character import *
import json
#import character
#print(dir(character))


#Main Variables:
saveData = {}
rested = True
decision = ""
inventory = []
memories = False
lastChoice = ""
atkType = ""


#Class Stats:
#Order of Parameters: health, strength, agility, intelligence
characterStats = {"warrior":[500,300,100,100], "ranger":[300,100,300,175], "sorcerer":[400,150,175,300]}
#level, health, strength, agi
enemyStats = {"Goblin":[10,600,150,150], "Bear":[15,1000,200,50]}
randomEvent = 0



#Loot Table:
lootTable = {"Trash":0,"Twig":0,"Broken Sword":1, "Gold Coin":5, "Stack of Gold Coins":10, "Green Gem":15, "Blue Gem":15, "Red Gem":15, "Yellow Gem":15,
                 "Rare Gem":20, "Diamond Necklace":25, "Giant Ruby":30, "Mysterious Flask":30, "Golden Apple":30, "Poisonous Apple":30, "Rare Sword":35,
                 "Suspicious Tablet":40, "Ancient Lighter":45, "Giant Bird Eggs":45, "Glowing Orbs":45, "Large Beast Egg":50, "New Cosmetic Set":75,
                 "New Cosmetic Weapon":75, "Treasure Box":75, "Giant Worm Egg":80, "Mysterious Sword":500, "Pet Dragon Egg":2000, "Blasphemous Eye":5000}
lootList = list(lootTable.keys())

#Food Table:
foodTable = ["Apple", "Bundle of Berries", "Deformed Fish", "Rabbit", "Cod", "Bass", "Salmon"]


#Loading:
try:
  with open("lastLoad.json", "r") as load:
    saveData = json.load(load)
    memories = True
except(FileNotFoundError):
  with open("lastLoad.json", "w") as load:

    #name process
    print("You find an ancient cup,")
    askName = input("""
    You decide to place your name into it, 
    what did you write?
    """)

    #class selection
    askStyle = input("""
    What kind of fighter are you?
      - Warrior
      - Ranger
      - Sorcerer
    """)
    askStyle = askStyle.lower()
    while(askStyle != "warrior" and askStyle != "ranger" and askStyle != "sorcerer"):
      print("Your choice is not of the options... Try again")
      askStyle = input("""
    What kind of fighter are you?
      - Warrior
      - Ranger
      - Sorcerer
    """)
      askStyle = askStyle.lower()
    
    #creating a player object for the first time
    saveData["playerObj"] = [askName, askStyle, characterStats[askStyle][0], characterStats[askStyle][1], characterStats[askStyle][2], characterStats[askStyle][3]]
    json.dump(saveData,load)




#Player Creation:
#obj below references the obj creation from the saveData dictionary

#player = character(askName, askStyle, characterStats[askStyle][0], characterStats[askStyle][1], characterStats[askStyle][2], characterStats[askStyle][3])
player = character(saveData["playerObj"][0], saveData["playerObj"][1], saveData["playerObj"][2], saveData["playerObj"][3], saveData["playerObj"][4], saveData["playerObj"][5])



#MEMORIES
if(memories == True):
  if(decision == "1"):
    lastChoice = "resting"
  elif(decision == "2"):
    lastChoice = "fighting"
  elif(decision == "3"):
    lastChoice = "eating"
  elif(decision == "4"):
    lastChoice = "searching"
  elif(decision == "5"):
    lastChoice = "looking at your items"
  elif(decision == "6"):
    lastChoice = "reviewing your aptitude"
  print(f""""
        Memories flow through your mind,
        You recall your name, it is {player.user}
        The fighting style you are familiar with are the ways of the {player.playerType}
        The last memories you had were {lastChoice}

        You orient yourself and remember your attributes:
        You have:
         - {str(player.currentHP)} Health
         - {str(player.power)} Strength
         - {str(player.agi)} Agility
         - {str(player.intel)} Intelligence""")



#Decision Menu:
while(decision != "100"):
  decision = str(input("""
      What is your choice?
      1. Rest
      2. Fight
      3. Eat
      4. Search
      5. Inventory
      6. Stats
      Type 100 to end the game
      """))
  
  #Main Checking

  #REST
  if(decision == "1"):
    print("You decided to rest")
    if(rested):
      if(player.currentHP < player.hp):
        player.currentHP = player.hp
        rested = False
        print(player.currentHP)
      else:
        print("Cannot Rest Now, Full Health Reached")
        print(player.currentHP)
    else:
      print("You've already rested")
      print(player.currentHP)


  #FIGHT    
  if(decision == "2"):
    enemies = list(enemyStats.keys())
    print(enemies)
    enemyPicker = enemies[randint(0,len(enemies)-1)]
    print(enemyPicker)
    opponent = enemy(enemyPicker, enemyStats[enemyPicker][0], enemyStats[enemyPicker][1], enemyStats[enemyPicker][2], enemyStats[enemyPicker][3])
    outcome = fight(player,opponent)
    rested = True
    if(outcome == "Fled"):
      print("You did not get an item")
    else:
      randomLoot = lootList[randint(0,len(lootList)-1)]
      inventory.append((str(randomLoot)))
      print("You got a " + str(randomLoot))


  #EAT
  if(decision == "3"):
    if(player.playerType == "warrior"):
      atkType = "str"
    elif(player.playerType == "ranger"):
      atkType = "agi"
    elif(player.playerType == "sorcerer"):
      atkType = "int"
    #add the check for food thing
  

  #SEARCH
  if(decision == "4"):
    print("This doesn't work yet")


  #INVENTORY
  if(decision == "5"):
    print(inventory)

  
  #STATS
  if(decision == "6"):
    print("This doesn't work yet")


  #Saving
  if(decision == "100"):
    saveData["playerObj"] = [askName, askStyle, player.currentHP, characterStats[askStyle][1], characterStats[askStyle][2], characterStats[askStyle][3]]
    saveData["rested"] = rested
    saveData["action"] = decision
    print(saveData)
    with open("lastLoad.json", "w") as load:
      json.dump(saveData,load)
    print("You have stopped the game")