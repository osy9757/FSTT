class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        for (int arr:array) {
            if (arr == n) 
                answer += 1;
        }
        return answer;
    }
}