class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        int freeDrink = n / 10;
        answer = n * 12000 + (k-freeDrink) * 2000;
        return answer;
    }
}