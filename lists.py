nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3 
n = 3

def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    total_size = m + n
    count = 0
    for index, num in enumerate(nums1):
        next_num = nums2[count]
        if next_num < nums1[index]:
            nums1.insert(index, next_num)
            nums1.pop()
        

        if count < n:
            count += 1
