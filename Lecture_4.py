#DICTIONARIES
"""dict={
    "name":"Anjani",
    "learning":"Python",
    "subjects" :["HTML","CSS","JS"],
    "ytchannel" :"apnacollege",

}
print(type(dict))
print(dict["name"])
dict["surname"] ="Chitlangia"
print(dict)"""

#Nested dictionary 
"""students ={
    "name ":"Anjani",
    "Standard": 12,
    "Subjects": {
        "Maths": 97,
        "Science": 89,
        "English": 98,
    }
}
print(students["Subjects"]["Maths"])
print(students)
print(students["Subjects"])
print(students.keys())
print(students.values())
print(students.items())
print(students.get("name "))
students.update({"city": "Kolkata"})
print(students)"""
#sets
"""collection = { 1,2,2,"HELLO ","HELLO "}
print(collection)
print(len(collection))
print(type(collection))
collection1={} #empty set
collectiond=set() #null set
collection.add("Anjani")
collection.remove(1)
print(collection)
collection.pop()
print(collection)
collection.clear()
print(collection)
collection.union(collectiond)
print(collection)"""
#questions 
#Q1
"""dict={
    "table":["A piece of furniture", "List of facts and figures"],
    "cat":"A small animal"
}
print(dict)"""
#Q2
"""list={"python","java","c++","python","javascript","java","python","java","c++","c"}
print("No. of classrooms required are:", len(list))"""
#Q3
"""marks={}

x=int(input("Enter physics marks: "))
marks.update({"physics": x})
x=int(input("Enter chemistry marks: "))
marks.update({"chemistry": x})
x=int(input("Enter maths marks: "))
marks.update({"maths": x})
print(marks)"""
#Q4
