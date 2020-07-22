n = input()
p = []
for i in range(int(n)):
    x = input()
    p.append(int(x))
    
m = 0
a = 0
for i in range(int(n)):
    for j in range(i+1,int(n)):
        if ((p[j]-p[i])-m)>0:
            m = p[j]-p[i]
            a = i
        
print(m)
print(a+1)