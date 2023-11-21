class Solution {
    public int solution(int num1, int num2) {
        float answer = (float) num1 / (float) num2;
        answer = answer * 1000;
        return (int) answer;
    }
}