class Solution:
    def kthsmallest(self,arr1,arr2,k):
       
        n1 = len(arr1)
        n2 = len(arr2)

        # why the smaller array
        if n1 > n2:
            n1,n2 = n2,n1
            arr1,arr2 = arr2,arr1

        
        low = max(0,k-n2)
        high = min(k,n1)

        while(low<=high):

            cut1 = (low+high)//2 


            cut2 = k - cut1 # to pick from n2

            l1 = float('-inf') if cut1 == 0 else arr1[cut1-1]
            r1 = float('inf') if cut1 == n1 else arr1[cut1]
            l2 = float('-inf') if cut2 == 0 else arr2[cut2-1]
            r2 = float('inf') if cut2 == n2 else arr2[cut2]

            if l1 <= r2 and l2 <= r1:
                return max(l1,l2)
            elif l1 > r2:
                high = cut1 -1 
            else:
                low = cut1 + 1
        


            
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        n1 = len(nums1)
        n2 = len(nums2)

        if (n1+n2) & 1 == 1:
            return self.kthsmallest(nums1,nums2,(n1+n2)//2+1)
        else:
            return (self.kthsmallest(nums1,nums2,(n1+n2)//2)+self.kthsmallest(nums1,nums2,(n1+n2)//2+1))/2.0



