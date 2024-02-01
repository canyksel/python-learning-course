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