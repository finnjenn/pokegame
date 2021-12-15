import time
#Functions holding pokemon move mechanics
def shadowball(mon):
        if mon.typing == 'Normal':
          print("Shadow Ball has no effect on Normal Types")
        elif mon.typing == 'Water' or mon.typing == 'Dark':
          mon.hp -= 30
def psychic(mon):
        if mon.typing == 'Dark':
          print("Psychic has no effect on Houndoom")
        elif mon.typing == 'Water' or mon.typing == 'Normal':
          mon.hp -= 30
def nasty_plot(mon):
  pass
def power_gem(mon):
        if mon.typing == 'Normal':
          mon.hp -= 30
        elif mon.typing == 'Water' or mon.typing == 'Dark':
          mon.hp -= 50
def crunch(mon):
        if mon.typing == 'Normal':
          mon.hp -= 30
        elif mon.typing == 'Ghost':
          mon.hp -= 50
        elif mon.typing == 'Dark':
          mon.hp -= 10
def aqua_tail(mon):
        if mon.typing == 'Dark':
          mon.hp -= 50
        elif mon.typing == 'Normal' or mon.typing == 'Ghost':
          mon.hp -= 30   
def ice_fang(mon):
        if mon.typing == 'Normal' or mon.typing == 'Ghost':
          mon.hp -= 30
        elif mon.typing == 'Dark':
          mon.hp -= 10
def dragon_dance(mon):
  pass
def flamethrower(mon):
        if mon.typing == 'Normal' or mon.typing == 'Ghost':
          mon.hp -= 30
        elif mon.typing == 'Water':
          mon.hp -= 10
def dark_pulse(mon):
        if mon.typing == 'Ghost':
          mon.hp -= 50 
        elif mon.typing == 'Normal' or mon.typing == 'Water':
          mon.hp -= 30   
def sludge_bomb(mon):
  mon.hp -= 30
def close_combat(mon):
        if mon.typing == 'Water':
          mon.hp -= 10
        elif mon.typing == 'Dark':
          mon.hp -= 50
        elif mon.typing == 'Ghost':
          print('Close Combat does not affect Ghost types')
def earthquake(mon):
        if mon.typing == 'Water' or mon.typing == 'Ghost':
          print('Earthquake does not affect Gyarados or Mismagius')
        elif mon.typing == 'Dark':
          mon.hp -= 50
def rock_slide(mon):
        if mon.typing == 'Water' or mon.typing == 'Dark':
          mon.hp -= 50
        elif mon.typing == 'Ghost':
          mon.hp -= 30
def swords_dance(mon):
  pass
# End of all possible moves                           
      
          
class Poke:
  def __init__(self,name,typing,level,hp):  #hp,attack,defense,desc
    self.name = name
    self.typing = typing
    self.level = level
    self.hp = hp

    if self.name == "Mismagius": #assigns moves to player selected pokemon
      self.movelist = [shadowball,psychic,nasty_plot,power_gem]
      self.movenames = ['Shadow Ball','Psychic','Nasty Plot','Power Gem']

    if self.name == "Gyarados":
      self.movelist = [crunch,aqua_tail,dragon_dance,ice_fang]
      self.movenames = ['Crunch','Aqua Tail','Dragon Dance','Ice Fang']

    if self.name == "Houndoom":
      self.movelist = [flamethrower,dark_pulse,sludge_bomb,nasty_plot]
      self.movenames = ['Flamethrower','Dark Pulse','Sludge Bomb','Nasty Plot']

    if self.name == "Ursaring":
      self.movelist = [close_combat,earthquake,swords_dance,rock_slide]
      self.movenames = ['Close Combat','Earthquake','Swords Dance','Rock Slide']

  def showMon(self):
    print('Pokemon: ',self.name,'\t Lvl:  ',self.level,'\nType: ',self.typing)

### End Poke Class

print('Pokemon: Mismagius\tLvl: 50\nType: Ghost\n')
print('Pokemon: Gyarados\tLvl: 50\nType: Water\n')
print('Pokemon: Houndoom\tLvl: 50\nType: Dark\n')
print('Pokemon: Ursaring\tLvl: 50\nType: Normal\n')
  
while True:  #Player 1's turn to pick mon
  choice1 = int(input('Player 1! Choose your Partner!\n'))
  if choice1 == 1:
    p1poke = Poke('Mismagius','Ghost',50,100)#instantiates Poke object based on choice 
    print("You picked",p1poke.name,'\n')
    break
  elif choice1 == 2:
    p1poke = Poke('Gyarados','Water',50,120)
    print("You picked",p1poke.name,'\n')
    break
  elif choice1 == 3:
    p1poke = Poke('Houndoom','Dark',50,100)
    print("You picked",p1poke.name,'\n')
    break
  elif choice1 == 4:
    p1poke = Poke('Ursaring','Normal',50,110)
    print("You picked",p1poke.name,'\n')
    break

  
while True:# Player 2's turn to pick mon 
  choice2 = int(input('Player 2! Choose your Partner!\n'))
  if choice2 == choice1:
    print('That Pokemon has already been selected.\nTry again.')## Re enter choice if mon has already been selected 
    continue
  if choice2 == 1:
    p2poke = Poke('Mismagius','Ghost',50,100)
    print("You picked",p2poke.name,'\n')
    break
  elif choice2 == 2:
    p2poke = Poke('Gyarados','Water',50,120)
    print("You picked",p2poke.name,'\n')
    break
  elif choice2 == 3:
    p2poke = Poke('Houndoom','Dark',50,100)
    print("You picked",p2poke.name,'\n')
    break
  elif choice2 == 4:
    p2poke = Poke('Ursaring','Normal',50,110)
    print("You picked",p2poke.name,'\n')
    break
    # End Player 2 pick 

def battle(mon1,mon2): #battle function
  battle_go = True

  while battle_go: # battle loop start
    print("Player 1. Go!")
    #Player 1 turn
    while True:
      count = 1
      for x in mon1.movenames:
        print(str(count) + '.',x)
        count+=1
      #print('1.',mon1.move1,'\n2.',mon1.move2,'\n3.', mon1.move3,'\n4.', mon1.move4,'\t\t',mon2.name,':',mon2.hp) #outputs moves for player to see 
      choice = int(input('Choose your move!\n'))
      if choice == 1: mon1.movelist[0](mon2)
      elif choice == 2: mon1.movelist[1](mon2)
      elif choice == 3: mon1.movelist[2](mon2)
      elif choice == 4: mon1.movelist[3](mon2)
      else:continue
      break
    #Check to see if battle is over 
    if mon2.hp <= 0: 
      print('Player 1 has won the battle!',mon2.name,'fainted.')
      break
    #Player 2 turn
    while True:
      count = 1
      for x in mon2.movenames:
        print(str(count) + '.',x)
        count+=1
      #print('1.',mon2.move1,'\n2.',mon2.move2,'\n3.', mon2.move3,'\n4.', mon2.move4,'\t\t',mon1.name,':',mon1.hp) #outputs moves for player to see 
      choice = int(input('Choose your move!\n'))
      if choice == 1: mon2.movelist[0](mon1)
      elif choice == 2: mon2.movelist[1](mon1)
      elif choice == 3: mon2.movelist[2](mon1)
      elif choice == 4: mon2.movelist[3](mon1)
      else:continue
      break
    if mon1.hp <= 0: 
      print('Player 2 has won the battle!',mon1.name,'fainted.')
      break
battle(p1poke,p2poke) #battle function call 