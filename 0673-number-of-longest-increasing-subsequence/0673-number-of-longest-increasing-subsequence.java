class Solution {
    public int findNumberOfLIS(int[] nums) {
        int dp[]=new int[nums.length];
        Arrays.fill(dp,1);
        int[] count=new int[nums.length];
        Arrays.fill(count,1);
        
        for(int i=1;i<nums.length;i++){
            int lis=0;
            for (int j=0;j<i;j++){
                if (nums[i]>nums[j]){
                    if (dp[j] + 1 > dp[i]){
                        dp[i] = dp[j] + 1;
                        count[i]=count[j];
                        lis=Math.max(lis, dp[i]);
                    }
                    else if (dp[j] + 1 == dp[i]){
                        count[i]+=count[j];
                    }
                }
            }
        }
        long MAX=0;
        for (int i=0;i<dp.length;i++){
            if (MAX<dp[i]){
                MAX=dp[i];
            }
        }
        int result=0;
        for(int i=0;i<dp.length;i++){
            if (dp[i]==MAX){
                result+=count[i];
            }
        }
        return result;
    }
}