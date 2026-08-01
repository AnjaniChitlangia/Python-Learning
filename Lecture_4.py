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
students ={
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
print(students)