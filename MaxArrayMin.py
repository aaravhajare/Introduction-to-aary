
def emin(a , s ) :

    temp = a[0]

    for  i in range(1 , s) :

        temp = min(temp , a[i])
    return temp

def emax (a ,s ) :

    temp = a[0]

    for  i in range(1,s) :

        temp = max(temp , a[i])

    return temp

arr = [1,2,3,4,6,7]
s = len(arr)

print(emin(arr , s))
print(emax(arr  ,s ))