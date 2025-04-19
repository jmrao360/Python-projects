def bubbleSrt(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


myArray = [1,0,3,2,6,5]
print(myArray)
bubbleSrt(myArray)
print(myArray)