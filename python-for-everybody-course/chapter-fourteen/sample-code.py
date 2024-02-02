'''
* class is a reserved word
* Each PartyAnimal object has a bit of code
* Tell the an object to run the party() code within it
* This is the template for making PartyAnimal objects.
* Each PartyAnimal object has bit of data
* Constructor a PartyAnimal object and store in animal
'''

class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x +1
        print('So far', self.x)
    

animal = PartyAnimal()
animal.party()
animal.party()
animal.party()

#A Nerdy Way to Find Capabilities
'''
* The dir() command lists capabilities
* Ignore the ones with underscores - these are used by Python itself
* The rest are real operations that the object can perform
* It is like type() - it tells us something *about* a variable

x = list()
type(x)
dir(x)
'''
class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x +1
        print('So far', self.x)
    

animal = PartyAnimal()
print("Type", type(animal))
print("Dir", dir(animal))

#Object Lifescycle
'''
* Objects are created, used and discarded
* We have special blocks of code (methods) that get called
 * At the moment creation (constructor)
 * At the moment of destruction (destructor)

* Constructor are used a lot
* Desctructor are seldom used
'''

#Constructor
'''
* The primary purpose of the constructor is to set up some instance variables to have the proper initial values when the object is created
* The constructor and destructor are optional. The constructor is typically used to set up variables. The destructor is seldom used.
* In object oriented programming, a constructor in a class is a special block of statements called when an object is created
* We can create lots of objects - the class is the template for the object
* We can store each distinct object in its own variable
* We call this having multiple instances of the same class
* Each instance has its own copy of the instance variables
'''

class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed')
    
    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

    def __del__(self):
        print('I am destructed', self.x)

animal = PartyAnimal()
animal.party()
animal.party()

animal = 42
print('animal contains', animal)

