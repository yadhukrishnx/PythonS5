file1=open("fileop.txt","r") # opening file in read mode (r)
#1 method for printing data
for x in file1:
    print(x)
#2 
print("\n2:\n")
print(file1.read())
#3
print("\n3:\n")
x=file1.read()
print(x)