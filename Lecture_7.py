f = open("demo.txt", "r")
#for printing 5 letters from the file
"""data = f.read(5)
print(data)
print(type(data))"""
#for readding a line
data = f.readline()
data1 = f.readline()
print(data)
print(data1)
f.close()
f = open("demo.txt", "w")
f.write("This is a demo file for writing data into it.\n")
#it replaced the previous data in the file
f.close()
#for appending data into the file
f = open("sample.txt", "a")
f.write("This is a demo file for appending data into it.\n")
f.close()
f = open("demo.txt", "r+")
f.write("Using r+ mode\n")
print(f.read())
f.close() 
#the r+ mode is used for both reading and writing into the file. It does not replace the previous data in the file but it overwrites the data from the beginning of the file.
with open("demo.txt","w") as f:
    data=f.write("Hello")
    print(data) #returning no. of letters

import os 
os.remove("sample.txt")

#QUESTIONS 
f=open("practice.txt","w")
f.write("Hi everyone\n We are learning File I/O \n using Java \n I like programming Java ")
f.close()
f=open("practice.txt", "r")
data = f.read()
new_data=data.replace("Java", "Python")
print(new_data)
f.close()
f=open("practice.txt", "r")
data=f.read()
if(data.find("learning")!=-1):
    print("Found")
else:
    print("Not found ")

f.close()
def check_for_line():
    word="learning"
    data=True
    line_no = 1 
    with open("practice.txt","r")as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1
    return-1

check_for_line()






    