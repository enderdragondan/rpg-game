#Libraries
from getkey import getkey, keys
import os
import random
from replit import db

#Variables
health = 20 #Player Health
maxhealth = 20 #Player Max Health
attack = 1 #Player Attack
lvl = 1 #Player Level
name = "" #Player Name
coins = 0 #Player Coins
infhealth = False #Infinite Health
infattack = False #Infinite Attack
inflvl = False #Infinite Levels
infcoins = False #Infinite Coins
hpotions = 0 #Health Potions
dpotions = 0 #Damage Potions
infhpotions = False #Infinite Health Potions
infdpotions = False #Infinite Health Potions
gamecompleted = False #Player is Dead or not
achievements = [] #Lists all the achievements have
bosseskilled = 0 #Keeps track of how many bosses you have killed (for achievements)
encounterskilled = 0 #Keeps track of how many encounters you have killed (for achievements)
cheats = False

def mainmenu():
  #Adds all the variables to the function
  global health
  global cheats
  global maxhealth
  global attack
  global lvl
  global achievements
  global name
  global coins
  global hpotions
  global dpotions
  global infhealth
  global infattack
  global inflvl
  global infcoins
  global infhpotions
  global infdpotions
  #Very start of the game. nice
  print("\033[1;34;34m")
  os.system('clear')
  print("""Welcome to Enemy Attack!
  1. New Game
  2. Load Game
  3. Settings
Press 1, 2 or 3.""")
  mainmenuchoosing = True
  while mainmenuchoosing == True:
    key = getkey()
    if key == "1":
      newgame()
      mainmenuchoosing = False
    elif key == "2":
      loadgame()
      mainmenuchoosing = False
    elif key == "3":
      settings()
      mainmenuchoosing = False

def newgame():
  #Adds all the variables to the function
  global health
  global cheats
  global maxhealth
  global attack
  global lvl
  global achievements
  global name
  global coins
  global hpotions
  global dpotions
  global infhealth
  global infattack
  global inflvl
  global infcoins
  global infhpotions
  global infdpotions
  #Asks for your name for saying it at random times
  os.system('clear')
  name = input("What is your name?: ")
  if infhealth == True or infattack == True or inflvl == True or infcoins == True or infhpotions == True or infdpotions == True:
    cheats = True

def loadgame():
  #Adds all the variables to the function
  global health
  global cheats
  global maxhealth
  global attack
  global lvl
  global achievements
  global name
  global coins
  global hpotions
  global dpotions
  global infhealth
  global infattack
  global inflvl
  global infcoins
  global infhpotions
  global infdpotions
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
    infcoins = db[savename+"infcoins"]
    infhpotions = db[savename+"infhpotions"]
    infdpotions = db[savename+"infdpotions"]
    achievements = db[savename+"achievements"]
    cheats = db[savename+"cheats"]
    print("Game successfully loaded with the name: ",savename)
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
  ihp = 0
  idp = 0
  while settingsinput != "7":
    #Adds all the variables to the function
    global infhealth
    global infattack
    global inflvl
    global infcoins
    global infhpotions
    global infdpotions
    os.system('clear')
    print("Settings:")
    print("  1. Infinite Health:", infhealth)
    print("  2. Infinite Attack:", infattack)
    print("  3. Infinite Levels:", inflvl)
    print("  4. Infinite Coins:", infcoins)
    print("  5. Infinite Health Potions:",infhpotions)
    print("  6. Infinite Damage Potions:",infdpotions)
    print("  7. Back to Main Menu")
    if ih == 1:
      if infhealth == True:
        print("Infinite Health Enabled")
      else:
        print("Infinite Health Disabled")
    elif ia == 1:
      if infattack == True:
        print("Infinite Attack Enabled")
      else:
        print("Infinite Attack Disabled")
    elif il == 1:
      if inflvl == True:
        print("Infinite Levels Enabled")
      else:
        print("Infinite Levels Disabled")
    elif ic == 1:
      if infcoins == True:
        print("Infinite Coins Enabled")
      else:
        print("Infinite Coins Disabled")
    elif ihp == 1:
      if infhpotions == True:
        print("Infinite Health Potions Enabled")
      else:
        print("Infinite Health Potions Disabled")
    elif idp == 1:
      if infdpotions == True:
        print("Infinite Damage Potions Enabled")
      else:
        print("Infinite Damage Potions Disabled")
    print("Press 1, 2, 3, 4, 5, 6 or 7. ")
    settingschoosing = True
    while settingschoosing == True:
      #These are for displaying the different "Infinite ______ Toggled" messages
      ih = 0
      ia = 0
      il = 0
      ic = 0
      ihp = 0
      idp = 0
      key = getkey()
      if key == "1":
        ih = 1
        settingschoosing = False
        if infhealth == False:
          infhealth = True
        else:
          infhealth = False
      elif key == "2":
        ia = 1
        settingschoosing = False
        if infattack == False:
          infattack = True
        else:
          infattack = False
      elif key == "3":
        il = 1
        settingschoosing = False
        if inflvl == False:
          inflvl = True
        else:
          inflvl = False
      elif key == "4":
        ic = 1
        settingschoosing = False
        if infcoins == False:
          infcoins = True
        else:
          infcoins = False
      elif key == "5":
        ihp = 1
        settingschoosing = False
        if infhpotions == False:
          infhpotions = True
        else:
          infhpotions = False
      elif key == "6":
        idp = 1
        settingschoosing = False
        if infdpotions == False:
          infdpotions = True
        else:
          infdpotions = False
      elif key == "7":
        mainmenu()

def savegame():
  #Adds all the variables to the function
  global health
  global cheats
  global maxhealth
  global attack
  global lvl
  global achievements
  global name
  global coins
  global hpotions
  global dpotions
  global infhealth
  global infattack
  global inflvl
  global infcoins
  global infhpotions
  global infdpotions
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
  db[savename+"infhpotions"] = infhpotions
  db[savename+"infdpotions"] = infdpotions
  db[savename+"achievements"] = achievements
  db[savename+"cheats"] = cheats
  os.system('clear')
  print("Saved game successfully with the name:",savename)
  print("Use this name to load the game next time you play!")
  input("Press Enter to Continue")

def shop():
  #Adds all the variables to the function
  global health
  global cheats
  global maxhealth
  global attack
  global lvl
  global achievements
  global name
  global coins
  global hpotions
  global dpotions
  global infhealth
  global infattack
  global inflvl
  global infcoins
  global infhpotions
  global infdpotions
  os.system('clear')
  print("""What do you want to buy?
  1. Health Potion (15 coins)
  2. Damage Potion (30 coins)
  3. Max Health Boost (50 coins)
  4. Attack Boost (25 coins)
  5. Exit Shop
Choose a product to see more details about it.""")
  print("You have", coins, "coins.")
  print("Press 1, 2, 3, 4 or 5: ")
  shopchoosing = True
  while shopchoosing == True:
    key = getkey()
    #All of these shop choices work almost the exact same way I literally copied and pasted them all and tweaked the numbers. Easy to add more items later!
    #Health Potion
    if key == "1":
      shopchoosing = False
      os.system('clear')
      print("""Health Potion (15 coins)
  Heals you by 10 HP. 
  Use this product in your inventory. 
  This is limited by your max health, to increase your max health check the shop!""")
      print("Do you want to purchase this product? Press Y or N. ")
      healthpotionchoosing = True
      while healthpotionchoosing == True:
        key = getkey()
        if key == "y":
          healthpotionchoosing = False
          if coins > 15:
            coins = coins - 15
            hpotions = hpotions + 1
            os.system('clear')
            print("Succesfully purchased! You now have", hpotions,"health potions. ")
            input("Press Enter to Continue")
            shop()
          else:
            os.system('clear')
            print("You don't have enough coins to buy this item.")
            input("Press Enter to Continue")
            shop()
        elif key == "n":
          healthpotionchoosing = False
          shop()
  
    #Damage Potion
    elif key == "2":
      shopchoosing = False
      os.system('clear')
      print("""Damage Potion (30 coins)
  Deals 15 damage to the current enemy you are fighting. 
  Helpful in Boss Battles. """)
      print("Do you want to purchase this product? Press Y or N. ")
      #lets the user choose an option
      damagepotionchoosing = True
      while damagepotionchoosing == True:
        key = getkey()
        if key == "y":
          damagepotionchoosing = False
          if coins > 30:
            coins = coins - 30
            dpotions = dpotions + 1
            os.system('clear')
            print("Succesfully purchased! You now have", dpotions,"damage potions.")
            input("Press Enter to Continue")
            shop()
          else:
            os.system('clear')
            print("You don't have enough coins to buy this item.")
            input("Press Enter to Continue")
            shop()
        elif key == "n":
          damagepotionchoosing = False
          shop()
  
    #Max Health Boost
    elif key == "3":
      shopchoosing = False
      os.system('clear')
      print("""Max Health Boost (50 coins)
  Increases your max health by 10 HP. 
  You will still need to use a health potion to reach your new max health. """)
      print("Do you want to purchase this product? Press Y or N. ")
      #lets the user choose an option
      maxhealthboostchoosing = True
      while maxhealthboostchoosing == True:
        key = getkey()
        if key == "y":
          maxhealthboostchoosing = False
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
        elif key == "n":
          maxhealthboostchoosing = False
          shop()
  
    #Attack Boost
    elif key == "4":
      shopchoosing = False
      os.system('clear')
      print("""Attack Boost (25 coins)
  Increases your attack by 1.""")
      print("Do you want to purchase this product? Press Y or N. ")
      #lets the user choose an option
      attackboostchoosing = True
      while attackboostchoosing == True:
        key = getkey()
        if key == "y":
          attackboostchoosing = False
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
        elif key == "n":
          attackboostchoosing = False
          shop()
    elif key == "5":
      shopchoosing = False
      main()


def inventory():
  #Adds all the variables to the function
  global health
  global cheats
  global maxhealth
  global attack
  global lvl
  global achievements
  global name
  global coins
  global enemyhp
  global hpotions
  global dpotions
  global infhealth
  global infattack
  global inflvl
  global infcoins
  global infhpotions
  global infdpotions
  os.system('clear')
  print(name+"'s Inventory: ")
  print("  1. Health Potions:", hpotions)
  print("  2. Damage Potions:", dpotions)
  print("  3. Exit Inventory")
  print("Press 1, 2 or 3: ")
  inventorychoosing = True
  if inventorychoosing == True:
    key = getkey()
    #Use Health Potion
    if key == "1":
      inventorychoosing = False
      if health == maxhealth:
        os.system('clear')
        print("Your health is already at the maximum of", health,". You can increase your max health with coins in the shop!")
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
    elif key == "2":
      inventorychoosing = False
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
          print("You don't have any damage potions. Purchase some in the shop after your battle!")
          input("Press Enter to Continue")
          inventory()
      else:
        print("You can't use this item here.")
        print("Use these items while in a battle to deal 15 damage to the enemy. ")
        input("Press Enter to Continue")
        inventory()

    elif key == "3":
      inventorychoosing = False
      return


def stats():
  #Adds all the variables to the function
  global health
  global cheats
  global maxhealth
  global attack
  global lvl
  global name
  global coins
  global bosseskilled
  global encounterskilled
  #Simple stats menu for keeping track in game and also for me for debugging a bit
  os.system('clear')
  print(name+"'s Stats")
  print("  Level:", lvl)
  print("  Health: ", health)
  print("  Max Health:", maxhealth)
  print("  Attack:", attack)
  print("  Coins:", coins)
  print("  Bosses Killed:",bosseskilled)
  print("  Trained Stats:",encounterskilled)
  input("Press Enter to Continue")


def encounter():
  #Adds all the variables to the function
  global health
  global cheats
  global maxhealth
  global attack
  global lvl
  global achievements
  global name
  global coins
  global enemyhp
  global hpotions
  global dpotions
  global infhealth
  global infattack
  global inflvl
  global infcoins
  global infhpotions
  global infdpotions
  global gamecompleted
  global encounterskilled
  #Chooses the health of the enemy based on your level
  enemyhp = random.randint(2,3) * lvl
  #If the player or enemy dies this will end
  while enemyhp > 0 and health > 0:
    os.system('clear')
    print("Enemy Health:", enemyhp)
    print("Your Health:", health)
    print("""What do you want to do?
  1. Attack
  2. Use an item
  3. Run away""")
    print("Press 1, 2 or 3: ")
    encounterchoosing = True
    while encounterchoosing == True:
      key = getkey()
      #Attacks the enemy and also makes the enemy attack the player
      if key == "1":
        encounterchoosing = False
        enemyattack = random.randint(0,2) * lvl
        enemyhp = enemyhp - attack
        health = health - enemyattack
      #Opens your inventory to use an item such as a health potion or damage potion
      elif key == "2":
        encounterchoosing = False
        inventory()
      #Makes you run away from the fight if you're like gonna die lmao
      elif key == "3":
        encounterchoosing = False
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
    encounterreward = random.randint(4, 7) * lvl
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
    encounterskilled = encounterskilled + 1
    input("Press Enter to Continue")

    if encounterskilled == 10 and "killencounter10" not in achievements:
      os.system('clear')
      print("Achievement Unlocked!")
      print("  Train Stats 10 times.")
      print("View your achievements in the achievements menu.")
      achievements.append("killencounter10")
      input("Press Enter to Continue")
  else:
    print("Error")
    input("Press Enter to Continue")

def achievementslist():
  global health
  global cheats
  global maxhealth
  global attack
  global lvl
  global achievements
  global name
  global coins
  global hpotions
  global dpotions
  global infhealth
  global infattack
  global inflvl
  global infcoins
  global infhpotions
  global infdpotions
  global bosseskilled
  global encounterskilled
  os.system('clear')
  if cheats == True:
    print("Achievements aren't available on a save file with cheats enabled.")
    input("Press Enter to Continue")
    return
  print("Achievements: ")
  
  if "killboss1" in achievements:
    print("  Defeat 1 Boss - 100% Completed")
  else:
    print("  Defeat 1 Boss - 0% Completed")

  if "killboss10" in achievements:
    print("  Defeat 10 Bosses - 100% Completed")
  else:
    killboss10 = round((bosseskilled / 10) * 100)
    print("  Defeat 10 Bosses - "+str(killboss10)+"% Completed")
  
  if "level2" in achievements:
    print("  Reach Level 2 - 100% Completed")
  else:
    print("  Reach Level 2 - 50% Completed")

  if "level10" in achievements:
    print("  Reach Level 10 - 100% Completed")
  else:
    level10 = round((lvl / 10) * 100)
    print("  Reach Level 10 - "+str(level10)+"% Completed")
    
  if "killencounter10" in achievements:
    print("  Train Stats 10 times - 100% Completed")
  else:
    killencounter10 = round((encounterskilled / 10) * 100)
    print("  Train Stats 10 times - "+str(killencounter10)+"% Completed")

  if "killencouter50" in achievements:
    print("  Train Stats 50 times - 100% Completed")
  else: 
    killencounter50 = round((encounterskilled / 50) * 100)
    print("  Train Stats 50 times - "+str(killencounter50)+"% Completed")
  
  input("Press Enter to Continue")

  
def main():
  #Adds all the variables to the function
  global health
  global cheats
  global maxhealth
  global attack
  global lvl
  global achievements
  global name
  global coins
  global hpotions
  global dpotions
  global infhealth
  global infattack
  global inflvl
  global infcoins
  global infhpotions
  global infdpotions
  global gamecompleted
  #Depending on what you chose in the settings these will change their respective values. 
  if infhealth == True:
    health = 9999
    maxhealth = 9999
  if infattack == True:
    attack = 9999
  if inflvl == True:
    lvl = 98
  if infcoins == True:
    coins = 9999
  if infhpotions == True:
    hpotions = 9999
  if infdpotions == True:
    dpotions = 9999
  #Literally the main function of the game. Thats why i called it main.
  os.system('clear')
  print("""What do you want to do?
  1. Train Stats
  2. Fight Boss
  3. Enter Shop
  4. Inventory
  5. Check Stats
  6. Achievements
  7. Save Game
  8. Exit Game""")
  print("Press 1, 2, 3, 4, 5, 6, 7 or 8: ")
  mainchoosing = True
  while mainchoosing == True:
    key = getkey()
    #Takes you to fight a smaller enemy to earn coins
    if key == "1":
      mainchoosing = False
      encounter()
    #Takes you to fight the boss which will level you up when i can be bothered to make that work
    elif key == "2":
      mainchoosing = False
      fightboss()
    #Takes you to the shop to buy stuff with coins
    elif key == "3":
      mainchoosing = False
      shop()
    #Takes you to your inventory to see your items
    elif key == "4":
      mainchoosing = False
      inventory()
    #Shows all your stats in the game
    elif key == "5":
      mainchoosing = False
      stats()
    elif key == "6":
      mainchoosing = False
      achievementslist()
    #Saves the game
    elif key == "7":
      mainchoosing = False
      savegame()
    elif key == "8":
      mainchoosing = False
      os.system('clear')
      #Confirms if you really want to exit the game or not and warns you about save data
      print("Are you sure you want to exit the game? ALL UNSAVED PROGRESS WILL BE LOST!")
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
  #Adds all the variables to the function
  global health
  global cheats
  global maxhealth
  global attack
  global lvl
  global achievements
  global name
  global coins
  global enemyhp
  global hpotions
  global dpotions
  global infhealth
  global infattack
  global inflvl
  global infcoins
  global infhpotions
  global infdpotions
  global gamecompleted
  global bosseskilled
  enemyhp = lvl * 20
  enemyattack = lvl * 8
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
    bossreward = 50 * lvl
    print("You defeated the boss!")
    print(" You earned", bossreward, "coins.")
    coins = coins + bossreward
    bosseskilled = bosseskilled + 1
    input("Press Enter to Continue")
    os.system('clear')
    print("Do you want to level up? Leveling up makes enemys stronger, but give you more rewards!")
    levelupchoice = input("Yes or No?: ").lower()
    while levelupchoice not in ("yes","no"):
      print("Invalid Input")
      levelupchoice = input("Yes or No?: ").lower()
    if levelupchoice == "yes":
      lvl = lvl + 1
      os.system('clear')
      print("You are now Level "+str(lvl)+"! Congratulations "+name+"!")
      input("Press Enter to Continue")
      #Give you a little prize for getting to level 100 without cheats...
      if lvl == 100 and cheats == False:
        gamecompleted = True
    else:
      os.system('clear')
      print("Fight the boss again when you're ready to level up!")
      input("Press Enter to Continue")
      
    if bosseskilled == 1 and "killboss1" not in achievements and cheats == False:
      os.system('clear')
      print("Achievement Unlocked!")
      print("  Kill the first boss.")
      print("View your achievements in the achievements menu.")
      achievements.append("killboss1")
      input("Press Enter to Continue")
      
    if lvl == 2 and "level2" not in achievements and cheats == False:
      os.system('clear')
      print("Achievement Unlocked!")
      print("  Reach Level 2.")
      print("View your achievements in the achievements menu.")
      achievements.append("level2")
      input("Press Enter to Continue")

    if bosseskilled == 10 and "killboss10" not in achievements and cheats == False:
      os.system('clear')
      print("Achievement Unlocked!")
      print("  Defeat 10 Bosses.")
      print("View your achievements in the achievements menu.")
      achievements.append("killboss10")
      input("Press Enter to Continue")

    if lvl == 10 and "level10" not in achievements and cheats == False:
      os.system('clear')
      print("Achievement Unlocked!")
      print("  Reach Level 10.")
      print("View your achievements in the achievements menu.")
      achievements.append("level10")
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
while gamecompleted == False:
  main()

#Game Over Screen
if health <= 0:
  if health != 0:
    health = 0
  os.system('clear')
  print("Game Over!")
  print("Your Final Stats:")
  print("  Level:", lvl)
  print("  Health: ", health)
  print("  Max Health:", maxhealth)
  print("  Attack:", attack)
  print("  Coins:", coins)
  print("  Health Potions:", hpotions)
  print("  Damage Potions:", dpotions)
  print("Thanks for Playing "+name+"!")
elif lvl == 100:
  os.system('clear')
  print("congratulations on making it to level 100.")
  print("go to this url for your prize: ")
  print()
  print(os.environ['secret'])

#to do list:
#Split functions into separate python files (idk how)

#if something and "achievement" not in achievements:
#  os.system('clear')
#  print("Achievement Unlocked!")
#  print("  Achievement.")
#  print("View your achievements in the achievements menu.")
#  achievements.append("achievement")
#  input("Press Enter to Continue")