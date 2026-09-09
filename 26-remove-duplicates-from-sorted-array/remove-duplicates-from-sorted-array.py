class Solution:
    def removeDuplicates(self,nums):
        if not nums:
            return 0
        off = 0
        cm = 1
        uniq=1
        while(cm<=(len(nums)-1)):
            if(nums[off]==nums[cm]):
                cm+=1
            elif(nums[off]!=nums[cm]):
                off+=1
                nums[off]=nums[cm]
                uniq+=1
        return uniq