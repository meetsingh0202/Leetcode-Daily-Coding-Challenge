class Solution {
    public static boolean checkReaders(int[] books, int ReadLimit, int Students){
        int count = 1;
        int currSum = 0;
        for (int element : books){
            if (element + currSum <= ReadLimit){
                currSum += element;
            }
            else{
                count++;
                if (count > Students || element > ReadLimit){
                    return false;
                }
                currSum = element;
            }
        }
        return true;
    }
    public int shipWithinDays(int[] weights, int days) {
        int sum = 0;
        int low = 0;
        for (int elements : weights){
            sum += elements;
        }
        int ans = -1;
        int high = sum;
        while (low <= high){
            int mid = (low + high) >> 1;
            if (checkReaders(weights, mid, days)){
                ans = mid;
                high = mid - 1;
            }
            else{
                low = mid + 1;
            }
        }
        return ans;
    }
}
