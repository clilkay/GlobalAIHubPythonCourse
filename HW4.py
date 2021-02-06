class Animal:
    def __init__(self,name,colour,leg):
        self.name=name
        self.colour=colour
        self.leg=leg
    def Show(self):
        print("Name :"+self.name+" "+"Colour :"+self.colour+" "+"Leg :"+str(self.leg))
class Dog(Animal):
    def __init__(self, name, colour, leg, sound):
        super().__init__(name, colour, leg)
       
        self.sound=sound

    def Sound1(self):
        print(  "It's sound is :"+self.sound)

class Cat(Animal):
    def __init__(self, name, colour, leg, sound2):
      super().__init__(name, colour, leg)
      self.sound2=sound2
    
      
    def Sound2(self):
        print("It's sound is :"+self.sound2)

cat1=Cat("Boncuk","Black",4,"miyav")
cat1.Show()
cat1.Sound2()

dog=Dog("Pera","White",4,"Havhav")
dog.Show()
dog.Sound1()
