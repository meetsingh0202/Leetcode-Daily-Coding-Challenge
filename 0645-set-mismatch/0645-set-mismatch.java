class Solution {public int[] findErrorNums(int[] nums) {
	boolean[] visited = new boolean[10001];
	int duplicate = 0, sum = 0, n = nums.length;
	for (int i: nums) {
		if (visited[i]) {
			duplicate = i;
		}
		visited[i] = true;
		sum += i;
	}
	int nsum =  (n * (n+1)) / 2;
	return new int[] {duplicate, duplicate + nsum - sum};
}
}