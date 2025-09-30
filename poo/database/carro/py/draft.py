class Carro:

    def __init__(self):
        self.pas: int = 0
        self.km: int = 0
        self.passMax: int = 2
        self.gas: int = 0
        self.gasMax: int = 100

    def __str__(self):
        return f"pass: {self.pas}, gas: {self.gas}, km: {self.km}"
    
    def show(self):
        print(self)

    def enter(self):
        self.pas += 1
        if self.pas > self.passMax:
            print("fail: limite de pessoas atingido")
            self.pas = self.passMax

    def leave(self):
        self.pas -=1
        if self.pas < 0:
            print("fail: nao ha ninguem no carro")
            self.pas = 0

    def fuel(self, increment:int):
        self.gas += increment
        if self.gas>self.gasMax:
            self.gas = self.gasMax

    def drive(self, distance:int):
        if self.pas == 0:
            print("fail: nao ha ninguem no carro")
        elif self.gas == 0:
            print("fail: tanque vazio")
        elif self.gas < distance:
            distance = self.gas
            self.km += distance
            print(f"fail: tanque vazio apos andar {distance} km")
            self.gas = 0


        else:
            self.gas -= distance
            self.km += distance

def main():
    carro = Carro()

    while True:
        linha = str(input())
        args: list[str] = linha.split(" ")

        print("$" + linha)

        if args[0] == "end":
            break
        elif args[0] == "show":
            carro.show()
        elif args[0] == "enter":
            carro.enter()
        elif args[0] == "leave":
            carro.leave()
        elif args[0] == "fuel":
            increment:int = int(args[1])
            carro.fuel(increment)
        elif args[0] == "drive":
            distance:int = int(args[1])
            carro.drive(distance)
main()