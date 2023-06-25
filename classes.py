#obejetc.methods()
#isinstance --> to know if Point is the instance of point 
#constructor def __init__ is the name of the function  (its a majic method called a constructor )
#self :- refrence to the current point object
#magic meths have teo underscores infront and back 




from typing import Any


class Point:
    def __str__(self):
        return f"({self.x} , {self.y})"
    def default_colour(self):
        print("red")
    def __init__(self , x , y):
        self.x = x 
        self.y = y
    @classmethod #its a decorator 
    def zero(cls):
        return cls(0,0) #this is same as Point(0,0)
    def draw(self):
         print(f"Point ({self.x} , {self.y})")
    def __eq__(self, other ):
        return self.x == other.x and self.y == other.y
    def __gt__(self , other):
        return self.x>other.x and self.y > other.y
    def __add__(self , other):
        return Point(self.x + other.x , self.y + other.y) #theres coma instead of and 
point = Point(1,2)
point.z = 10 #no need to do it in the function itself
print(type(point))
print(isinstance(point , Point))
print(point.x)
point.draw()
another = Point(3,4) #completly different than the first
another.draw()
another.default_colour()
Point.default_colour ="yellow"
print(another.default_colour)
print(point.default_colour) #changes in both cases 
#if we wannna call a class method , in a different way 
point2 = Point.zero() #just a different way to express like i said 
print(point2)
point2.draw()
print(Point(3,6))
point3 = Point(3 ,3 )
print(str(point3) , point3)
pointer = Point(1,2)
other = Point(1,2)
other2 = Point(10, 10)
print(pointer == other) #gives false , in memory we are addresses in obejcts in memory, now it gives true cause of the __eq__
print(pointer > other2)
print(pointer < other2)
print (pointer + other)
combined = pointer + other 
print(combined.x)
###########################################################################################################################
#custom containers 
class TagCloud: # this clss gives access to the underlying dictionary , which is not a good thing , uncomment line 84
    def __init__(self):
        self.tags = {}
    def add (self , tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower() , 0) + 1 # the zero indicates the default value if the tag is not present 
    def __getitem__(self , tag):
        return self.tags.get(tag.lower() , 0)
    def __setitem__(self , tag , count):
        self.tags[tag.lower()] = count
    def __len__(self):
        return len(self.tags)
    def __iter__(self):
        return iter(self.tags) #this function returns self.tags over a for loop 


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags) #says 3 pythons are added
k = cloud["python"]
print(k)
#print(cloud.tags['PYTHON'])
class TagCloud2: # we can make the class private by replacing tags2 with __tags2 
    def __init__(self):
        self.__tags2 = {}
    def add (self , tag):
        self.tags[tag.lower()] = self.__tags2.get(tag.lower() , 0) + 1 # the zero indicates the default value if the tag is not present 
    def __getitem__(self , tag):
        return self.__tags2.get(tag.lower() , 0)
    def __setitem__(self , tag , count):
        self.tags[tag.lower()] = count
    def __len__(self):
        return len(self.__tags2)
    def __iter__(self):
        return iter(self.__tags2) #this function returns self.tags over a for loop 
cloud2 = TagCloud2()
#print(cloud2.__tags2) # gives an arrtribute error, uncomment to find out  
print(cloud2.__dict__)#look at the console 
print(cloud2._TagCloud2__tags2) #using this you can access them, private things are used to reduce accedental usage
#___________________________________________________________________________________________________________________________________________________________________________
class Product:
    def __init__(self , price):
        self.__price = price 
# the above class wil even take a negatice price , so, 
class Product2:
    def __init__(self , price):
        self.set_price(price)
    def get_price(self):
        return self.__price 
    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value 
# this above class will not take a negatve value for price 
product = Product(-50)
#product2 = Product2(-50) #this gives an error , for simplar code
class Product3:
    def __init__(self , price):
        self.set_price(price)
    def get_price(self):
        return self.__price 
    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value 
    price = property(get_price , set_price) #this is not a method , as you can see when calling it 

product3 = Product3(10)
#product3.price = -10 # will give an error 
product3.price = 10 
print(product3.price) #to minimise the way code looks. when . is used you will still see the previous methods , to eleminate them we will use 