d = input()
x = 10**(int(d)-1)
y = 9
z = str(y)
s = int(d)
while s>1:
    z += str(9)
    s = s-1
y = int(z)
file1 = open("myFirstFile.txt", "w")
a = []
n = x
while n<y:
    h = 0
    for i in range(2,n):
        if(n%i)==0:
            h = 1
            break
    if h==0:
        a.append(n)
    n = n+1   
print(a)
p = a[0]
l = len(a)
for index in range(1,l):
    i = a[index]
    if (i-p)==2:
        file1.write(str(p)+" "+str(i)+"\n")
        print(str(p)+" "+str(i))
    p = i
file1.close()