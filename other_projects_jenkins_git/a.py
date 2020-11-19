myfile=open('aziz.csv', 'w+')
myfile.write('Hello World!')
myfile.writelines(['\n1234567890','\nThis is the new line'])
for i in myfile:
    print(i)

