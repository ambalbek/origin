myfile=open('aziz.csv', 'r+')
myfile.write('Hello World!')
myfile.writelines(['put some comments here',])
for i in myfile():
    print(i)

