
def sort_asc(a):

    for i in range(len(a)):
        j=i+1
        for j in range(len(a)):
            if a[i]<a[j]:
                temp=a[j]
                a[j]=a[i]
                a[i]=temp
    
    return a
def sort_desc(a):

    for i in range(len(a)):
        j=i+1
        for j in range(len(a)):
            if a[i]>a[j]:
                temp=a[j]
                a[j]=a[i]
                a[i]=temp
    
    return a




arr = [1,3,5,10,4,20,100,2,5,6,2,3,5,4,9,0,2,3,512,12412,232]
print(sort_asc(arr))
print(sort_desc(arr))






