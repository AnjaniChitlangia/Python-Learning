#Creating a class 
class Student:
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
    def __init__(self,fullname,marks=0):  #constructor with parameters
        #more than one parameter are parameteried constructor
        self.name=fullname  #VALUE assign hogayi 
        self.marks=marks 
        print("different name will appear this time")

s1=Students("John Doe" , 85)
print(s1.name ,s1.marks)
s2=Students("Karan Wahi" , 90)
print(s2.name ,s2.marks)
