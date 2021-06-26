class Food:
    def __init__(self,taste,temp,rating,price):
        self.taste = taste
        self.temp = temp
        self.rating = rating
        self.price = price
        self.taste = taste
#classify raing in numerics out of 5
Pasta = Food("Spicy","Hot",5,100)
Fries = Food("Salty","Warm",4,200)
Shake = Food("Sweet","Chill",3,70)

#print(Pasta) # To print address of object pasta (Where it occupied memory)
#taste of foods
print(" ")
print("************** Food Tastes **************")
print(" ")

print("Taste of Pasta is " + Pasta.taste)
print("Taste of Shake is " + Shake.taste)
print("Taste of Fries is " + Fries.taste)

#Temp of foods
print(" ")
print("************** Food Temperatures **************")
print(" ")

print("Temperature of Pasta is " + Pasta.temp)
print("Temperature of Shake is " + Shake.temp)
print("Temperature of Fries is " + Fries.temp)

#Rating of foods
print(" ")
print("************** Food Ratings **************")
print(" ")
#CAN'T CONCATENATE STR WITH INT SO TYPECASTED RATING,PRICE USING STR METHOD
print("Rating of Pasta is " + str(Pasta.rating) + "/5")
print("Rating of Shake is " + str(Shake.rating) + "/5")
print("Rating of Fries is " + str(Fries.rating) + "/5")

#Price of foods
print(" ")
print("************** Food Price List **************")
print(" ")

print("Price of Pasta is " + str(Pasta.price) + " PKR")
print("Price of Shake is " + str(Shake.price) + " PKR")
print("Price of Fries is " + str(Fries.price) + " PKR")