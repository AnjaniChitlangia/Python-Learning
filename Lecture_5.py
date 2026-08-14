#WHILE LOOP 
"""while True:
    print("Hello World")"""
 #it will repeat for infinite times because true will always be  true 
"""count =1
while count<=5:
    print("Hello World")
    count+=1

print(count) """
#it will print 6 because it will increment the value of count after printing hello world 5 times

#print numbers from 1 to 10
"""i=1
while i<=10:
    print(i)
    i+=1"""

#print multiplication of n 
"""i=1
n = int(input("Enter a number: "))
while i<=10:
    print(n*i)
    i+=1 """


#print square of 1 to 10
"""i=1
while i<=10:
    print(i*i)
    i+=1"""

#searching for a number in a tuple

"""i=0 #initialisation
tuple = (1,4,9,16,25,36,49,64,81,100)
n = int(input("Enter a number to search: "))
while i<len(tuple):
    if tuple[i]==n:
        print("Number found at index:", i)
        break
    i+=1"""

#FOR LOOP 
"""list = [1,2,3,4,5,6,7,8,9,10]
for el in list:
    print(el)
vegetables = ["potato", "tomato", "onion", "cabbage"]
for veg in vegetables:
    print(veg)
tuple = (1,2,3,4,5,6,7,8,9,10)
for el in tuple:
    print(el)
str ="Apnacollege"
for char in str:
    print(char)
else:
    print("Loop is over")"""

#QUESTIONS
#Q1
"""nums =[1,4,9,16,25,36,49,64,81,100]
for num in nums:
    if (num==36):
        print("Number found")
        break
    print(num)"""

#RANGE FUNCTION
"""for el in range (1,5,2):
    print (el)
for i in range(101):
    print(i)
for i in range(100,0,-1):
    print(i)
n = int(input("Enter a number: "))
for i in range(1,11):
    print(n*i)"""


#QUESTION BY WHILE LOOP
"""n = int(input("Enter a number: "))
i=1
sum=0
while i<=n:
    sum = sum + i
    i+=1
print("Sum of first", n, "numbers is:", sum)"""

#QUESTION BY FOR LOOP
n = int(input("Enter a number: "))
fac=1
for i in range (1, n+1):
    fac = fac * i
print("Factorial of", n, "is:", fac)
    
