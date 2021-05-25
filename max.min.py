

a=[1,2,3,7,4,67,87,54]
i=0
max=a[i]
min=a[i]
while i<len(a):
    if a[i]>max:
        max=a[i]
    elif a[i]<min:
        min=a[i]
    i+=1
print(("max",max,"min",min))



