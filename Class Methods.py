class Toys:
    Toy_Manufacturer = "Local Toys"
    Fixed_Price =  500
    def __init__(self,name):
        self.name = name

    @classmethod #Decorater To Present that it's a class method
    def Manufacturer_change(cls,newManfct): #newManfct = new Toy_Manufacturer
        cls.Toy_Manufacturer = newManfct

    @classmethod
    def ChangePrice(cls, newprice):
        cls.Fixed_Price = newprice

Toy1 = Toys("Rubber Duck")
print("Toy 1 is : " + Toy1.name)
print() #blank Line

print("Old Toy Manufacturer is: " + Toys.Toy_Manufacturer) #Before Updating Value
Toys.Manufacturer_change("Github Toys") #method calling and assigning value in argument
print("New Toy Manufacturer is: " + Toys.Toy_Manufacturer) #After Updating Value

print() #blank Line
print("Old Fixed Price of Toys: " + str(Toys.Fixed_Price) + "PKR")
Toys.ChangePrice(800) #class method called with arg
print("New Fixed Price of Toys: " + str(Toys.Fixed_Price) + "PKR")

