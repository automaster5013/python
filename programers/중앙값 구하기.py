def solution(array):
   array.sort()
   center_index = len(array) // 2

   return array[center_index]

###################################################################

def solution(array):
    n = len(array)
    for i in range(n):
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                
    return array[n // 2]

###################################################################












































