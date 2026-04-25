def fact(n):
    r = 1
    for i in range(1,n+1):
        r*=i
    return r

s = input()
n = len(s)
m = ''
for i in range(1,n+1):
    m+=str(i)



def comb(s):
    n = len(s)
    t = ['']*fact(n)
    
    if n == 1:
        return [s]
    i = 0
    for j in range(n):
        u = comb(s[0:j]+s[j+1::])
        for k in range(fact(n-1)):
            t[i] = s[j]+u[k]
            i+=1
    return t
u = comb(m)
result = ''
for i in u:
    word = ''
    for j in i:
        word+=s[int(j)-1]
    if result.find(word+'|') ==-1:
        result= result+word+'|'
print(result)

            
