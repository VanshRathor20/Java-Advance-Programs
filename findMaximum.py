class Solution:
    def findMaximum(self, arr):
        n = len(arr)
        low = 0
        high = n - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # If mid is the peak element
            if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid]):
                return arr[mid]
            
            # If the middle element is part of the increasing sequence
            elif mid < n - 1 and arr[mid] < arr[mid + 1]:
                low = mid + 1
            
            # Otherwise, move to the left part
            else:
                high = mid - 1
