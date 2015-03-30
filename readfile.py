#if = open("test.txt","r")
#print(f.read(1))
#print(f.read())
#f.close()

f = open("test.txt","r") #opens file with name of "test.txt"
myList = []
for line in f:
 myList.append(line)
print(myList)
