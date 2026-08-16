def calc_sum(a,b):
    s=a+b
    return s
print(calc_sum(5,6))
print(calc_sum(10,20))
def print_hello():
    print("Hello")
print_hello()

#average 
def calc_avg(a,b,c):
    avg=(a+b+c)/3
    return avg
print(calc_avg(10,20,30))

print("Anjani Chitlangia" , end="")
print("I am learning Python from Apnacollege" , end="\n")
print("Thank you shraddha kapra mam")
#output will be 
#Anjani Chitlangia I am learning Python from Apnacollege 
#Thank you shraddha kapra mam
#QUESTIONS 
def print_lenght(string):
    print(len(string))

print_lenght("Anjani Chitlangia")

cities=["Delhi","Mumbai","Bangalore","Chennai"]
def print_cities(cities):
    for city in cities:
        print(city , end=" ")
print_cities(cities)
print(end="\n")


def calc_factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print(calc_factorial(5))

def converter(usd_value):
    inr_value=usd_value*95
    return inr_value
usd_value= int(input("Enter USD value: "))
print("USD VALUE =" , usd_value , "INR VALUE =" , converter(usd_value))

#RECURSION
def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)

print(show(5))

def fact(n):
    if (n==0 or n==1):
        return 1 
    return n*fact(n-1)
print(fact(5))