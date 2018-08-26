a=list(input("Enter the input:"))
b=[]
z=[]
s=0
r=0
opp=['+',"-","*","/","(",")"]

for i,v in enumerate(a):
    s+=1
    r=s
    if i == 0:
        s -= 1
    if v=="+" or v=="-" or v=="*" or v=="/" or v=="(" or v==")":
        for j in opp:
            if v==j:
                s-=1
                for k in range(i-s,i):
                    a[0]=str(a[0])+a[k]
                if a[0]!="(" and a[0]!="-":
                    if a[0]!=0:
                        b.append(float(a[0]))
                b.append(v)
                a[0]=0
                s=0
                
for i in range(len(a)-r,len(a)):
    a[0]=str(a[0])+a[i]
    
if a[len(a)-1]!=")":
    b.append(float(a[0]))
    
if b[0]=="-":
    b[0]="-"+str(b[1])
    b[0]=float(b[0])
    del b[1]
    
for i, v in enumerate(b):
    if b[i] == "-" and (b[i - 1] == "(" or b[i - 1] == "*" or b[i - 1] == "/"):
        b[i] = b[i] + str(b[i + 1])
        b[i] = float(b[i])
        del b[i + 1]
        
def calc():
    global er
    cd = 0
    cm = 0
    cs = 0
    cp = 0
    for j in z:
        if j=="/":
            cd+=1
        elif j=="*":
            cm+=1
        elif j=="-":
            cs+=1
        elif j=="+":
            cp+=1
    for h in range(cd):
        for i,v in enumerate(z):
            if v=="/":
                d1=z[i-1]
                d2=z[i+1]
                try:
                    d3=d1/d2
                except ZeroDivisionError:
                    er=1
                    print("Can\'t divide by 0")
                    break;
                z[i]=d3
                del z[i+1]
                del z[i-1]
                break
    for h in range(cm):
        for i,v in enumerate(z):
            if v=="*":
                m1 = z[i - 1]
                m2 = z[i + 1]
                m3 = m1 * m2
                z[i] = m3
                del z[i + 1]
                del z[i - 1]
                break
    for h in range(cp):
        for i,v in enumerate(z):
            if v=="+":
                a1 = z[i - 1]
                a2 = z[i + 1]
                a3 = a1 + a2
                z[i] = a3
                del z[i + 1]
                del z[i - 1]
                break
    for h in range(cs):
        for i,v in enumerate(z):
            if v=="-":
                s1 = z[i - 1]
                s2 = z[i + 1]
                s3 = s1 - s2
                z[i] = s3
                del z[i + 1]
                del z[i - 1]
                break
    return z[0]

ob=0
cb=0
numcount=0
ccc=0

for ijk in b:
    if ijk=="(":
        ccc+=1
        
for ii in range(ccc):
    for i,v in enumerate(b):
        if v=="(":
            ob=i
        elif v==")":
            cb=i
            for k in range(ob+1,cb):
                z.append(b[k])
            ans=calc()
            b[ob+1]=ans
            if cb<len(b)-1:
                if b[cb+1]!="+" and b[cb+1]!="-" and b[cb+1]!="*" and b[cb+1]!="/" and b[cb+1]!="(" and b[cb+1]!=")":
                    b[cb]="*"
                else:
                    del b[cb]
            elif cb==len(b)-1:
                b.pop()
            for df in range(ob+2,cb):
                del b[ob+2]
            if b[ob-1]!="+" and b[ob-1]!="-" and b[ob-1]!="*" and b[ob-1]!="/" and b[ob-1]!="(" and b[ob-1]!=")" and ob!=0:
                b[ob]="*"
            else:
                del b[ob]
            break
        for ij in range(len(z)):
            z.pop()
    for ij in range(len(z)):
        z.pop()
for i,v in enumerate(b):
    if b[i]=="*" and b[i+1]=="*":
        del b[i+1]
for i in range(len(b)):
    z.append(b[i])
    
answer=0
answer=calc()

try:
    if er==0:
        print(answer)
except:
    print(answer)
