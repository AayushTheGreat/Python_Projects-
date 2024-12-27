# %%
name=input("Enter Your Name :")
print('\nHello '+name+ ', Welcome to the Adventure Game!')#string concatenation
decide=input("\nDo you want to play? ")
play=decide.lower()=='yes' or decide.upper()=='Y'
def endingR():
    """This ending is executed when the user chose the left path at the starting of the game.
    """
    print('\nYou found a river and saw a very old bridge reaching the other bank.')
    choice=input('How do you want to cross the river(swim/walk)?').lower()
    if choice=='swim':
        print("\nYou were eaten by an alligator. Game over...")
    elif choice=='walk':
        print('\nYou crossed the bridge and saw a few men threatening a helpless looking lady')
        ch=input('Do you want to interfere(yes/no)? ').lower()
        if ch=='yes':
            print('''\nYou saved her from the men but she conned you when you were sleeping.
                    Now you have nothing left in the middle of the night and wolves eat you alive...Game OVER''')
        elif ch=='no':
            print("\nThose men told asked you for help and the con woman was locked away.")
            print('You reached the final destination and found the treasure...Game has ended.')
        else:
                    print('Invalid response...Restart')
    else:
                print('Invalid response...Restart')
if play:
    print('\nAdventure Game starts now...Good Luck!')
    while True:
        weapon=input("Choose your Weapon(Sword/Axe) :").lower()
        armour=input("Choose your armour(Light/Heavy) :").lower()
        try:
            if weapon=='sword' or 'axe':
                pass
            if armour=='light' or 'heavy':
                pass
            break
        except:
            print("\nInvalid Response....Enter Again")

    
    print('\nYou are at the crossroads just outside your village.\nThere are two roads diverging into the forest, left and right.')
    direction=input('Choose your path(left/right) :').lower()
    
    if direction=='left':
        print('\nAfter walking for some time, you met the infamous Witcher, Geralt of Rivia.\nHe gave you a health potion and went through a portal.')
    
    elif direction=='right':
        print('\nYou met a group of traders and they gave you a rage potion.')
        print('''You found an abandoned house on your way into the forest.''')
        choice=input('Do you want to enter the house?(yes/no) ').lower()
        if choice=='yes' and weapon=='sword'and armour=='light':
            print("\nYou got attacked by bandits and they killed you because your sword was useless...Game Over")
        elif choice=='yes' and weapon=='axe' and armour=='heavy':
            print('''\nYou got attacked by bandits but you butchered them all...
            \nYou stayed the night and moved ahead in the morning.''')
            endingR()
        elif choice=='yes' and weapon=='axe' and armour=='light':
            print('Bandits attacked you and your armour was wrecked easily and they killed you...Game Over')
        elif choice=='no':
            print('\nYou are walking and suddenly you saw a dragon')
            choice=input('You have two options(run/fight) :').lower()
            if choice=='run'and armour=='heavy':
                print('\nThe Dragon chased you and burnt you alive because the heavy armour slowed you...GAME OVER')
            if choice=='run' and armour=='light':
                print('\nYour light armour helped you escape the dragon.')
                endingR()
            elif choice=='fight' and weapon=='sword':
                print('\nYou slayed the Dragon and continued your journey')
                endingR()
            elif choice=='fight' and weapon=='axe':
                print("\nsYour axe was useless, the dragon smoked you....GAME OVER")
                
        else:
            print('Invalid response...Restart')
    else:
        print('Invalid response...Restart')



    #print("While taking his last breath your father told you about the hidden treasure he looted when he was a pirate.")
    #print('He hid the treasure and lived as a comman man but now on his deathbed, he wants to see you fulfilled.')
else:
    print('\nAdventure Game has ended...See you again!')



# %%
