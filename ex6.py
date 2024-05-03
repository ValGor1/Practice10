file = open('input.txt', 'r')
a = 0
c = 'Yes'
d = 'NO'
e = 'ERROR'
f = ''
counter = -1
for line in file:
    first_line = file.readline()
    counter += 1

if first_line == counter:
    f == c
elif first_line != counter:
    f == d
else:
    f == e
file.close()

file2 = open('output.txt', 'w')
file2.write(f)
file2.close()
