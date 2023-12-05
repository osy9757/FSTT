class Solution {
    public int[] solution(int n) {
        int[] answer = new int[(n + 1) / 2];
        int value = 1;

        for (int i = 0; i < answer.length; i++) {
            answer[i] = value;
            value += 2;
        }
        return answer;
    }
}