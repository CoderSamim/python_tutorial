# there are 5 types of arguments in a function in python

#1.positional argument
def person1(name,age):
    print(name+"")
    print(age+0)

person1("samim",21)

#2.keyword arguments
def person2(name,age):
    print(name+"")
    print(age+0)

person1(age=21,name="samim")

#3.default arguments
def person2(name,age=18):
    print(name+"")
    print(age+0)

person2("samim")  #here age=18 is default value

#4.variable length arguments
def add(a,*b):  #we can write only *b
    print(a)
    print(b)  # *b take input in form of tuple

    c=a
    for i in b:
        c=c+i
    print(c)

add(7,5,3,4)


#5.keyworded variable length arguments
def person3(name,*data):
    print(name)
    print(data)

person3('samim',21,'kolkata',7074299693)

#part2 of keyworded variable length arguments
def person4(name,**data):
    print(name)
    #print(data)
    for i,j in data.items():   # here items() is a built-in function
        print(i,j)

person4('samim',age=21,city='kolkata',phone=7074299693)

