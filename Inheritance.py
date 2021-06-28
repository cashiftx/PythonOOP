class parent: #Main CLass
    def __init__(self,name,fame):
        self.name=name
        self.fame =fame

Github = parent("Github","99%")
print("Parent name is " + Github.name)

class child(parent): #Main CLass
    def __init__(self,name,fame,car,bike): #merge all parameters parent + child
        super().__init__(name,fame)         #Args of Parent class only
        self.car = car                      #Initialize self object
        self.bike = bike
git = child("Git","90","Many","None")
#calling
print("Child Name: "  + git.name)
print("Child Fame: "  + git.fame)