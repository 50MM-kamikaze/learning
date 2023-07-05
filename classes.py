#object.methods()
#isinstance --> to know if Point is the instance of point 
#constructor def __init__ is the name of the function  (its a magic method called a constructor )
#self :- reference to the current point object
#magic meths have teo underscores in front and back 



class Point:
    def __str__(self):
        return f"({self.x} , {self.y})"
    def default_color(self):
        print("red")
    def __init__(self , x , y):
        self.x = x 
        self.y = y
    @classmethod #its a decorator 
    def zero(cls):
        return cls(0,0) #this is same as Point(0,0) #takes a default point (0,0)
    def draw(self):
         print(f"Point ({self.x} , {self.y})")
    def __eq__(self, other ):
        return self.x == other.x and self.y == other.y
    def __gt__(self , other): # we used and here cause , we need those both to be true , but in the addition case , we are returning a pointer 
        return self.x>other.x and self.y > other.y
    def __add__(self , other):
        return Point(self.x + other.x , self.y + other.y) #theres coma instead of and 
point = Point(1,2)
point.z = 10 #no need to do it in the function itself
print(type(point))
print(isinstance(point , Point))
print(point.x)
point.draw()
another = Point(3,4) #completely different than the first
another.draw()
another.default_color()
Point.default_color ="yellow"
print(another.default_color)
print(point.default_color) #changes in both cases 
#if we wanna call a class method , in a different way 
point2 = Point.zero() #just a different way to express like i said  #this is how we call the class normally --> point = Point(1,2)
print("new topic")
print(point2) 
point2.draw()
print(Point(3,6))
point3 = Point(3 ,3 )
print(str(point3) , point3)
pointer = Point(1,2)
other = Point(1,2)
other2 = Point(10, 10)
print(pointer == other) #gives false , in memory we are addresses in objects in memory, now it gives true cause of the __eq__
print(pointer > other2)
print(pointer < other2)
print (pointer + other)
combined = pointer + other 
print(combined.x)
print('new topic 2')
###########################################################################################################################
#custom containers 
class TagCloud: # this class gives access to the underlying dictionary , which is not a good thing , uncomment line 84
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
#print(cloud.tags['PYTHON'])# we will get an error , cause we are accessing the dictionary it self, to make the dictionary private , we use the below method
class TagCloud2: # we can make the class private by replacing tags2 with __tags2 
    def __init__(self):
        self.__tags2 = {}
    def add (self , tag):
        self.__tags2[tag.lower()] = self.__tags2.get(tag.lower() , 0) + 1 # the zero indicates the default value if the tag is not present 
    def __getitem__(self , tag):
        return self.__tags2.get(tag.lower() , 0)
    def __setitem__(self , tag , count):
        self.__tags2[tag.lower()] = count
    def __len__(self):
        return len(self.__tags2)
    def __iter__(self):
        return iter(self.__tags2) #this function returns self.tags over a for loop 
cloud2 = TagCloud2()
cloud2.add("Samhith")
print("Samhith--->" , cloud2["samhith"])
#print(cloud2.__tags2) # gives an attribute error, uncomment to find out  
print(cloud2.__dict__)#look at the console #this holds all the dictionary the class holds 
print(cloud2._TagCloud2__tags2) #using this you can access them, private things are used to reduce accidental usage
#if the members are private , we need to use the above method to know the number of tags present 
#___________________________________________________________________________________________________________________________________________________________________________
class Product:
    def __init__(self , price):
        self.__price = price 
# the above class wil even take a negative price , so, 
class Product2: # this cant take a negative price 
    def __init__(self , price):
        self.set_price(price)
    def get_price(self):
        return self.__price 
    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value 
# this above class will not take a negative value for price 
product = Product(-50)
#product2 = Product2(-50) #this gives an error , for simple code
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

product3 = Product3(30)
print(product3.price)
#product3.price = -10 # will give an error 
product3.price = 10 
print(product3.price) #to shorten the way code looks. when . is used you will still see the previous methods , to eliminate them we will use 
# when we are calling the methods, the set__ and get__ are still accessible , which make code look worse, to fix it , we are gonna use decorators
class Product4:
    def __init__(self , price):
        self.price = price #in this method we can call the price method like we normally do it
    @property
    def price(self):
        return self.__price 
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value 
    
product4 = Product4(10) # uncomment the below line to find the better version of the method menu 
#product4.
#___________________________________________________________________________________________________________________________________________________
