print('hello')

#crete a function
def greet():
    print('hello')

greet()

#crete a fuction that only display the output not return any value
def add1(a,b):     #a,b are formal argument
    c=a+b
    print(c)

add1(4,5)    #4,4 are actual argument.this is 4 types.
             #position,keyword,default,variable length

#a function that return value, so we can store this value in a variable
def add2(a,b):
    c=a+b
    return c

x=add2(4,5)

print(x)


#a function that return multiple values

def add_sub(a,b):
    c=a+b
    d=a-b
    return c,d

x,y=add_sub(5,4)

print(x,y)


