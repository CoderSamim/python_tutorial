class Item:

    all=[]    #create empty list named all

    def __init__(self,name,price,quantity=0):
        self.name=name
        self.price=price
        self.quantity=quantity

        #to store all instances in a list
        Item.all.append(self)

    def __repr__(self):          #it's a magic method
        return f"Item({self.name},{self.price},{self.quantity})"



item1=Item('iphone',8000,3)
item2=Item('redmi',7000,2)
item3=Item('realme',3000,10)
item4=Item('oppo',5000,3)
item5=Item('vivo',2000,1)


print(Item.all)

#for instance in Item.all:
    #print(instance.name)


