class Towel:

    def __init__(self, color:str = ' ', size:str = ' '):
        self.color:str = color
        self.size:str = size
        self.wetness:int = 0

    
    def __str__(self):
        return f"Cor: {self.color}, Tamanho: {self.size}, Umidade: {self.wetness}"
    
    def show(self):
        print(self)

    def isDry(self):

        if self.wetness == 0:
            print("sim")
        else:
            print("nao")

    def getMaxWetness(self):
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        
        

    def dry(self, ammount:int):
        self.wetness += ammount
        if self.wetness >= self.getMaxWetness():
            print("toalha encharcada")
            self.wetness = self.getMaxWetness()

    def wringOut(self):
        self.wetness=0
        
def main():

    towel = Towel(" ", " ")


    while True:
        linha = str(input())
        args: list[str] = linha.split(" ")

        print("$" + linha)

        if args[0] == "end":
            break
        elif args[0] == "criar":
            color:str = args[1]
            size:str = args[2]
            towel = Towel(color, size)
        elif args[0] == "mostrar":
            towel.show()
        elif args[0] == "seca":
            towel.isDry()
        elif args[0] == "enxugar":
            ammount:int = int(args[1])
            towel.dry(ammount)
        elif args[0] == "torcer":
            towel.wringOut()
        
main()
    

    