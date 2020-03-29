heap = []
temp_arr = []
sorted_arr = []
size = int(input("Enter size : "))

[temp_arr.append(int(input("Enter Data : "))) for i in range(size)]

rootIndex = 0
leftIndex = 0
rightIndex = 0

for k in range(size):
    for i in range(len(temp_arr)):
        value = temp_arr.pop(0)
        heap.append(value)
        index = i
        for j in range(0, i):
            if index % 2 != 0:
                rootIndex = int((index - 1) / 2)
            else:
                rootIndex = int((index - 2) / 2)
            if value > heap[rootIndex]:
                temp = heap[index]
                heap[index] = heap[rootIndex]
                heap[rootIndex] = temp
                index = rootIndex
    temp_arr = heap
    heap = []
    sorted_arr.append(temp_arr.pop(0))


print(sorted_arr)


