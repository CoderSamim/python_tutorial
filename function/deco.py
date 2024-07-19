
# use and property of decorator

#@smart_div
def div(a,b):
    '''if a<b:
       a,b=b,a'''
    print(a/b)

def smart_div(func):     #pass div() to func as a parameter by line-14 statement....function as parameter
    def inner(a,b):      
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner


div= smart_div(div)  # we can replce it by,  @smart_div
div(2,4)


def decor(func): #decorator
    def inner():    #wrapper function
        func()      #actual function
    return inner

def f1():  #this function called inside wrapper function
    pass

f1= decor(f1)  #pass functiopn inside decorators

f1()  # call the function

