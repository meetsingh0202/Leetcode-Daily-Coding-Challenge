class Solution {
    public int[] sortArray(int[] nums) {
        
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        
        for(int i : nums){
            heap.offer(i);
        }
        
        int[] res = new int[nums.length];
        for(int i = 0; i < nums.length; i++){
            res[i] = heap.poll();
        }
        
        return res;
    }
}