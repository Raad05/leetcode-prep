# Stack => Last in first out(LIFO)
print("Stack:")
nums1 = []
# push
nums1.append(1)
nums1.append(2)
nums1.append(3)
print(nums1)
# pop
nums1.pop()
print(nums1)

# Queue => First in first out(FIFO)
from collections import deque

print("Queue:")
nums2 = deque([])
nums2.append(2)
nums2.append(3)
nums2.append(4)
print(nums2)

nums2.appendleft(1)
print(nums2)

nums2.remove(2)
print(nums2)

nums2.popleft()
print(nums2)

nums2.pop()
print(nums2)