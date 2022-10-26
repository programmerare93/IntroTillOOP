import random as rand

class Entity:
    def __init__(self, lifes):
        self.lifes = lifes
        self.scores = 0
        self.did_hit = False
        #self.is_hitted = False

    def fire(self):
        self.did_hit = rand.randrange(1, 6) in {3, 4, 5}
        if self.did_hit:
            self.scores += 1

    def reduce_lifes(self):
        self.lifes -= 1
    
    def reset_status(self):
        self.did_hit = False


def play_game(player_obj, enemy_obj):
    # Speel-loopen
    while True:
        input("Skjut (enter)")
        
        player_obj.fire()
        if player_obj.did_hit:
            enemy_obj.reduce_lifes()
            print(f"\nDu träffa och fienden har nu {enemy_obj.lifes} liv kvar\n")
        else:
            print("\nDu missa\n")
        
        if enemy_obj.lifes <= 0:
            print("Du vann!\n")
            break
        
        enemy_obj.fire()
        if enemy_obj.did_hit:
            player_obj.reduce_lifes()
            print(f"Fienden träffa och du har nu {player_obj.lifes} liv kvar\n")
        else:
            print("Fienden missa\n")
        
        if player_obj.lifes <= 0:
            print("Du förlorade\n")
            break

        player_obj.reset_status()
        enemy_obj.reset_status()
        

player = Entity(3)
enemy = Entity(2)

play_game(player, enemy)
