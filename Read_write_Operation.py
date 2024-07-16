"""f=open("C:\\Users\\gazala parveen\\OneDrive\\Documents\\txt files\\demo.txt","r")
f_out=open("C:\\Users\\gazala parveen\\OneDrive\\Documents\\txt files\\demoWriteBack.txt","w")
for line in f:
    tokens=line.split(" ")
    f_out.write("wordcount:" +str(len(tokens))+ line)
f.close()
f_out.close()"""


with open("C:\\Users\\gazala parveen\\OneDrive\\Documents\\txt files\\demo.txt","r") as f:

    print(f.read())
print(f.closed)

