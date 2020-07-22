n = input()
p = int(n)+1
while True:
    a = [d for d in str(p)]
    a.reverse()
    q = ''.join(a[0:len(a)])
    if p==int(q):
        print(p)
        break
    p+=1