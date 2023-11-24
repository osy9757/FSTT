class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        for (int a: array) {
            if (a == n) {
                answer++;
            }
        }
        return answer;
    }
}