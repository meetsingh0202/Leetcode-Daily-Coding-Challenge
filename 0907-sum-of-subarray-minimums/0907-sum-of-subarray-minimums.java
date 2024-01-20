class Pair{
    int element;
    int Mincount;
    Pair(int ele, int count){
        element = ele;
        Mincount = count;
    }
}
class Solution {
    int MOD = (int) Math.pow(10, 9) + 7;
    public int sumSubarrayMins(int[] arr) {
        int n = arr.length;
        long[] left = new long[n];
        long[] right = new long[n];
        
        Stack <Pair> lesser = new Stack<>();
        Stack <Pair> greater = new Stack<>();
        
        for(int i = 0; i < n; i++){
            int currElement = arr[i];
            int count = 1;
            while (lesser.size() > 0 && lesser.peek().element > currElement){
                count += lesser.peek().Mincount;
                lesser.pop();
            }
            lesser.push(new Pair(currElement, count));
            left[i] = count;
        }
        for(int i = n - 1; i >= 0; i--){
            int currElement = arr[i];
            int count = 1;
            while (greater.size() > 0 && greater.peek().element >= currElement){
                count += greater.peek().Mincount;
                greater.pop();
            }
            greater.push(new Pair(currElement, count));
            right[i] = count;
        }
        
        long ans = 0;
        for(int i = 0; i < n; i ++){
            long currElement = (long) arr[i];
            ans = ans % MOD + (arr[i] * left[i] * right[i] ) % MOD;
        }
        return (int) ans;
    }
}