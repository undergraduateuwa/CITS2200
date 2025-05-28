
def binary_search(arr,tar,l,r):
    if l > r:
        return -1
    mid = (l+r)//2
    if tar == arr[mid]:
        return mid
    elif tar > arr[mid]:
        return binary_search(arr,tar,mid+1,r)
    else:
        return binary_search(arr,tar,l,mid-1)


print(binary_search([1,2,3,4,5,6,7,8,9],5,0,len([1,2,3,4,5,6,7,8,9])))