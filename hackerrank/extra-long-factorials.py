def add_arrays(arr1, arr2):
    for i in range(len(arr1) - 1, -1, -1):
        print(arr1[i])
        if arr1[i] + arr2[i] > 9:
            arr1[i-1] += 1
        arr1[i] = (arr1[i] + arr2[i]) % 10
    return arr1

print(add_arrays([1,9,9], [0,0,1]))
