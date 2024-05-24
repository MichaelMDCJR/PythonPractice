file1 = open("MyFile1.txt", "w+")

file1.write("Testing")
file1.write("cats")
file1.write("dogs")

file1.close()

file1 = open("MyFile1.txt", "r+")

var = file1.readline()
print(var)

