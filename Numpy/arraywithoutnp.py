import array as arr 
inum=arr.array("i",[1,2,3,4])
inum.insert(1,6)
for i in inum:
    print(i)
print("\n")
inum.remove(6)
for i in inum:
    print(i)
print("\n",inum.index(4))
print("\n")
inum[2]=7
for i in inum:
    print(i)
b=inum[0:3]
print(b)
print(inum)