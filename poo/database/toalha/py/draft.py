class Towel:
    def __init__(self,color: str = "", size:str = ""):
        self.color:str = color
        self.size:str = size
        self.wetness:int = 0

    def __str__(self):
        return f"color:{self.color} size:{self.size} wetness:{self.wetness}"
    
    def show(self):
        print(self)

    def getMaxWetness(self):
        if self.size == "P":
            return 10
        elif self.size == "M":
            return 20
        else:
            return 30

    def dry(self, amount:int):
        self.wetness += amount
        if self.wetness>self.getMaxWetness():
            print("enxarcada")
            self.wetness=self.getMaxWetness()

    def wringOut(self):
        self.wetness=0

    def isDry(self):
        if self.wetness == 0:
            print("True")
        else:
            print("False")
    

def main():
    towel = Towel(" ", " ")

    while True:
        linha = str(input())
        args: list[str] = linha.split(" ")  

        if args[0] == "end":
            break
        elif args[0] == "init":
            color:str = args[1]
            size:str = args[2]
            towel = Towel(color, size)
        elif args[0] == "show":
            print(towel)
        elif args[0] == "dry":
            amount:int = int(args[1])
            towel.dry(amount)
        elif args[0] == "wringOut":
            towel.wringOut()
        elif args[0] == "isDry":
            towel.isDry()

main()