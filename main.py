#Adventure Time
#Basic adventure game using if/elif/else logic statements to print various results based on player's choice 

import ascii_art
from clearscreen import clear

print(ascii_art.fairy)
print("Welcome to Terra! I'm Estelle, the fairy queen.")
player_name = input("Tell me your name adventurer.\n")

clear() 

print(f"Nice to meet you {player_name}. I met you just in time! I have a mission for you.")
print("The Lycans have started to gather around to take over the capital. I need you to infiltrate their camp, and steal their blueprints for their weapon of mass destruction.\n")
print("You don't have a choice by the way ... good luck! Oh and try not to get bitten!\n")

print("YOU HAVE LEFT THE FAIRY QUEEN COURT -- SAFE TRAVELS!\n")

print(ascii_art.mountains)

print("YOU HAVE ENTERED LYCAN TERRITORY -- BEWARE OF THE LURKING CREATURES\n")

print("A group of Lycans are approaching you. You have 250 HP. On your left, is thick shrubbery that can mask your presence. On your right is a tall tree with low branches that's easy to climb - lycans can't climb trees by the way.\n")

direction = input("Where do you want to go? Type left to go the shrubbery or right to climb the tree\n")

if direction.lower() == "left":
  clear()
  print(ascii_art.cave)
  print("There's a rabbit hole in the shrubbery which you fall into. This brings you into a massive underground cave. You have an open wound on your calves, and you've landed between two underground streams. You now have 200 HP left.\n")
  print("One stream is black and murky with a horrible stench and the other is crystal clear running water.\n")
  
  water_choice = input("Which stream do you go to, to clean your wound? Type murky or crystal\n")
  
  if water_choice.lower() == "murky":
    clear()
    print(ascii_art.tunnel)
    print("The polluted water has infected your wound. You now have 150 HP left.\n")
    print("You see a tunnel in this underground cave and it leads you right into the Lycans hideout. They are on lunch! You spot the blueprints on their work table. But there's three, one red, one purple and one blue.\n")
    
    color_choice = input("Which colored blueprint will you take with you? Type red, purple or blue\n")

    if color_choice.lower() == "red":
      clear()
      print(ascii_art.fumes)
      print("You've released toxic fumes in the room. You are slowly dying of poison. The Lycans are alerted of your presence and watch you die.\n")
      print(ascii_art.skull)
      print(ascii_art.gameover)
    elif color_choice.lower() == "blue":
      clear()
      print(ascii_art.lycan)
      print("Oh no! A lycan has just returned from lunch. He attacks you and gravely wounds you. You now have 50 HP left ... but you get teleported to Estelle, the fairy queen.\n")

      print("YOU HAVE LEFT LYCAN TERRITORY -- PLEASE COME AGAIN!\n")
      
      print(ascii_art.fairy)

      print("YOU ARE IN THE FAIRY QUEEN COURT -- BEWARE GOSSIPING FAIRIES\n")
      
      print(f"Congratulations {player_name}! You have successfully completed this mission ... oh ... but you're injured. Follow me to the medic to get treated!\n")
      print("YOU'VE WON!\nGo get some well deserved rest!")
    elif color_choice.lower() == "purple":
      clear()
      print(ascii_art.wasp)
      print("You have triggered an alarm. A swarm of carnivorous wasps appeared and killed you.\n")
      print(ascii_art.skull)
      print(ascii_art.gameover)
    else:
      clear()
      print("You were teleported to the beginning because of your wrong choice. At least you get to live a safe life now!\n")
      print(ascii_art.skull)
      print(ascii_art.gameover)
  else:
    clear()
    print(ascii_art.octopus)
    print("Great, your wound is now clean. Your blood in the stream attracted a giant octopus that strangled you and ate you alive.\n")
    print(ascii_art.skull)
    print(ascii_art.gameover)
else:
  clear()
  print(ascii_art.spider)
  print("You have successfully climbed the tree ... into a giant spider's nest. It captured you in it's web and slowly ate you.\n")
  print(ascii_art.skull)
  print(ascii_art.gameover)