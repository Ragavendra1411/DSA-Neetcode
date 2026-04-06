class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums

        # Bubble sort
        # for i in range(1,len(nums)):
        #     for j in range(1,len(nums)):
        #         if nums[j]<nums[j-1]:
        #             temp = nums[j]
        #             nums[j] = nums[j-1]
        #             nums[j-1]=temp
        
        # return nums

        # merge sort
        def mergeSort(arr,l,r):
            if l>=r:
                return 
            m=(l+r)//2

            mergeSort(arr,l,m)
            mergeSort(arr,m+1,r)
            merge(arr,l,r,m)

        def merge(a,l,r,m):
            left = a[l:m+1]
            right = a[m+1:r+1]
            i=l
            j,k=0,0
            while j<len(left) and k<len(right):
                if left[j]<right[k]:
                    a[i]=left[j]
                    j+=1
                else:
                    a[i]=right[k]
                    k+=1
                i+=1
            while j<len(left):
                a[i]=left[j]
                j+=1
                i+=1
            while k<len(right):
                a[i]=right[k]
                k+=1
                i+=1


        mergeSort(nums,0,len(nums)-1)
        return nums




        