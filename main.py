prosti = []
n = 51013
e = 26389
M = 321
p = 0
q = 0

for i in range(0, 1001):
    prosti.append(i)
for i in range(2,11):
    for j in prosti:
        #print(i,j)
        if j % i == 0 and j != i:
            prosti.remove(j);
#for i in prosti:
    #print(i)

for i in prosti:
    for j in prosti:
        if i*j == n:
            p=i
            q=j
            break
    if p!=0:
        break
print("p,q:", p,q)

fi = (p-1) * (q-1)
d = 0

for i in range(1,fi):
    #print(i)
    if e*i % fi == 1:
        d=i
        break
print("d", d)

c=0
f=1

#print(bin(e))
#for i in range(2,bin(e).__len__()):
#    print(bin(e)[i])
for i in range(2, bin(e).__len__()):
    c = c*2
    f = (f*f) % n
    if bin(e)[i] == '1':
        c += 1
        f = (f*M) % n
    #print(i,f, bin(e)[i])
print("C", f)

Ct = f
c=0
f=1

for i in range(2, bin(d).__len__()):
    c = c*2
    f = (f*f) % n
    if bin(d)[i] == '1':
        c += 1
        f = (f*Ct) % n
    #print(i,f, bin(d)[i])
print("M", f)