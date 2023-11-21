import java.util.Arrays;

class Solution {
    public int solution(int[] array) {
        int answer = 0;
        Arrays.sort(array);
        int idx = 0;
        if (array.length % 2 == 0) {
            idx = (int) array.length / 2 - 1;
            answer = array[idx];
        } else {
            idx = (int) array.length / 2;
            answer = array[idx];
        }
        return answer;
    }
}