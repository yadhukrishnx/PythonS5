while True:
    print("\nFile Handling With Python\n","."*40)
    n=int(input("\n\tPress :\n\t1 : For New File creation\n\t2 : For file Reading\n\t3 : For Appending To existing\n\t0 : For Exiting "))
    print("\n","."*40,"\n")
    if(n==1):
        name=input("Enter Filename: ")
        file1=open(name,"w")
        cont=input("Enter the Contents of File: ")
        file1.write(cont)
        print("File created..")
        print("\n","."*40,"\n")
    elif(n==2):
        name=input("Enter Filename to Read: ")
        file1=open(name,"r")
        print("Contents: ",file1.read())
        print("\n","."*40,"\n")
    elif(n==3):
        name=input("Enter Filename to append content: ")
        file1=open(name,"a")
        cont=input("Enter the Contents to append to  File: ")
        file1.write(cont)
        print("File created..")
        print("\n","."*40,"\n")
    elif(n==0):
        
        print("\nBye")
        exit()
    else:
        print("\n Enter a valid number")
    