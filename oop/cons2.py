

# here we overcome hard code variable craeting ob object by constructor
class Item:
    def __init__(self,name,price,quantity=0):
        self.name=name
        self.price=price
        self.quantity=quantity


    #def calculate_total_price(self,x,y):
        #return x*y


    def calculate_total_price(self):
        return self.price*self.quantity



# create object with constructor
item1=Item('phone',8000,3)
item2=Item('laptop',45000)




#print and use of method of object -------->(item1.calculate_total_price(item1.price,item1.quantity))

print(item1.calculate_total_price())


