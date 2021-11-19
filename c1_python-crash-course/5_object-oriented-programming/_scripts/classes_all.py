class Flower:
  color = 'unknown'

rose = Flower()
rose.color = "red"

violet = Flower()
violet.color = "green"

this_pun_is_for_you = "I don't sleep at night cause I'm thinking of you"

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you)



#A class represents and defines a concept, while an object is a specific instance of a class.
class Furniture:
	color = ""
	material = ""

table = Furniture()
table.color = "brown"
table.material = "wood"

couch = Furniture()
couch.color = "red"
couch.material = "leather"

def describe_furniture(piece):
	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

print(describe_furniture(table))
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch))
# Should be "This piece of furniture is made of red leather"



class Dog:
  years = 0
  def dog_years(self):
    return self.years*7

fido=Dog()
fido.years=3
print(fido.dog_years())

class Apple:
    def __init__(self,color,flavor):
        """First initialization method"""
        self.color = color
        self.flavor = flavor

    #without __str__ it will be
    #jonagold <__main__.Apple object at 0x0000024E4DE5AA00>
    #which printed the position of the object in memory.
    def __str__(self):
        """That function returns formatted string"""
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

jonagold = Apple("red","sweet")
print('jonagold.color',jonagold.color)#correct
print('jonagold',jonagold)


class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        """Outputs a message with the name of the person"""
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(self.name)

# Create a new instance with a name of your choice
some_person = Person("Ruslan")
# Call the greeting method
print(some_person.greeting())
#print(help(Person))

class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name}! {sound}".format(name = self.name, sound = self.sound))

class Piglet(Animal):
    sound = "Oink!"
hamlet = Piglet("Hamlet")
hamlet.speak()
class Cow(Animal):
    sound = "Moooo"
milke = Cow("Milky White")
milke.speak()

class Clothing:
    material = ""
    def __init__(self,name):
        self.name = name
    def checkmaterial(self):
        print("This {} is made of {}".format(self.name,self.material))

class Shirt(Clothing):
    material="Cotton"
    #pass

polo = Shirt("Polo")
polo.checkmaterial()
