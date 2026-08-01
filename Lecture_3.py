#List IN Python
"""marks=[98.7 , 56.8 , 94.4 , 65.4 , 45.1 , "Anjani" , "Aditya "]
print(marks)
print(len(marks))
print(marks[0])
marks[4]=57.9
print(marks)
print(marks[0:4])
print(marks[-1])
list=[2,4,3,1]
print(list.append(6))
print(list)
print(list.sort())
print(list)
print(list.sort(reverse=True))
print(list)
print(list.reverse())
print(list)
print(list.insert(2,5))
print(list)
list.remove(3)
print(list)
list.pop(2)
print(list)
tuple=(1,2,3,4,5)
print(tuple[2])
tup=(2,3,7,1,9,1,3,5)

print(tup.index(5))
print(tup.count(1))"""
#WAP TO ASK THE USER FOR 3 FAV MOVIES AND STORE THEM IN THE LIST 
"""a= input("Enter your first favourite movie: ")
b= input("Enter your second favourite movie: ")
c= input("Enter your third favourite movie: ")
fav_movies=[a,b,c]
print("Your favourite movies are: ",fav_movies)"""
#WAP TO CHECK IF A LIST CONTAINS A PARTICULAR ELEMENT OR NOT
"""list=[1,2,2,1]
listrev=list.copy()
listrev.reverse()
if (list==listrev):
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")"""
#WAP TO COUNT NUMBER OF STUDENTS WITH GRADE A 
tup=("C","D","B","A","A","B","A")
print( "No. of students with grade A: ", tup.count("A"))
#STORE THE ABOVE VALUES IN A LIST AND SORT THEM 
list=list(tup)
list.sort()
print("The sorted list is: ",list)
