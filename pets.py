class Pet:

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.direction = 0
        self.is_alive = True
        self.happiness = 5

    def eat(self):
        if self.is_alive:
            print(self.name + " goes 'Nom Nom Nom...'")
        else:
            print("Dis boi ded.")

    def sleep(self):
        print("zzzzzzzzzzzzzz...")

    def speak(self, output):
        print(self.name + " says " + output + ".")

    def play(self):
        print("Yippee!")

    def sing(self):
        print("Do, re, mi, fa, so, la, ti, do!")
    
    def rotate_right(self):
        self.direction += 1

        if self.direction == 4:
            self.direction = 0

    def rotate_left(self):
        self.direction -= 1

        if self.direction == -1:
            self.direction = 3

    def move(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x -= 1


    def hanging_out (self, other):
        print(self.name + " is hanging out with " + other.name +"!")
        other.happiness += 5

        if other.happiness < 10:
            print(other.name + " this is legitness ")
        else:
            print(other.name + " i wanna go HOME!!!!!")
    
    def hug(self, other):
        print(self.name + " hugs " + other.name +"!")
        other.happiness += 1

        if other.happiness < 10:
            print(other.name + " says, 'I'm like " + str(other.happiness) + " happy now.")
        else:
            print(other.name + " says, 'Um, this is awkward.'")
            
    def kill(self, other):
        print(self.name + " kills " + other.name + "!")
        other.is_alive = False

    def reincarnate (self, other):
        print(self.name + " brings " + other.name + " back to life!")
        other.is_alive = False
        
    def __repr__(self):
        return "Name: " + self.name + \
               " [x=" + str(self.x) + \
               ", y=" + str(self.y) + \
               ", d=" + str(self.direction) + "]"
    
    
pet1 = Pet("Jaden")
pet2 = Pet("Coop Dogg")
pet3 = Pet("Bob Ross")
