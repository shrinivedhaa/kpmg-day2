f=open("IO/demofile.txt", 'r')
print(f.read())

f=open('IO/demofile.txt','w')
f.write("This is my file\n")
f.write("I am Shrinivedhaa\n")
f.write("I am from Bangalore\n")
print("Contents of file")
f=open("IO/demofile.txt",'r')
print(f.read())

print("W+")
f=open("demofile.txt","w+")
f.write("It is raining in Bangalore\n")
f.seek(0)

print("a+")
f=open("IO/demofile.txt",'a+')
f.write("I am Shrinivedhaa\n")
f.write("I am from Bangalore\n")
f.write("It is raining in Bangalore, it is getting very cold\n")

f=open("demofile.txt","r")
print(f.read(10))