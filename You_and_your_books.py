
class Solution:
    # Function should return an integer
    # a - list/array containing height of stacks respectively
    def max_Books(self, n, k, arr):
        max_books = 0
        current_books = 0
        for i in range(n):
            if arr[i] <= k:
                current_books += arr[i]
            else:
                if current_books > max_books:
                    max_books = current_books
                current_books = 0
        # Final check to update max_books in case the valid subarray reaches the end
        if current_books > max_books:
            max_books = current_books
        return max_books