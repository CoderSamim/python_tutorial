

# create a class
class Item:
    pay_rate=0.08  #this is a class attribute,
    # class attribute is like a global attibute in other language but it is only for class

    def __init__(self,name,price,quantity=0):
        self.name=name
        self.price=price
        self.quantity=quantity

    def apply_discount(self):
        return self.price * self.pay_rate
    

# directly extract variable of a class without create an object (bcz its a global variable)
print(Item.pay_rate)


# create object item1 and use it
item1=Item('phone',8000,3)
print(item1.pay_rate)
print(item1.apply_discount())


# create object item2 and use it
item2=Item('phone',8000,3)
item2.pay_rate=0.02   #declare a local variable and replce global variable by it
print(item2.pay_rate)
print(item2.apply_discount())


#how to check how many attributes present in a class or in a instance?
print(Item.__dict__)
print(item1.__dict__)
print(item2.__dict__)

