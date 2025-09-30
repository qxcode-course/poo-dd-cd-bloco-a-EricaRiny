class Animal:
    def __init__(self, species:str = "", sound: str = ""):
        self.species: str = species
        self.age: int = 0
        self.sound: str = sound
    
    def __str__(self) -> str:
        return f"{self.species}:{self.age}:{self.sound}"
    
    def ageBy(self, increment:int):
        self.age += increment
        if self.age>=4:
            print(f"warning: {self.species} morreu")
            self.age=4

    def show(self) -> None:
        print(self)

    def makeSound(self):
        if self.age == 0:
            print("---")
        elif self.age==4:
            print('RIP')
        else:
            print(self.sound)

def main():
    animal = Animal(" "," ")


    while True:
        linha = str(input())
        args: list[str] = linha.split (' ')

        print("$" + linha)

        if args[0] == 'end':
            break
        elif args[0] == "init":
            species: str= args[1]
            sound: str= args[2]
            animal = Animal(species, sound)

        elif args[0] == "show":
            print(animal)

        elif args[0] == "grow":
            increment:int = int(args[1])
            animal.ageBy(increment)

        elif args[0] == "noise":
            animal.makeSound()

#aqui
main()       