class Calculadora:

    def __init__(self, batteryMax:int):
        self.batteryMax:int = batteryMax
        self.battery:int = 0
        self.display:int = 0
    
    def __str__(self):
        return(f"display = {self.display:.2f}, battery = {self.battery}")
    
    def show(self):
        print(self)

    def charge(self,increment:int):
        self.battery += increment
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax
        
    def sum(self, a:float, b:float):
        if self.battery > 0:
            sum = a + b
            self.display = sum
            self.battery -=1
        elif self.battery <= 0:
            print("fail: bateria insuficiente")
            self.battery = 0

    def div(self, den:float, num:float):
        if den == 0 or num == 0:
            print("fail: divisao por zero")
            self.battery -= 1
        elif self.battery > 0:
            div = den / num
            self.display = div
            self.battery -= 1
        elif self.battery <= 0:
            print("fail: bateria insuficiente")
            self.battery = 0
        


def main():
    calculadora = Calculadora(" ")

    while True:
        linha = str(input())
        args: list[str] = linha.split(" ")

        print("$" + linha)

        if args[0] == "end":
            break
        elif args[0] == "init":
            batteryMax:int = int(args[1])
            calculadora = Calculadora(batteryMax)
        elif args[0] == "show":
            calculadora.show()
        elif args[0] == "charge":
            increment:int = int(args[1])
            calculadora.charge(increment)
        elif args[0] == "sum":
            a:float = float(args[1])
            b:float = float(args[2])
            calculadora.sum(a,b)
        elif args[0] == "div":
            den:float = float(args[1])
            num:float = float(args[2])
            calculadora.div(den, num)
main()