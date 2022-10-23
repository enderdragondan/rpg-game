#Libraries
import os
import random
from replit import db

#Variables (I HATE GLOBAL VARIABLES AFTER MAKING THIS HOW DO THEY WORK)
health = 0 #Player Health
maxhealth = 20 #Player Max Health
attack = 0 #Player Attack
lvl = 0 #Player Level
name = "" #Player Name
coins = 0 #Player Coins
infhealth = False #Infinite Health
infattack = False #Infinite Attack
inflvl = False #Infinite Levels
infcoins = False #Infinite Coins
hpotions = 0 #Health Potions
dpotions = 0 #Damage Potions
gamecompleted = False #Player is Dead or not


def mainmenu():
  #Adds all the variables to the function
  global health
  global maxhealth
  global attack
  global lvl
  global name
  global coins
  global hpotions
  global dpotions
  global infhealth
  global infattack
  global inflvl
  global infcoins
  global hpotions
  #Very start of the game. nice
  os.system('clear')
  print("""Welcome to RPG Game!
  1. New Game
  2. Load Game
  3. Settings""")
  menuinput = input("Choose 1, 2 or 3: ")
  while menuinput not in ("1", "2", "3"):
    print("Invalid Input")
    menuinput = input("Choose 1, 2 or 3: ")
  #Starts a new game
  if menuinput == "1":
    newgame()
  #Loads a game from a save file
  elif menuinput == "2":
    loadgame()
  #THE SETTINGS MENU OOOOO
  else:
    settings()
    mainmenu()


def newgame():
  #Adds variables to the function again (help)
  global health
  global maxhealth
  global attack
  global lvl
  global name
  global coins
  global hpotions
  global dpotions
  global infhealth
  global infattack
  global inflvl
  global infcoins
  #Depending on what you chose in the settings these will change (mostly for me for testing but also fun to play)
  #I probably could have just used contant variables for this but OH WELL TOO LATE
  if infhealth == True:
    health = 9999
    maxhealth = 9999
  else:
    health = 20
  if infattack == True:
    attack = 9999
  else:
    attack = 1
  if inflvl == True:
    lvl = 9999
  else:
    lvl = 1
  if infcoins == True:
    coins = 9999
  else:
    coins = 0
  #Asks for your name for literally no reason at all (until I add saving and loading multiple save files)
  os.system('clear')
  name = input("What is your name?: ")

def loadgame():
  global health
  global maxhealth
  global attack
  global lvl
  global name
  global coins
  global hpotions
  global dpotions
  global infhealth
  global infattack
  global inflvl
  global infcoins
  loading = True
  failed = False
  while loading == True:
    os.system('clear')
    savename = input("Enter the name of your save file: ").lower()
    if savename in db:
      health = db[savename+"health"]
      maxhealth = db[savename+"maxhealth"]
      attack = db[savename+"attack"]
      lvl = db[savename+"lvl"]
      name = db[savename+"name"]
      coins = db[savename+"coins"]
      hpotions = db[savename+"hpotions"]
      dpotions = db[savename+"dpotions"]
      infhealth = db[savename+"infhealth"]
      infattack = db[savename+"infattack"]
      inflvl = db[savename+"inflvl"]
      infcoins = db[savename+"infcoins"]
      loading = False
      print("Game Successfully loaded with the name",savename)
      input("Press Enter to Continue")
    else:
      os.system('clear')
      print("Game save not found. ")
      input("Press Enter to return to Main Menu")
      mainmenu()

def settings():
  #This whole menu probably could have been done a way simpler way but I like things the complicated way (just kidding I wish i knew the the simple way)
  settingsinput = ""
  #These are for displaying the different "Infinite ______ Toggled" messages
  ih = 0
  ia = 0
  il = 0
  ic = 0
  while settingsinput != "5":
    #Adds the variables to the function AGAIN
    global infhealth
    global infattack
    global inflvl
    global infcoins
    os.system('clear')
    print("Settings:")
    print("  1. Infinite Health:", infhealth)
    print("  2. Infinite Attack:", infattack)
    print("  3. Infinite Levels:", inflvl)
    print("  4. Infinite Coins:", infcoins)
    print("  5. Back to Main Menu")
    if ih == 1:
      print("Infinite Health Toggled")
    elif ia == 1:
      print("Infinite Attack Toggled")
    elif il == 1:
      print("Infinite Levels Toggled")
    elif ic == 1:
      print("Infinite Coins Toggled")
    settingsinput = input("Choose 1, 2, 3, 4 or 5: ")
    while settingsinput not in ("1", "2", "3", "4", "5"):
      print("Invalid Input")
      settingsinput = input("Choose 1, 2, 3, 4 or 5: ")
    #These are for displaying the different "Infinite ______ Toggled" messages
    ih = 0
    ia = 0
    il = 0
    ic = 0
    if settingsinput == "1":
      ih = 1
      if infhealth == False:
        infhealth = True
      else:
        infhealth = False
    elif settingsinput == "2":
      ia = 1
      if infattack == False:
        infattack = True
      else:
        infattack = False
    elif settingsinput == "3":
      il = 1
      if inflvl == False:
        inflvl = True
      else:
        inflvl = False
    elif settingsinput == "4":
      ic = 1
      if infcoins == False:
        infcoins = True
      else:
        infcoins = False


def savegame():
  global health
  global maxhealth
  global attack
  global lvl
  global name
  global coins
  global hpotions
  global dpotions
  global infhealth
  global infattack
  global inflvl
  global infcoins
  os.system('clear')
  print("The name of your save file will be needed to load the game.")
  savename = input("What do you want to name this save file?: ").lower()
  db[savename] = savename
  db[savename+"health"] = health
  db[savename+"maxhealth"] = maxhealth
  db[savename+"attack"] = attack
  db[savename+"lvl"] = lvl
  db[savename+"name"] = name
  db[savename+"coins"] = coins
  db[savename+"hpotions"] = hpotions
  db[savename+"dpotions"] = dpotions
  db[savename+"infhealth"] = infhealth
  db[savename+"infattack"] = infattack
  db[savename+"inflvl"] = inflvl
  db[savename+"infcoins"] = infcoins
  os.system('clear')
  print("Saved game successfully with the name:",savename)
  print("Use this name to load the game next time you play!")
  input("Press Enter to Continue")

def shop():
  #Adds the variables to the function ANOTHER TIME (theres gotta be an easier way to do this)
  global health
  global maxhealth
  global attack
  global lvl
  global name
  global coins
  global hpotions
  global dpotions
  global infhealth
  global infattack
  global inflvl
  global infcoins
  os.system('clear')
  print("""What do you want to buy?
  1. Health Potion (10 coins)
  2. Damage Potion (20 coins)
  3. Max Health Boost (50 coins)
  4. Attack Boost (25 coins)
  5. Exit Shop
Choose a product to see more details about it.""")
  print("You have", coins, "coins.")
  shopchoice = input("Choose 1, 2, 3, 4 or 5: ")
  while shopchoice not in ("1", "2", "3", "4", "5"):
    print("Invalid Input")
    shopchoice = input("Choose 1, 2, 3, 4 or 5: ")

  #All of these shop choices work almost the exact same way I literally copied and pasted them all and tweaked the numbers. Easy to add more items later!

  #Health Potion
  if shopchoice == "1":
    os.system('clear')
    print("""Health Potion (10 coins)
    Heals you by 10 HP. 
    Use this product in your inventory. 
    This is limited by your max health, to increase your max health check the shop!"""
          )
    confirmbuy = input(
      "Do you want to purchase this product? Yes or No: ").lower()
    while confirmbuy not in ("yes", "no"):
      print("Invalid Input")
      confirmbuy = input(
        "Do you want to purchase this product? Yes or No: ").lower()
    if confirmbuy == "yes":
      if coins > 10:
        coins = coins - 10
        hpotions = hpotions + 1
        os.system('clear')
        print("Succesfully purchased! You now have", hpotions,
              "health potions. ")
        input("Press Enter to Continue")
        shop()
      else:
        os.system('clear')
        print("You don't have enough coins to buy this item.")
        input("Press Enter to Continue")
        shop()

  #Damage Potion
  elif shopchoice == "2":
    os.system('clear')
    print("""Damage Potion (20 coins)
    Deals 15 damage to the current enemy you are fighting. 
    Helpful in Boss Battles. """)
    confirmbuy = input(
      "Do you want to purchase this product? Yes or No: ").lower()
    while confirmbuy not in ("yes", "no"):
      print("Invalid Input")
      confirmbuy = input(
        "Do you want to purchase this product? Yes or No: ").lower()
    if confirmbuy == "yes":
      if coins > 20:
        coins = coins - 20
        dpotions = dpotions + 1
        os.system('clear')
        print("Succesfully purchased! You now have", dpotions,
              "damage potions.")
        input("Press Enter to Continue")
        shop()
      else:
        os.system('clear')
        print("You don't have enough coins to buy this item.")
        input("Press Enter to Continue")
        shop()

  #Max Health Boost
  elif shopchoice == "3":
    os.system('clear')
    print("""Max Health Boost (50 coins)
    Increases your max health by 10 HP. 
    You will still need to use a health potion to reach your new max health. """
          )
    confirmbuy = input(
      "Do you want to purchase this product? Yes or No: ").lower()
    while confirmbuy not in ("yes", "no"):
      print("Invalid Input")
      confirmbuy = input(
        "Do you want to purchase this product? Yes or No: ").lower()
    if confirmbuy == "yes":
      if coins > 50:
        coins = coins - 50
        maxhealth = maxhealth + 10
        os.system('clear')
        print("Succesfully purchased! Your max health is now", maxhealth)
        input("Press Enter to Continue")
        shop()
      else:
        os.system('clear')
        print("You don't have enough coins to buy this item.")
        input("Press Enter to Continue")
        shop()

  #Attack Boost
  elif shopchoice == "4":
    os.system('clear')
    print("""Attack Boost (25 coins)
    Increases your attack by 1.""")
    confirmbuy = input(
      "Do you want to purchase this product? Yes or No: ").lower()
    while confirmbuy not in ("yes", "no"):
      print("Invalid Input")
      confirmbuy = input(
        "Do you want to purchase this product? Yes or No: ").lower()
    if confirmbuy == "yes":
      if coins > 25:
        coins = coins - 25
        attack = attack + 1
        os.system('clear')
        print("Succesfully purchased! Your attack is now", attack)
        input("Press Enter to Continue")
        shop()
      else:
        os.system('clear')
        print("You don't have enough coins to buy this item.")
        input("Press Enter to Continue")
        shop()
    else:
      shop()


def inventory():
  #Adds all the variables to the function (please tell me a better way to do this)
  global health
  global maxhealth
  global attack
  global lvl
  global name
  global coins
  global enemyhp
  global hpotions
  global dpotions
  global infhealth
  global infattack
  global inflvl
  global infcoins
  os.system('clear')
  print("Your Inventory: ")
  print("   1. Health Potions:", hpotions)
  print("   2. Damage Potions:", dpotions)
  print("   3. Exit Inventory")
  inventoryuse = input("Choose 1, 2 or 3: ")
  while inventoryuse not in ("1", "2", "3"):
    print("Invalid Input")
    inventoryuse = input("Choose 1, 2 or 3: ")
  os.system('clear')

  #Use Health Potion
  if inventoryuse == "1":
    if health == maxhealth:
      os.system('clear')
      print("Your health is already at the maximum of", health,
            ". You can increase your max health with coins in the shop!")
      input("Press Enter to Continue")
      inventory()
    elif hpotions > 0:
      hpotions = hpotions - 1
      health = health + 10
      if health > maxhealth:
        health = maxhealth
      print("Health Potion Used! Your Health is now", health)
      input("Press Enter to Continue")
      inventory()
    else:
      os.system('clear')
      print("You don't have any health potions. Purchase some in the shop!")
      input("Press Enter to Continue")
      inventory()

  #Use Damage Potion
  elif inventoryuse == "2":
    os.system('clear')
    #Tests if you are in a battle or not to tell whether or not you can use the item right now
    if enemyhp > 0:
      if dpotions > 0:
        enemyhp = enemyhp - 15
        dpotions = dpotions - 1
        os.system('clear')
        if enemyhp > 0:
          print("Damage Potion used! The enemy's health is now", enemyhp)
          input("Press Enter to Continue")
          inventory()
        else:
          return
      else:
        os.system('clear')
        print(
          "You don't have any damage potions. Purchase some in the shop after your battle!"
        )
        input("Press Enter to Continue")
        inventory()
    else:
      print("You can't use this item here.")
      print(
        "Use these items while in a battle to deal 15 damage to the enemy. ")
      input("Press Enter to Continue")
      inventory()


def stats():
  #ADDS ALL THE VARIABLES TO THE FUNCTION AHHHHHHHHH
  global health
  global maxhealth
  global attack
  global lvl
  global name
  global coins
  global infhealth
  global infattack
  global inflvl
  global infcoins
  #Simple stats menu for keeping track in game and also for me for debugging a bit
  os.system('clear')
  print("Health: ", health)
  print("Max Health:", maxhealth)
  print("Attack:", attack)
  print("Level:", lvl)
  print("Name:", name)
  print("Coins:", coins)
  print("Infinite Health:", infhealth)
  print("Infinite Attack:", infattack)
  print("Infinite Level:", inflvl)
  print("Infinite Coins:", infcoins)
  input("Press Enter to Continue")


def encounter():
  #adds all the variables to the function (again again again)
  global health
  global maxhealth
  global attack
  global lvl
  global name
  global coins
  global enemyhp
  global hpotions
  global dpotions
  global infhealth
  global infattack
  global inflvl
  global infcoins
  global gamecompleted
  #Chooses the health of the enemy based on your level
  if lvl == 1:
    enemyhp = random.randint(2, 3)
  else:
    print("Error")
    input("Press Enter to Continue")
  #If the player or enemy dies this will end
  while enemyhp > 0 and health > 0:
    os.system('clear')
    print("Enemy Health:", enemyhp)
    print("Your Health:", health)
    print("""What do you want to do?
  1. Attack
  2. Use an item
  3. Run away""")
    encounterchoice = input("Choose 1, 2 or 3: ")
    while encounterchoice not in ("1", "2", "3"):
      print("Invalid Input")
      encounterchoice = input("Choose 1, 2 or 3: ")
    #Attacks the enemy and also makes the enemy attack the player
    if encounterchoice == "1":
      enemyattack = random.randint(0, 2)
      enemyhp = enemyhp - attack
      health = health - enemyattack
    #Opens your inventory to use an item such as a health potion or damage potion
    elif encounterchoice == "2":
      inventory()
    #Makes you run away from the fight if you're like gonna die lmao
    else:
      os.system('clear')
      enemyhp = 0
      print("""You succesfully ran away from the fight.
              You earned 0 coins.""")
      input("Press Enter to Continue")
      return

  #Checks whether the enemy or the player died in the fight
  #If it was the player the game ends
  if health <= 0:
    gamecompleted = True
    return
  #If it was the enemy you get the coins!!!
  elif enemyhp <= 0:
    os.system('clear')
    encounterreward = random.randint(4, 7)
    #I LOVE GAMBLING LETS ADD A JACKPOT CHANCE
    jackpotchance = random.randint(1, 10)
    print("You defeated the enemy.")
    #One in Ten chance to get the jackpot which will TRIPLE your coins from the fight. big money moves
    if jackpotchance == 1:
      encounterreward = encounterreward * 3
      print(" You hit the JACKPOT and earned", encounterreward,
            "coins. Congratulations!")
    else:
      print(" You earned", encounterreward, "coins.")
    coins = coins + encounterreward
    input("Press Enter to Continue")
  else:
    print("Error")
    input("Press Enter to Continue")


def main():
  #ADDS the VARIABLES to the FUNCTIONAsfaondgsaabo
  global health
  global maxhealth
  global attack
  global lvl
  global name
  global coins
  global hpotions
  global dpotions
  global infhealth
  global infattack
  global inflvl
  global infcoins
  #This is my makeshift constant variable because you come back to this function so often (i should have used constant variables (aaahh i'll do that later))
  if infhealth == True:
    health = 9999
    maxhealth = 9999
  if infattack == True:
    attack = 9999
  if inflvl == True:
    lvl = 9999
  if infcoins == True:
    coins = 9999
  #Literally the main function of the game. Thats why i called it main.
  os.system('clear')
  print("""What do you want to do?
    1. Train Stats
    2. Fight Boss
    3. Enter Shop
    4. Inventory
    5. Check Stats
    6. Save Game
    7. Exit Game""")
  mainchoice = input("Choose 1, 2, 3, 4, 5, 6 or 7: ")
  while mainchoice not in ("1", "2", "3", "4", "5", "6", "7"):
    print("Invalid Input")
    mainchoice = input("Choose 1, 2, 3, 4, 5, 6 or 7: ")
  #Takes you to fight a smaller enemy to earn coins
  if mainchoice == "1":
    encounter()
  #Takes you to fight the boss which will level you up when i can be bothered to make that work
  elif mainchoice == "2":
    fightboss()
  #Takes you to the shop to buy stuff with coins
  elif mainchoice == "3":
    shop()
  #Takes you to your inventory to see your items
  elif mainchoice == "4":
    inventory()
  #Shows all your stats in the game
  elif mainchoice == "5":
    stats()
  #Saves the game (but not yet)
  elif mainchoice == "6":
    savegame()
  #Exits the game (why would you want to)
  else:
    os.system('clear')
    #Confirms if you really want to exit the game or not and warns you about save data
    print(
      "Are you sure you want to exit the game? ALL UNSAVED PROGRESS WILL BE LOST!"
    )
    exitconfirm = input("Yes or No: ").lower()
    while exitconfirm not in ("yes", "no"):
      print("Invalid Input")
      exitconfirm = input("Yes or No: ")
    #Quits the game :(
    if exitconfirm == "yes":
      exit()
    #Takes you back to the game :)
    else:
      main()


def fightboss():
  #aDDS ALL THE vaRIABLEs TO thE fuNCTION
  global health
  global maxhealth
  global attack
  global lvl
  global name
  global coins
  global enemyhp
  global hpotions
  global dpotions
  global infhealth
  global infattack
  global inflvl
  global infcoins
  global gamecompleted
  if lvl == 1:
    enemyhp = 20
    enemyattack = 8
  else:
    print("Error")
    input("Press Enter to Continue")
  #If the player or enemy dies this will end
  while enemyhp > 0 and health > 0:
    os.system('clear')
    print("Enemy Health:", enemyhp)
    print("Your Health:", health)
    print("""What do you want to do?
  1. Attack
  2. Use an item
  3. Run away""")
    bosschoice = input("Choose 1, 2 or 3: ")
    while bosschoice not in ("1", "2", "3"):
      print("Invalid Input")
      bosschoice = input("Choose 1, 2 or 3: ")
    #Attacks the enemy and also makes the enemy attack the player
    if bosschoice == "1":
      enemyhp = enemyhp - attack
      health = health - enemyattack
    #Opens your inventory to use an item such as a health potion or damage potion
    elif bosschoice == "2":
      inventory()
    #Makes you run away from the fight if you SUCK
    else:
      os.system('clear')
      enemyhp = 0
      print("""You succesfully ran away from the fight.
  You earned 0 coins.""")
      input("Press Enter to Continue")
      return

  if enemyhp <= 0 and health > 0:
    #Gives player coins for defeating the boss based on level
    os.system('clear')
    if lvl == 1:
      bossreward = 100
    else:
      print("Error")
      input("Press Enter to Continue")
    print("You defeated the boss!")
    print(" You earned", bossreward, "coins.")
    coins = coins + bossreward
    input("Press Enter to Continue")
  #Tests to see if the player has no health, and if so, ends the game.
  elif health <= 0:
    gamecompleted = True
  else:
    print("Error")
    input("Press Enter to Continue")


#Literally one line that starts the whole game. VERY COOL
mainmenu()

#Tests to see if you are dead
while gamecompleted == False and health > 0:
  main()

#Game Over Screen
if health != 0:
  health = 0
os.system('clear')
print("Game Over!")
print("Your Final Stats:")
print("   Level:", lvl)
print("   Health Potions:", hpotions)
print("   Health: ", health)
print("   Max Health:", maxhealth)
print("   Attack:", attack)
print("   Damage Potions:", dpotions)
print("   Coins:", coins)
print("Thanks for Playing!")

#to do list: (in order from easiest to hardest)
#Make the levels actually work and be useful
#Split functions into separate python files (idk how)