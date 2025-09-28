
def aaraymean(arr , arr_s) :

    total_sum = 0

    for i in range(0 , arr_s) :
        total_sum += arr[i]

    return float(total_sum / arr_s)

def arraymeadian(arr , arr_s) :

    sorted(arr)

    if arr_s % 2 != 0 :

        return float(arr[int(arr_s / 2)])

    return float((arr[int((arr_s - 1) / 2 )] + arr[int(arr_s / 2)]) / 2)

arr = [1,2,3,4,5,6,7]
arr_s = len(arr)

print(aaraymean(arr, arr_s))
print(arraymeadian(arr,arr_s))
    
