import java.util.*;

class Solution {
    public int[] solution(int n, int[] numlist) {
        List<Integer> tempAnswer = new ArrayList<>();
        for (int num : numlist) {
            if (num % n == 0) {
                tempAnswer.add(num);
            }
        }
        int[] answer = new int[tempAnswer.size()];
        for (int i = 0; i < tempAnswer.size(); i++) {
            answer[i] = tempAnswer.get(i);
        }
        return answer;
    }
}