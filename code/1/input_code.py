def solution(arr):
   max_value = None
   for num in arr:
       if (max_value is None or num > max_value):
           max_value = num
   return max_value