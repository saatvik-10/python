arr = ['messi', 'ronaldo', 'neymar']
print(arr)

print("-----------------------------------------------------------------------------------------------------")

arr = ['messi', 'ronaldo', 'suarez', 'neymar']
print(arr[0])
print(arr[1:3])
print(arr[-1])
print(arr[0:4])

print("-----------------------------------------------------------------------------------------------------")

arr2 = arr[:]
print(arr2)

arr2.append("mbappe")
print(arr2)

arr[1] = "xavi"

print(arr)

print("-----------------------------------------------------------------------------------------------------")

ans = arr + arr2
print(ans)

del arr[1]
print(arr)

print("-----------------------------------------------------------------------------------------------------")

for i, num in enumerate(arr):
    print("Index {} in array is: {}" .format(str(i), num))
    
print("-----------------------------------------------------------------------------------------------------")

arr3 = arr[:]
ini = ["M", "S", "N"]

for i, n in zip(arr3, ini):
    print("{} is {}" .format(str(i), n))
    
print("-----------------------------------------------------------------------------------------------------")

print('pedri' in arr)
print('messi' in arr)

print("-----------------------------------------------------------------------------------------------------")

arr2.sort()
print(arr2)

arr2.sort(reverse=True)
print(arr2)

ans = sorted(arr2)
print(ans)