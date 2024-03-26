class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def can_run (self):
        print("the dog is running")
    def can_bark(self):
        print("woof woof woof woof")
tiger=dog("tiger",2)
print(tiger.can_bark())
print(tiger.can_run())

print(tiger.age)
print(tiger.name)