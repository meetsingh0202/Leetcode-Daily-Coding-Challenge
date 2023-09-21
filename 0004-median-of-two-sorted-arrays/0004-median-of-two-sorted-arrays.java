class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) 
    {
        int size=nums1.length+nums2.length;
        int []nums3=new int[size];
        for(int i=0;i<nums1.length;i++)
            nums3[i]=nums1[i];
        for(int i=0;i<nums2.length;i++)
            nums3[i+nums1.length]=nums2[i];
        Arrays.sort(nums3);
        if(nums3.length%2!=0)
        {
            int c=nums3.length/2;
            double b=Math.ceil(c);
            int b2=(int)b;
            return nums3[b2];
        }
        else
        {
            int a=(nums3.length/2)-1;
            double res=(nums3[a]+nums3[a+1]);
            return res/2;
        }
        
    }
}