#this program written for explain class method

import csv

class Item:
    all = []


    def __init__(self,name,price,quantity=0):
        self.name=name
        self.price=price
        self.quantity=quantity

        Item.all.append(self)



    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader=csv.DictReader(f)
            items=list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=int(item.get('price')),
                quantity=int(item.get('quantity'))
            )

            #print(item)

    def __repr__(self):
        return f"Item({self.name},{self.price},{self.quantity})"



Item.instantiate_from_csv()

print(Item.all)