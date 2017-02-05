def save(filename,string):
 filename=filename+".txt"
 fo=open(filename,"w")
 fo.write(string)
 fo.close()
 
save("hello","helloworld")
