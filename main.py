def life(hero,v):
  if v<0:
    if (hero['life']+v<0): # No negative life points.
      hero['life'] = 0
    else:
      hero['life'] = hero['life']+v
    print(" \U0001FA78 You lose %d life points\t\t[%d/%d]" % (-v,hero['life'],hero['max']))
  else:
    if (hero['life']+v>hero['max']): # Not higher than max.
      hero['life'] = hero['max']
    else:
      hero['life'] = hero['life']+v
    print(" \U00002695 You gain %d life points\t\t[%d/%d]" % (v,hero['life'],hero['max'])) 
  return hero

def gold(hero,v):
  if v<0:
    if (hero['gold']+v<0): # No negative money. This should be tested before calling this function.
      hero['gold'] = 0
    else:
      hero['gold'] = hero['gold']+v
      print(" \U0001FA99 You lose %d gold coins\t\t[%d]" % (-v,hero['gold'])) # Coin emoji
  else:
    hero['gold'] = hero['gold']+v
    print(" \U0001F4B0 You gain %d gold coins\t\t[%d]" % (v,hero['gold'])) # Bag of money emoji
  return hero


def dead(h):
  print("You died, game over!")
  printStats(h)

def printStats(hero):
  print("Your name was %s, you had %d life points and owned %d gold coins." % (hero['name'],hero['life'],hero['gold']))

def entranceRoom(hero):
  print("You are in the entrance hall.")
  print("There is a wooden door to the right and a metal door to the left.")
  userIn=input("[Enter \"Wooden\" or \"Metal\" to choose a door, or \"Exit\" to leave the donjon (and the game)].      ")
   # lowercase of input so case does not matter
  if userIn=="Metal": 
    print("Let's go to the left.")
    guardsRoom(hero)
    return
  elif userIn=="Wooden":
    print("Right it is, then.")
    corridor(hero)
    return
  else:
    print("Invalid input. Wooden or Metal")
    entranceRoom(hero)
  return

def guardsRoom(hero):
  print("You are in the guards room. A goblin appears!")
  print("Do you use your sword or punch him?")
  print("[Enter \"Sword\" to use the sword and \"Punch\" to punch the goblin]")
  i = input().lower() # lowercase of input so case does not matter
  inputOk=False
  if i=="sword":
    inputOk = True
    print("\U0001F5E1 You take your sword out. The goblin jumps at you with claws out and impales himself on your blade.")
    print("You killed the goblin with only some scratches.")
    hero=life(hero,-5)
  elif i=="punch":
    inputOk=True
    print("\U0001F44A The goblin jumps at you with claws out teeth bare. You punch at him until it finally dies, but you are badly hurt.")
    hero = life(hero,-50)
  else: # invalid input
    print("The input was invalid. Let's try again")
    guardsRoom(hero) # re-enter the same room
  if inputOk: 
    if hero['life']<=0: # No more life points
      dead(hero)
    else:
      print("There is a wooden door to the left, a gilded door to the front, and the metal door you came through. Which do you want to enter; Wooden, Gilded, or Metal?")
      userIn = input().lower() 
      if userIn=="Wooden":
        print("You leave by the door to the left...")
        cellar(hero)
      elif userIn=="Gilded":
        print("You leave by the door to the front...")
        ballroom(hero)
      else:
        print("You went back to the entrance!")
        entranceRoom(hero)
    return

def corridor(hero):
  print("Quick! You have encountered an Orc. Use sword and punch")
  sword = input().lower()
  punch = input().lower()
  sword=input("Enter S to use sword")
  if sword=="S":
    chance = 0
    print("The orc yells in pain and charges at you.")
    punch=input("Enter P for punch")
    chance+=1
    if punch=="P":
      print("The orc falls and you can now safely pass.")
      def rooms():
        i = input().lower()
        i = input("Choose either the WOODEN door you came from or the METAL door ahead.")
        if i=="METAL":
          kitchen(hero)
        if i=='WOODEN':
          entranceRoom(hero)
        else:
          print("Choose a room.")
          rooms()
        return
    else:
      print("You missed and the orc manages to throw you down the hall. You lose 15L.")
      hero['life'] = hero['life']-15
      corridor(hero)
      chance+=1
  elif sword!="S":
    "The orc dodges your sword and you are injured. You lose 15L."
    hero['life'] = hero['life']-15
    corridor(hero)
    chance+=1
  elif chance>2:
    "You are too injured and head back to the entrance."
    entranceRoom(hero)
  return      
   
def cellar(hero):
  print("You have entered the cellar.")
  print("An old man is hidden in the cellar. You can play a riddle game for 5G. Will you play the game? Yes or No")
  userIn = input().lower()
  if userIn=="Yes":
    hero['gold'] = hero['gold']-5
    print("What is always in front of you but can’t be seen?")
    if userIn=="the future":
      print("You guessed it. You earned 20G. Good luck on the rest of your quest.")
      hero['gold'] = hero['gold']+20
    else:
      print("Try again")
      cellar(hero)
  elif userIn=="No":
    print("You are now leaving the cellar.")
    guardsRoom(hero)
  else:
    cellar(hero)
  return


def ballroom(hero):
  print("You are in a nice ballroom. There is a gilded door and a door wooden door.")
  print("[Enter \"Gilded\" or \"Wooden\"]")
  i = input().lower()
  if i=="gilded":
    guardsRoom(hero)
  elif i=="wooden":
    kitchen(hero)
  else:
    print("You take a tour of the room.")
    ballroom(hero)
  return

def kitchen(hero):
  print("You are in a kitchen. Food smells good, there is ham, bread,cheese, and beer; which do you choose?")
  print("[Enter \"Ham\", \"Bread\", \"Cheese\", or \"Beer\"]")
  i = input().lower()
  if i=="ham":
    print("\U0001F356 \"Humm, what a delicious ham!\"")
    hero = life(hero,15)
  elif i=="bread":
    print("\U0001F35E \"A crispy loaf of bread!\"")
    hero = life(hero,5)
  elif i=="cheese":
    print("\U0001F9C0 \"What a nice piece of cheese!\"")
    hero = life(hero,10)
  elif i=="beer":
    print("\U0001F37A \"Nice fresh beer... I do feel tipsy, though...\"")
    hero = life(hero,20)
    hero = gold(hero,-5)
    print("You spilled 5G in your drunkness")
  else: # invalid input
    print(" \"Nah, I'm good\"")
    print("After this little snack, you take a look around.")
    print("There are three doors: one wooden, one gilded, and one in metal.")
    print("[Enter \"Wooden\", \"Gilded\" or \"Metal\" to choose a door]")
  i = input().lower()
  if i=="wooden":
    ballroom(hero)
  elif i=="metal":
    corridor(hero)
  elif i=="gilded":
    throne(hero)
  else:
    print("You rummage through the food stores. A pot falls on your head.")
    hero = life(hero,-1)
    if hero['life']<=0:
      gameOver(hero,win=False)
    else:
      print("You wake up.")
      kitchen(hero)
  return

def throne(hero):
  print("You enter the throne room. You see the Crown of Fame glowing on a cushion next to the throne.")
  print("As you walk to grab it, a deep voice resonates through the room.")
  print("\"I have been expecting you, %s. You are not the first adventurer who tries to steal my Crown." % hero['name'])
  print("And you won't be the last. You will be just another pile of bones!\"")
  print("Suddenly, a knight in black armour falls from the ceiling and slashes at you with his flail.")
  hero = life(hero,-10)
  if hero['life']>0:
    turn1(hero)
  else:
    gameOver(hero,win=False)
  return

def turn1(hero):
  print("Do you use your sword or punch him?")
  print("[Enter \"Sword\" to use the sword and \"Punch\" to punch the dark knight]")
  i = input().lower()
  choice = 0
  if i=="sword": # Correct choice here
    choice = 1
    print("\U0001F5E1 You slash at the knight's side. He blocks with his shield and sends a kick from below it.")
  elif i=="punch":
    choice = -1
    print("\U0001F44A You try to punch the knight. He blocks with his shield. The shield is of steel, your hand is of flesh. Guess who wins...")
  else:
    print("You are stunned by the knight's apparition. He takes advantage of that to give you a second dose of flail.")
  hero = life(hero,-15)
  if hero['life']>0:
    turn2(hero,choice)
  else:
    gameOver(hero,win=False)
  return

def turn2(hero,t1):
  print("Do you use your sword or punch him?")
  print("[Enter \"Sword\" to use the sword and \"Punch\" to punch the dark knight]")
  i = input().lower()
  choice = 0
  if i=="sword": # Correct choice here
    choice = 1
    print("\U0001F5E1 You slash at the knight's side. He blocks with his shield and sends a kick from below it.")
  elif i=="punch":
    choice = -1
    print("\U0001F44A You try to punch the knight. He blocks with his shield. The shield is of steel, your hand is of flesh. Guess who wins...")
  else:
    print("You are stunned by the knight's apparition. He takes advantage of that to give you a second dose of flail.")
  hero = life(hero,-15)
  if hero['life']>0:
    turn3(hero,choice)
  else:
    gameOver(hero,win=False)
  return


def turn3(hero,t1,t2):
# Gets the choices for turns 1, and 2: 1 for sword, -1 for punch, 0 otherwise
  print("Do you use your sword or punch him?")
  print("[Enter \"Sword\" to use the sword and \"Punch\" to punch the dark knight]")
  i = input().lower()
  choice = 0
  if i=="sword":
    choice = 1 
    if (t1==1 and t2==-1): #Correct sequence
      print("\U0001F5E1 You slash at the knight's head and your blade gets right between breastplate and helmet. The head rolls to the floor.")
      victory(hero)
    else:
      print("\U0001F5E1 You slash at the knight's head, but the dark knight ducks and shoves his shield in your belly.")
      hero = life(hero,-15)
    if hero['life']>0:
      turn4(hero,t1,t2,choice)
    else:
      gameOver(hero,win=False)
  elif i=="punch":
    choice = -1
    print("\U0001F44A You punch the knight. He spins around but extends his leg in the process to land a roundhouse kick to your chest.")
    hero = life(hero,-15)
    if hero['life']>0:
      turn4(hero,t1,t2,choice)
    else:
      gameOver(hero,win=False)
  else:
    print("You are overwhelmed by the knight's attacks and can't decide. Your defense is wide open for another dose of flail.")
    hero = life(hero,-15)
  if hero['life']>0:
    turn4(hero,t1,t2,choice)
  else:
    gameOver(hero,win=False)
  return
  

def turn4(hero,t1,t2,t3):
  print("Do you use your sword or punch him?")
  print("[Enter \"Sword\" to use the sword and \"Punch\" to punch the dark knight]")
  i = input().lower()
  choice = 0
  if i=="sword": # Correct choice here
    choice = 1
    print("\U0001F5E1 You slash at the knight's side. He blocks with his shield and sends a kick from below it.")
  elif i=="punch":
    choice = -1
    print("\U0001F44A You try to punch the knight. He blocks with his shield. The shield is of steel, your hand is of flesh. Guess who wins...")
  else:
    print("You are stunned by the knight's apparition. He takes advantage of that to give you a second dose of flail.")
  hero = life(hero,-15)
  if choice>1:
    victory(hero)
  else:
    gameOver(hero,win=False)
  return
  
  

def victory(hero):
  print("The dark knight is dead. You catch your breath as you walk slowly to the Crown of Fame.")
  print("You take the Crown in your fingertips and place it on your head.\n \U0001F451 You made it, you are famous!")
  print("There will be song sung in your glory for the centuries ahead. Unless an adventurer manages to steal the Crown from you!")
  gameOver(hero,win=True)
  return

def gameOver(hero,win=False):
  if win:
    print("\t\tCongratulations, you finished the game!")
  else:
    print("\t\tYou died! Game Over!")
    print("\t\U0001F3B6 O %s, mighty adventurer, you had %d life points and owned %d gold coins... \U0001F3B5" % (hero['name'],hero['life'],hero['gold']))
  return

def donjonGame(hero):
  print("\t\t*** Welcome to this RPG ***\n\t(Real Python Game or Role Playing Game)")
  print("Please enter the name of your hero: ")
  name = input().title() # Capitalize every word
  print("Good day, %s!" % name)
  print("You seem ready to go on an adventure. You have your sword and a strong fist.\nI suggest you use these in alternance, it usually works best against ennemies.")
  print("This mysterious donjon is rumoured to harbour the Crown of Fame, which makes his bearer famous.\nIsn't that the goal of any adventurer?")
  print("Let's go!")
  entranceRoom(hero)
  return
donjonGame("hero")
  


