class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        for (Integer e : array) {
            if(e == n) answer++;
        }
        return answer;
    }
}