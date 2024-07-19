
# oreder------main.py--->cons.py--->clast.py---->inherite.py----->more.py


print("hello")

# declare variable and print it (hard code)
item_name = 'phone'
price = 8000
print(type(item_name))
print(type(price))


# string conversion and printing
random_str = str('ram')
print(random_str)
name = 'samim'
print(name)


# create a class (item)
class item:
    values=0
    def calculate_total_price(self):
        pass


# create a instance(object) of item (item1)
item1 = item()


# create variable of item1 object (hard code)
item1.name = 'oppo'
item1.price = 8000

item1.calculate_total_price()
