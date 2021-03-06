class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        if len(arr)==1:
            return 0;
        left = 0;
        right = len(arr) - 1;
        while left <= right :
            mid = (left + right) // 2;
            if mid == 0 and arr[mid] > arr[mid + 1]:
                return mid
            if mid == len(arr) - 1 and arr[mid] > arr[mid - 1]:
                return mid
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            if arr[mid] < arr[mid + 1]:
                left = mid + 1;
            else :
                right = mid - 1;

