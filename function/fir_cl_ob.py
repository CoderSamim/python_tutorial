#function is a first class object(value)

#properties of a first class object

#1  #assign a function to a variable
def plus_one(number):
    return number + 1

a= plus_one  #this variable(a) become a function, because we asssign a function to it
a(5)



#2   #function inside a function
def plus_one(number):
    def add_one(number):
        return number + 1

    result = add_one(number)
    return result

plus_one(4)



#3   #Passing Functions as Arguments to other Functions
def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

function_call(plus_one)



#4  #Functions Returning other Functions
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
hello = hello_function()
hello()


#5  #Closure: A nested function can access the outer scope of the enclosing function
def print_message(message):
    "Enclosong Function"
    def message_sender():
        "Nested Function"
        print(message)

    message_sender()

print_message("Some random message")



