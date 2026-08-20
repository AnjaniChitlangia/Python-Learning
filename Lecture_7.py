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