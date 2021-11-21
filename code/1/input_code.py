def solution(arr):
    max = 0
    for i in range(1,len(arr)):
       if arr[i] > max:
          max = arr[i]
    return max