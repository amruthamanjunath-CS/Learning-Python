
n=int(input("enter a number:"))
digit=bin(n)[2:] 
x=[]
count=0
for i in digit:
    if i=="1":
           x.append(count)
           count+=1
    else:
         count+=1       
diff1=[]
for i in range(0,len(x)-1):
    diff1.append(x[i+1]-x[i])
if diff1:    
    print((max(diff1)) )
else:
     print("0")              
            
        
        
            
                        



              
