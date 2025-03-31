class player_weapon: #level 1
    def enfield(self):
        print("pistol")

class p1(player_weapon):#level2
    #  def enfield(self):
    #     print("pistol")  overide by bazuka
    def enfield(self):
        print("bazuka")
 

class p2(player_weapon):#level2
    #  def enfield(self):
    #     print("pistol")
 pass

# Polymorphic behavior


players = [p1(), p2()]
for player in players:
    player.enfield()


