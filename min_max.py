
def max(a):
    for i in range(len(a)):
        max= a[0]
        j = i + 1
        for j in range(len(a)):
            if a[j] > max:
                max=a[j]

    return(max)

def min(a):
    for i in range(len(a)):
        min= a[0]
        j = i + 1
        for j in range(len(a)):
            if a[j] < min:
                min=a[j]

    return(min)

a = [1,2,3,4,12,1222,12212121,20201]
print(max(a))
print(min(a))
