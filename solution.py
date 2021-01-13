from collections import Counter
class Solution:
    def majorityElement(self, nums) :
        dict1=Counter(nums)
        dict1=sorted(dict1.items(), key = 
             lambda kv:(kv[1]),reverse=True)
        return dict1[0][0]


s=Solution()
arr=[3,2,3]
print(s.majorityElement(arr))    