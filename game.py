
from game_attr import *
import time


###### GAME INITIATION ######

print(' Welcome to the PVP Game!'.center(50, '*'))



def attack_info():
    print("""
╔════════════════════════════════════════╗
              ⚔️ ATTACK INFO
╚════════════════════════════════════════╝

🛡️ WARRIOR

Level 1:
20 damage — 50% chance
30 damage — 50% chance

Level 2:
25 damage — 100% chance

Level 3:
5 damage  — 75% chance
50 damage — 25% chance


🧙 MAGE

Level 1:
20 damage — 50% chance
30 damage — 50% chance

Level 2:
25 damage — 100% chance

Level 3:
5 damage  — 75% chance
50 damage — 25% chance


🏹 ARCHER

Level 1:
20 damage — 50% chance
30 damage — 50% chance

Level 2:
25 damage — 100% chance

Level 3:
5 damage  — 75% chance
50 damage — 25% chance

╚════════════════════════════════════════╝
""")

time.sleep(3)

attack_info()


def game(player1_wincount = 0, player2_wincount = 0):
    print('********************************************************')
    print('\n\n Choose your character class'.upper())

    print(' 1. Warrior\n 2. Mage\n 3. Archer')


    


    p1 = int(input(' Player 1, choose your class (1-3): '))
    p2 = int(input(' Player 2, choose your class (1-3): '))

    print(f' Player 1 chose class {p1}')
    print(f' Player 2 chose class {p2}')


    ###### PLAYER CREATION ######

    while True:
        if p1 == 1:
            player1 = Warrior('player1')
            break

        elif p1 == 2:
            player1 = Mage('player1')
            break

        elif p1 == 3:
            player1 = Archer('player1')
            break


    while True:
        if p2 == 1:
            player2 = Warrior('player2')
            break

        elif p2 == 2:
            player2 = Mage('player2')
            break

        elif p2 == 3:
            player2 = Archer('player2')
            break


###### GAME OPERATES ######


   

    def victory():

        nonlocal player1_wincount, player2_wincount

        if player1.hp <= 0:
            print('\n\n\nCONGRATS!\nPLAYER 2 WINS!!!🏆🏆')
            player2_wincount += 1
            print(f'Player 2 wins: {player2_wincount}\nplayer 1 wins: {player1_wincount}')

        elif player2.hp <= 0:
            print('\n\n\nCONGRATS!\nPLAYER 1 WINS!!!🏆🏆')
            player1_wincount += 1
            print(f'Player 1 wins:  {player1_wincount}\nPlayer 2 wins:{player2_wincount}')


    print(' Let the battle begin!'.center(50, '*'))


    while player1.hp > 0 and player2.hp > 0:

        s_ = random.choice([1, 2])

        if s_ == 1:
            print(f'player 1 \'s hp={player1.hp}:player 2 \'s hp={player2.hp}\n')
            print('🔵🔵Player 1 ATTACKS\n')
            player1.attack(player2)
            if player2.hp>0:

                print('NEXT ROUND'.center(40,'^'))
            
        else:
            print(f'player 1 \'s hp={player1.hp}:player 2 \'s hp={player2.hp}')

            print('🟡🟡Player 2 ATTACKS\n')
            player2.attack(player1)
            if player1.hp>0:
            
                            print('NEXT ROUND'.center(40,'^'))
                        
            

    victory()
            
    user_input=input('\n\ndo you want to have another round\npress y tofor another and q to quit\n').lower()   
    if user_input =='y':
        game()
    elif user_input=="q":
        return 'Thanks for playing😊😊'



    


game()

