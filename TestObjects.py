class Animals:
    def __init__(self,name,color,age):
        self.name =name
        self.color = color
        self.age = age
    #    self.name = name

Lion = Animals("Leo","Orange",12)
print("Lion's name is " + Lion.name + " and Lion's age is " + str(Lion.age))
