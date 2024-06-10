class Solution(object):
    def twoSum(self, nums, target):
        for i in nums :
            for x in nums:
                sum = x + i
                if sum == target:
                    return [{nums.index(i)},{nums.index(x)}]
                    stop = True
                    break
                else:
                    continue
        if stop:
            break
        
    
        

       
        
        