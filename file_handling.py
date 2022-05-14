import os,sys
fname=input("Enter the file name: ")
if os.path.isfile(fname):
    print("file exists", fname)
    f=open(fname,"r")
else:
    print("File doesnt exist",fname)
    sys.exit(0)
print("Content of the file is :")
data=f.read()
print(data)