class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
     def sound(self):
        print("Dog barks")
class Cat(Animal):
      def sound(self):
        print("Cat meows")

dog = Dog()
cat = Cat()

print("Inheritance:")
dog.sound()

print("\nPolymorphism:")
animals = [Dog(),Cat()]

for animal in animals:
    animal.sound()
