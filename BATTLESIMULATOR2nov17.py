#THE CHARACTER BATTLE SIMULATOR .
#REQUIEMNTS:Give both the player_hp and monster_hp a starting value of 50 .
#Create a function roll_damage (min_damage,max_damage) that use python's random module to return to return a random hit module . 
#Use a while loop to alternate turns :
#PLAYER TURN:choose to "Attack" (deals 5-15 damage) or "Heal" (restore 8-12 HP ).
#MONSTER TURN : Automatically attacks the player (deals 6-12 damage).
# The game ends and declares a winner as soon as either hp hits 0.
#step 1 give the player a backpack to hold items and to buy goods before battle .
backpack = []
player_gold = 20#give the user a gold variable of 20 to buy stuff from inventory .
player_hp = 50 #fixed hp for both the player and the monster .
monster_hp = 50
 # shop item and prices .
shop = {
       "big health potion":10,
       "iron punch":15,
       "small health potion":5,
}
# step 2 the shop loop 
print("\n ........welcome to the shop .......")
#step 3 run the while loop to let the player buy anything from the shop.
while True:
       print("current inventory :",backpack)
       print("current gold :",player_gold)
       print("\n items for sale :")
       print(shop)
       print("before the fight begin you can buy the weapons using your gold .")
       #step 3 using input ask for the item the user would like to buy .
       purchase = str(input("ENTER THE NAME OF THE ITEM YOU'D LIKE TO BUY (or enter 'leave' to fight) : ")).strip().lower()
       # step 4 allow the user to leave the inventory for fight whenever the user want just by giving one command .
       if purchase == "leave":
                print("leaving the shop , prepare for battle .")
                break
       elif purchase in shop:# if the user have enough gold. append the item in backpack.
              cost = shop[purchase]
              #check if the player has enough gold .
              if player_gold >= cost:
                      player_gold -= cost
                      backpack.append(purchase)
                      print("you bough a", {purchase})
              else :
                      print("="*15)
                      print("not enough gold ")  
                      print("="*15)      
              player_gold -10
              print(backpack)
       else:  
                  print("item not found in the shop .")
        
#step 5 set up a while loop to keep the program asking for heal or attack until either hp becomes 0 .
while True:
         #step 6import a random value for both the monster and player using python's random function . 
      import random
      monster_attack = random.randint(6,12)
      if monster_attack :#whenever moster makes an attack subtrack that from the player hp.
               player_hp -=random.randint(6,12)# decrease a random value from the player hp as monster attack.
               print("monster made an attack now your hp is :",max(0,player_hp))
      #step7 take input from the user if they want to attack , heal or use something from backpack .         
      player = input("enter 'Attack' or 'Heal' or use any special equipment to win the game . :").strip().lower()  
      valid_turn = True      
      if player == "attack":
               monster_damage = random.randint(5,15)
               monster_hp -= monster_damage
               print("great attack now monster hp is :",max(0,monster_hp))
      elif player == "heal":
                heal_amount = random.randint(6,12)
                player_hp += heal_amount
                print("great save now your hp is ",max(0,player_hp)) 
      elif player == "small health potion":
                if "small health potion" in backpack:
                         player_hp += 10 # if user uses something from backpack remove that from backpack so that the player cannot use it multiple time .
                         print("you have used the small health potion and now you hp is :",max(0,player_hp)) 
                         backpack.remove("small health potion")
                else :
                          print("you dont have the 'small health potion' availavle.")
                          valid_turn = False
      elif player == "iron punch":   
                      if "iron punch" in backpack:
                                 monster_hp -=20
                                 print("you have used 'iron punch ' and now the monster hp is ",max(0,monster_hp))
                                 backpack.remove("iron punch") 
                      else:
                              print("item is not available in backpack")  
                              valid_turn = False                        
      elif player == "big health potion":
                 if "big health potion" in backpack:
                         player_hp += 15
                         print("you've used big health potin hence your hp increased massively \n now your hp is :", max(0,player_hp) ) 
                         backpack.remove("big health potion")
                 else:
                         print("big health potion is not available in your backpack.")
                         valid_turn =  False                                                           
      #step 8 set the conditions at which the program declares whether the player wins or the monster .
      if monster_hp <= 0:
               print("="*50)
               print("The enemy has been defeated !\n player wins ") 
               print("="*50)
               break
      elif player_hp <= 0 :
               print("="*50)
               print("ooo! You have been DEFEATED ! \nEnemy wins ") 
               print("="*50)
               break           
    


             
          
    
     

 

              



