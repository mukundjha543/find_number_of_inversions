def permute(arr):
    if len(arr) == 1:
        return [arr]

    ans = []

    for i in range(len(arr)):
        l = [arr[i]]
        m = arr[:i]+arr[i+1:]

        for per in permute(m):
            ans.append(l+per)

    return ans

print(permute([1,2,3]))
