b=0
c=0
d=0
with open("data.dat","r") as a:
    for y in a:
        c=0
        d=0
        li=list(y)
        
        for z in range(len(li)):
            for x in li[z]:

                #print(x," ",li[z])
                
                if x=='1':
                    c=c+1
                    #print(c)
                elif x=='0':
                    d=d+1
                #print(d,":",c)
        if d%3==0 or c%2==0:
            b=b+1
                
                
            
    print(b,c,d)
        