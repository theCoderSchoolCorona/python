from random import *
class character:
  def __init__(self, name, style, health, strength, agility, intelligence):
    self.user = name
    self.playerType = style
    self.hp = health
    self.currentHP = health
    self.power = strength
    self.agi = agility
    self.intel = intelligence
  def changeName(self, newName):
    self.name = newName
    return(newName)
  def changeStyle(self,newPlayerType):
    self.playerType = newPlayerType
    return(newPlayerType)
  def changeHealth(self, change):
    self.currentHP = self.currentHP + change
    return(self.currentHP)
class enemy:
  def __init__(self, type, level, health, strength,agility):
    self.ty = type
    self.lvl = level
    self.hp = health
    self.currentHP = health
    self.str = strength
    self.agi = agility
def fight(character, enemy):
  battlemode = False
  askChoice = str(input("You've encountered an enemy, Attack (1), or Flee (2)"))
  while(character.currentHP > 0 and enemy.currentHP > 0):
    if(battlemode == False):
      print("A battle started")
      battlemode = True
    if(askChoice == "1"):

      if(character.agi > enemy.agi):
        if(character.playerType == "warrior"):
          damageDone = int((randint(9,11)*character.power)/10)
          enemy.currentHP -= damageDone
          print("You did " + str(damageDone) + " damage!")
          print("You have " + str(character.currentHP)+ "HP")
          print("Your enemy has " + str(enemy.currentHP)+ "HP")
        elif(character.playerType == "ranger"):
          damageDone = int((randint(9,11)*character.agi)/10)
          enemy.currentHP -= damageDone
          print("You did " + str(damageDone) + " damage!")
          print("You have " + str(character.currentHP)+ "HP")
          print("Your enemy has " + str(enemy.currentHP)+ "HP")
        elif(character.playerType == "sorcerer"):
          damageDone = int((randint(9,11)*character.intel)/10)
          enemy.currentHP -= damageDone
          print("You did " + str(damageDone) + " damage!")
          print("You have " + str(character.currentHP)+ "HP")
          print("Your enemy has " + str(enemy.currentHP)+ "HP")
          if(enemy.currentHP <= 0):
            print("You won the fight with " + str(character.currentHP) + "HP")
            return(None)
        damageDone = int((randint(9,11)*((.7*enemy.str)+(.3*enemy.agi)))/10)
        character.currentHP -= damageDone
        print("You took " + str(damageDone) + " damage!")
        print("You have " + str(character.currentHP)+ "HP")
        print("Your enemy has " + str(enemy.currentHP)+ "HP")
        if(character.currentHP <= 0):
          print("You Lost the battle")
          exit()
      else:
        damageDone = int((randint(9,11)*((.7*enemy.str)+(.3*enemy.agi)))/10)
        character.currentHP -= damageDone
        print("You took " + str(damageDone) + " damage!")
        print("You have " + str(character.currentHP)+ "HP")
        print("Your enemy has " + str(enemy.currentHP)+ "HP")
        if(character.currentHP <= 0):
          print("You Lost the battle")
          exit()
        if(character.playerType == "warrior"):
          damageDone = int((randint(9,11)*character.power)/10)
          enemy.currentHP -= damageDone
          print("You did " + str(damageDone) + " damage!")
          print("You have " + str(character.currentHP)+ "HP")
          print("Your enemy has " + str(enemy.currentHP)+ "HP")
        elif(character.playerType == "ranger"):
          damageDone = int((randint(9,11)*character.agi)/10)
          enemy.currentHP -= damageDone
          print("You did " +  str(damageDone) + " damage!")
          print("You have " + str(character.currentHP)+ "HP")
          print("Your enemy has " + str(enemy.currentHP)+ "HP")
        elif(character.playerType == "sorcerer"):
          damageDone = int((randint(9,11)*character.intel)/10)
          enemy.currentHP -= damageDone
          print("You did " + str(damageDone) + " damage!")
          print("You have " + str(character.currentHP)+ "HP")
          print("Your enemy has " + str(enemy.currentHP) + "HP")
        if(enemy.currentHP <= 0):
          print("You won the fight with " + str(character.currentHP) + "HP")
          xpgained = enemy.lvl*10
          print("hello")
          character.xp += xpgained
          print(f"""
                You gained {xpgained} XP!
                You have {character.xp} XP""")
          return("Victory")
    else:
      print("You've decided to take the easy way out, you fled the battle!")
      return("Fled")

