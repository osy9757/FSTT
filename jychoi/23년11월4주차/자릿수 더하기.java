class Solution {
    public int solution(int n) {
        int answer = 0;
        int temp = n;
        int numDigits = (int) Math.log10(n) + 1;
        for (int i = numDigits-1; i >= 0; i--){
            answer += temp / Math.pow(10, i);
            temp = temp % (int) Math.pow(10, i);
        }
        return answer;
    }
}