a=[1,2,3,4,5]
odd=[]
even=[]
for i in a:
    if i % 2==0:
        even.append(i)
    else:
        odd.append(i)   
print ("odd:",*odd)
print("even:",*even)         