class Player:
    def __init__(self,name,ballon_dor,ucl):
        self.name = name
        self.ballon_dor = ballon_dor
        self.ucl = ucl
        
    def __str__(self):
        return f"Name: {self.name} | Ballon Dor: {self.ballon_dor} | UCL: {self.ucl}"
        
    def __eq__(self, other):
        return self.ballon_dor == other.ballon_dor
    
    def __lt__(self, other):
        return self.ballon_dor < other.ballon_dor
    
    def __gt__(self, other):
        return self.ballon_dor > other.ballon_dor

player1 = Player("messi",8,4)
player2 = Player("ronaldo",5,5)
player3 = Player("zidane",1,1)
player4 = Player("ronaldinho",1,1)

print(player1)
print(player2)
print(player3)
print(player4)

print(f"is Messi == Ronaldo? {player1 == player2}")
print(f"is Messi > Ronaldo? {player1 > player2}")
print(f"is Zidane < Ronaldo? {player3 < player2}")
print(f"is Zidane == Ronaldinho? {player3 == player4}")

