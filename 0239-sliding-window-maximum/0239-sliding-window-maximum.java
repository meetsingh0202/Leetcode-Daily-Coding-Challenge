class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> deque = new ArrayDeque<Integer>();
        int left = 0;
        int right = 0;
        int[] res = new int[nums.length - k + 1];
        int index = 0;
        while (right < nums.length){
            while (deque.size() > 0 && nums[right] >= nums[deque.peekLast()]){
                deque.removeLast();
            }
            deque.addLast(right);
            if (left > deque.peekFirst()){
                deque.removeFirst();
            }
            if (right + 1 >= k){
                res[index++] = nums[deque.peekFirst()];
                left += 1;
            }
            right += 1;
        }
        return res;
    }
}