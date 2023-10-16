file1=open("fileop.txt",'a') # opening fileop.txt file using open() in write mode ( creates a new file if it doesnot exist)
file1.write("Opening files in w mode will override everytime when we write into it , opening in a mode will not overrider existing data \n both a & w mode creates file if it doesnot exist")
file1.close()
