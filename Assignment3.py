# Q1
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[0] + nums[1] + nums[2]
        for i in range(n-2):
            l, r = i + 1, n - 1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                if abs(ans - target) > abs(sum3 - target):
                    ans = sum3
                if sum3 == target: return target
                if sum3 > target:
                    r -= 1  
                else:
                    l += 1  
        return ans

# Q2
def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    result = set()

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left = j + 1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if current_sum == target:
                    result.add((nums[i], nums[j], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

    return list(result)

# Q3
def nextPermutation(nums):
    # Find the first index i from the right where nums[i] > nums[i-1]
    i = len(nums) - 1
    while i > 0 and nums[i] <= nums[i-1]:
        i -= 1

    if i == 0:
        # The given permutation is the largest possible arrangement
        nums.reverse()
        return

    # Swap nums[i-1] with the smallest element greater than nums[i-1] to its right
    j = len(nums) - 1
    while nums[j] <= nums[i-1]:
        j -= 1
    nums[i-1], nums[j] = nums[j], nums[i-1]

    # Reverse the elements to the right of index i
    left, right = i, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

# Q4
class Solution:
    def recursive_serach(self, low, high):
        if low<=high:
            mid = low +(high-low)//2
            if self.nums[mid]==self.target:
                return mid
            elif self.nums[mid]<self.target:
                return self.recursive_serach(mid+1, high)
            elif self.nums[mid]>self.target:
                return self.recursive_serach(low, mid-1)
        return low
        
    def searchInsert(self, nums: list[int], target: int) -> int:
        self.nums = nums
        self.target = target 
        
        low, high = 0, len(nums)-1
        if self.target<self.nums[low]:
            return low
        if self.target>self.nums[high]:
            return high+1
        if low<=high:
            return self.recursive_serach(low, high)
            
            
        return low

# Q5
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
        return [1]+[0]*len(digits)
    
# Q6
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = nums[0]
        for i in range(1,len(nums)):
            result = result ^ nums[i]
        return result

# Q7
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def f(a, b):
            return str(a) if a == b else f'{a}->{b}'

        n = len(nums)
        if n == 0:
            return [f(lower, upper)]
        ans = []
        if nums[0] > lower:
            ans.append(f(lower, nums[0] - 1))
        for a, b in pairwise(nums):
            if b - a > 1:
                ans.append(f(a + 1, b - 1))
        if nums[-1] < upper:
            ans.append(f(nums[-1] + 1, upper))
        return ans
    
# Q8
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
       # If there are no meetings, we don't need any rooms.
        if not intervals:
            return 0
        num_rooms = 0
# Separate out the start and the end timings and sort them individually.
        start_timings = sorted(i[0] for i in intervals)
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)
# The two pointers in the algorithm: e_ptr and s_ptr.
        end_pointer = 0
        start_pointer = 0
# Until all the meetings have been processed
        while start_pointer < L:
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            print(start_timings[start_pointer],end_timings[end_pointer])
            if start_timings[start_pointer] < end_timings[end_pointer]:
                # Free up a room and increment the end_pointer.
                num_rooms += 1
            else:
                end_pointer += 1
        start_pointer += 1
        return num_rooms

