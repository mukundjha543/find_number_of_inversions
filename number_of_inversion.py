ans = 0
def merge(left, right):
    result = []
    i, j = 0, 0
    k, l = 0, 0
    while i < len(left) and j < len(right):
        while k < len(left) and l < len(right):
            if left[k] > right[l]:
                global ans 
                print(left, right)
                ans += len(left) - k
                l += 1
            else:
                k += 1
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        
    result += left[i:]
    result += right[j:]

    return result

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = int(len(arr)/2)

    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    return merge(left, right)


print(mergesort([52244275, 123047899, 493394237, 922363607, 378906890, 188674257, 222477309, 902683641, 860884025, 339100162]))
print(ans)