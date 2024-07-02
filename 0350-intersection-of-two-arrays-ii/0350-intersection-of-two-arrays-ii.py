class Solution(object):
    def intersect(self, nums1, nums2) -> List[int]:

        def binary_search(num, target)-> bool:
            l,h=0,len(num)-1
            while(l<=h):
                m=(l+h)//2
                if (num[m]==target):
                    num.pop(m)
                    return True
                elif (num[m]>target):
                    h=m-1
                elif (num[m]<target):
                    l=m+1
            return False
    
        nums1.sort()
        nums2.sort()
        result=[]
        
        for x in nums1:
            if (binary_search(nums2,x)==True):
                result.append(x)

        return result