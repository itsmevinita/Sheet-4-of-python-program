a=[1,2,3,4]
even_count = sum(x%2==0 for x in a)
odd_count = sum(x % 2 != 0 for x in a) 
D=abs(even_count - odd_count)
print(D)        