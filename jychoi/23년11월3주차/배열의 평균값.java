class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        for (int num : numbers) {
            answer += num;
        }
        answer = answer / numbers.length;
        return answer;
    }
}