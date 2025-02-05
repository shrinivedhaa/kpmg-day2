class Bird():
    def intro(self):
        print("We are all birds")

    def flight(self):
        print("Most of the birds do fly")

class parrot(Bird):
    def flight(self):
        print("Parrots do fly")

class penguin(Bird):
    def flight(self):
        print("penguins don't fly")

bird=Bird()
parr=parrot()
peng=penguin()

bird.flight()
parr.flight()
peng.flight()

bird.intro()
parr.intro()
peng.intro()