file = open("input.txt",'r')
a = ''
for line in file:
    a += line[0]
file.close()

file2 = open('output.txt', 'w')
file2.write(a)
file2.close()