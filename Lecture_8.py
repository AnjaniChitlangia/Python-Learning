#Creating a class 
"""class Student:
    name = "John Doe"    # constructor will always be called even if not initialied 
    def __init__(self):  #here now constructor is created 
        #has only one parameter i.e self constructor 
        print("adding new students in the database")
        print(self)  #shows student object 

#creating an object of the class
s1=Student() #class ka name 
print(s1.name)
s2=Student()
print(s2.name) #will show same name . we will learn further how to change it 

class Car:
    colour = "Red"
    brand = "Toyota"
car1=Car()
print(car1.colour)
print(car1.brand)

#Constructor
#used in object creation 
class Students:
    name="karan" #class  attribute 
    #object is placed at higher priority than class attribute
    def __init__(self,fullname,marks=0):  #constructor with parameters
        #more than one parameter are parameteried constructor
        self.name=fullname  #VALUE assign hogayi 
        self.marks=marks 
        print("different name will appear this time")
    def welcome(self):
        print("Welcome to the class " + self.name)
        print("Your marks are " + str(self.marks))
s1=Students("John Doe" , 85)
print(s1.name ,s1.marks)
print(s1.welcome())
s2=Students("Karan Wahi" , 90)
print(s2.name ,s2.marks)

#methods
class Stude:
    def __init__(self,fullname):
        self.name=fullname
    #creating a method
    def welcome(self):
        print("Welcome to the class " + self.name)
        #creating an object 
        s1=Stude("John Doe")
        s1.welcome()
        #using method inside the class"""

    #LETS PRACTICE
class Student:
    def __init__(self,fullname,marks=0):
            self.name=fullname
            self.marks=marks

    def avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi " + self.name + " your average marks are " + str(sum/len(self.marks)))
s1=Student("John Doe",[85,90,95])
s1.avg()
s1.name="Karan Wahi"
s1.marks=[80,85,90]
s1.avg()