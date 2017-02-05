def openfile(filename):
 fo=open(filename+".txt","r+")
 string=fo.read()
 return string
 
string=openfile("hello")
print(string)
