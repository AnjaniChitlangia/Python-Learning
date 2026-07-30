"""str="This is a string , We are creating it in python"
str1='This is also a string'
str2=""This is a multi line string . \n tHIS is a multi line string""
print(str2)"""
#concatenation of strings
"""str1="Hello"
str2="World"   
print(str1+str2)
print(len(str1))"""
#indexing of strings
"""print(str1[3] + str2[4])"""
#slicing of strings
"""str="Hello World"
print(str[0:5])
print (str[3:len(str)])
str1="Apple"
print(str1[-3:-1])"""
#String Functions
"""str="I am studying python from apna college and I am loving it"
print(str.endswith("it"))
print(str.capitalize())
print(str) #Capitalize function bas ek hi baar string ko capital karta hai , it does not change the original string 
print(str.replace("am","was"))
print(str)
print(str.find("o"))
print(str.find("am "))
print(str.count("am"))"""
#Q.WAP to input users first name and print its lenght 
"""name=input("Enter your first name: ")
print("Length of your name is: ",len(name))"""
#Q. WAP to find the occurence of $ in a string 
"""str="Hi , I am$ , and I am increasing heavily . Do u know $ sign one time or Kr$na"
print(str.count("$"))"""
#Conditional Statements
"""age= int(input("Enter your age: "))

if (age>=18):
    print("You are eligible to applu for a driving license")
elif(age<18 and age>=16):
    print("You are eligible to apply for a learner's license")
else:
    print("You are not eligible to apply for a driving license")"""

"""marks=int(input("Enter your marks: "))
if(marks>=90):
    print("You have got A grade")
    elif(marks>=80 and marks<90):
        print("You have got B grade")
    elif(marks>=70 and marks<80):
        print("You have got C grade")
    else:
        print("You have got D grade")"""

#Q.WAP TO CHECK IF A NO. ENTERED BY THE USER IS ODD OR EVEN 
"""number = int(input( "Enter a number:"))
if ( number%2==0):
    print("It is an Even Number")
else :
        print("It is an Odd Number ")"""

#Q.WAP TO FIND THE GREATEST OF THE THREE NO.S ENTERED BY THE USER 

"""a=int(input("Enter the first number"))
b=int(input("Enter the seconf number"))
c=int(input("Enter the third number"))
if (a>b and b>c):
    print (" The greatest number is ", a )
elif (b>a and b>c ):
    print ("The greatest number is " , b)
else:
    print ("The greatest number is " , c)"""

#Q.WAP TO CHECK IF A NO. IS MULTIPLE OF 7 OR NOT 
"""num=int(input("Enter a number: "))
if (num%7==0):
    print("It is a multiple of 7")
else:
    print("It is not a multiple of 7")"""