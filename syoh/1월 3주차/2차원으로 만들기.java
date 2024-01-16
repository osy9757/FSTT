class Solution {
    public int[][] solution(int[] num_list, int n) {
        int rows = num_list.length / n;
        int[][] answer = new int[rows][n];

        for (int i = 0; i < num_list.length; i++) {
            int row = i / n;
            int col = i % n;
            answer[row][col] = num_list[i];
        }
    return answer;
    }
}