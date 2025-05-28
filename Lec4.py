
def insert_sort(arr):
    for i in range(len(arr)-1):
        l = i
        r = i+1
        if arr[r] < arr[l]:
            temp = arr[r]
            while l >= 0 and temp < arr[l]:
                arr[r] = arr[r-1]
                r -= 1
                l -= 1
            arr[l+1] = temp
    return arr





arr = [1,2,3,4,-1,-100,5,1000,-1]
print(insert_sort(arr))