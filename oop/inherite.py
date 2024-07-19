
from cons2 import Item   #cons2 is file name (module) and Item is class name (present in cons module)

'''class Item:
    def __init__(self,name,price,quantity=0):
        self.name=name
        self.price=price
        self.quantity=quantity'''


# inherite Item class in Phone class
class phone(Item):
    def __init__(self,name,price,quantity=0,broken_phone=0):
        super().__init__(
            name,price,quantity
        )
        self.broken_phone=broken_phone


phone1=phone('redmi',500)

print(phone1.name)
print(phone1.broken_phone)



