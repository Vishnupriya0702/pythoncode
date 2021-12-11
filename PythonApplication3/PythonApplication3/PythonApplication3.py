
def func(x):
    y=list(x.split())
    length=len(y)
    s=" "
    l=[]
    for i in range(-1,-(length+1),-1):
        l.append(y[i])
        #print(l)
    
    #return l
    for i in l:
        s=s+' '+i
        
    return s

print(func("python is a great language"))
