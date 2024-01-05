class Animal():
    a_name = ""
    def __init__(self,name):
        self.a_name = name
    def speak(self):
        print("I am an animal")
    def yell(self):
        print("AHH!!!")
class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
    def speak(self):
        print("Meow")

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    def yell(self):
        print("I'm a dog, I don't yell, I b")


a = Cat("Cat")
b = Dog("dog")
b.speak()
a.speak()
a.yell()
b.yell()