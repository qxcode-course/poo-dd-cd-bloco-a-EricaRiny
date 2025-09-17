class Towel:
    def __init__(self, color: str, size: str):
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0
    
    def __str__(self):
        return f"color:{self.color} size:{self.size} wetness:{self.wetness}"
    
    def dry(self, amount: int):
        self.wetness += amount
        if self.wetness>self.getMaxWetness():
            print("Tá moiado demais, vá estender essa toalha")
            self.wetness = self.getMaxWetness()

    def wringout(self):
        self.wetness = 0
    
    def getMaxWetness(self):
        if self.size == "P":
            return 10
        elif self.size == "M":
            return 20
        else:
            return 30
    
    def isDry(self):
        if self.wetness == 0:
            return True
        else:
            return False
        
    def show(self):
        print(self)

        

towel = Towel("red", "P")
print(towel.color)
print(towel.size)
print(towel.wetness)

print(towel)
towel.dry(10)
print(towel.wetness)
towel.wringout()
towel.show()
towel.dry(12)
towel.show()
print(towel.isDry())
