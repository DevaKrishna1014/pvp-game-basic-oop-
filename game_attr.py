import random

class Game:
    def __init__(self,name):
        self.name=name
        self.hp=00
        
    def health_cutter(self,a):
        self.hp-=a
       

class Warrior(Game):


    def attack(self,victim):
        att_level=int(input('ATTACK ARSENAL:\n\n 1.Thrust🤺\n\n2.Swing⚔️\n\n3.absolute👊\n\n\n'))
        attack3=random.choice([5,45,5,5,45])
        attack2=25
        attack1=random.choice([30,20,20,30,20])
        if att_level==1: 
            victim.health_cutter(attack1)
            
            if victim.hp>0:
                print(f"\n\n{victim.name}'s hp ={victim.hp +attack1}➡️  {victim.hp}\n\n\t")
                
            else:
                print(f'\n\n\n\n{victim.name} Dies Ahhhhhh Shammeeeeekk  ❤️❤️❤️❤️❤️')
                
        elif att_level==2: 
            victim.health_cutter(attack2)
            
            if victim.hp>0:
                print(f"\n\n{victim.name}'s hp ={victim.hp +attack2}➡️  {victim.hp}\n\n\t")
                
            else:
                print(f'\n\n\n\n{victim.name}  Ahhhhhh Shammeeeeekk  ❤️❤️❤️❤️❤️')
                
        elif att_level==3: 
            victim.health_cutter(attack3)
            
            if victim.hp>0:
                print(f"\n\n{victim.name}'s hp ={victim.hp +attack3}➡️  {victim.hp}\n\n\t")
                
            else:
                print(f'\n\n\n\n{victim.name}  Ahhhhhh Shammeeeeekk  ❤️❤️❤️❤️❤️')
                

        
        else:
            print('PLEASE ENTER VALID ATTACK NO.\nDUE TO YOUR MISTAKE YOU MISSED YOUR CHANCE\n')

class Mage(Game):


             def attack(self,victim):
                    att_level=int(input('ATTACK ARSENAL:\n 1.earthquake🌎\n\n2.cascade🐳\n\n3.volcano🌋\n\n\n'))
                    attack3=random.choice([5,45,5,5,45])
                    attack2=25
                    attack1=random.choice([30,20,20,30,20])
                    if att_level==1: 
                        victim.health_cutter(attack1)
                        
                        if victim.hp>0:
                            print(f"\n\n{victim.name}'s hp ={victim.hp +attack1}➡️  {victim.hp}\n\n\t")
                            
                        else:
                            print(f'\n\n\n\n{victim.name}  Ahhhhhh Shammeeeeekk  ❤️❤️❤️❤️❤️')
                            
                    elif att_level==2: 
                        victim.health_cutter(attack2)
                        
                        if victim.hp>0:
                            print(f"\n\n{victim.name}'s hp ={victim.hp +attack2}➡️  {victim.hp}\n\n\t")
                            
                        else:
                            print(f'\n\n\n\n{victim.name}  Ahhhhhh Shammeeeeekk  ❤️❤️❤️❤️❤️')
                            
                    elif att_level==3: 
                        victim.health_cutter(attack3)
                        
                        if victim.hp>0:
                            print(f"\n\n{victim.name}'s hp ={victim.hp +attack3}➡️  {victim.hp}\n\n\t")
                            
                        else:
                            print(f'\n\n\n\n{victim.name}  Ahhhhhh Shammeeeeekk  ❤️❤️❤️❤️❤️')


    
                    else:
                        print('PLEASE ENTER VALID ATTACK NO.\nDUE TO YOUR MISTAKE YOU MISSED YOUR CHANCE\n')
            


class Archer(Game):
             def attack(self,victim):
                    att_level=int(input('ATTACK ARSENAL:\n wind gale🍃\n2.dragon short🐉\n\n3.sky piercer🩵\n\n\n'))
                    attack3=random.choice([5,45,5,5,45])
                    attack2=25
                    attack1=random.choice([30,20,20,30,20])
                    if att_level==1: 
                        victim.health_cutter(attack1)
                        
                        if victim.hp>0:
                            print(f"\n\n{victim.name}'s hp ={victim.hp +attack1}➡️  {victim.hp}\n\n\t")
                            
                        else:
                            print(f'\n\n\n\n{victim.name}  Ahhhhhh Shammeeeeekk  ❤️❤️❤️❤️❤️')
                            
                    elif att_level==2: 
                        victim.health_cutter(attack2)
                        
                        if victim.hp>0:
                            print(f"\n\n{victim.name}'s hp ={victim.hp +attack2}➡️  {victim.hp}\n\n\t")
                            
                        else:
                            print(f'\n\n\n\n{victim.name}  Ahhhhhh Shammeeeeekk  ❤️❤️❤️❤️❤️')
                            
                    elif att_level==3: 
                        victim.health_cutter(attack3)
                        
                        if victim.hp>0:
                            print(f"\n\n{victim.name}'s hp ={victim.hp +attack3}➡️  {victim.hp}\n\n\t")
                            
                        else:
                            print(f'\n\n\n\n{victim.name}  Ahhhhhh Shammeeeeekk  ❤️❤️❤️❤️❤️')


    
                    else:
                        
                        print('PLEASE ENTER VALID ATTACK NO.\nDUE TO YOUR MISTAKE YOU MISSED YOUR CHANCE\n')


