#Inheritance
'''
* When we make a new class - we can reuse an existing class and inherit all the capabilities of an existing class and then add our own litle bit to make our new class
* Another form of store and reuse
* Write once - reuse many times
* The new class (child) has all the capabilities of the old class (parent) - and some more
'''

class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, nam):
        self.name = nam
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

class FootballFan(PartyAnimal) :
    points = 0
    
    def touchdown(self) :
        self.points = self.points + 7
        self.party()
        print(self.name, 'points', self.points)

s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()

'''
* FootballFan is a class which extends PartyAnimal. It has all the capabilities of PartyAnimal and more.
'''

#Definitions
'''
* Class - a template
* Attribute - A variable within a class
* Method - A function within a class
* Object - A particular instance of a class
* Constructor - Code that runs when an object is created
* Inheritance - The ability to extend a class to make a new class
'''