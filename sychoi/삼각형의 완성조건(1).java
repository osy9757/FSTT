import java.util.*;

class Solution {
    public int solution(int[] sides) {
        int answer = 0;
        int maxLen = 0;
        int sumOtherLen = 0;

        for (int s : sides) {
            if (maxLen < s) {
                sumOtherLen = sumOtherLen + maxLen;
                maxLen = s;
            } else {
                sumOtherLen = sumOtherLen + s;
            }
        }

        if (sumOtherLen > maxLen) {
            answer = 1;
        } else {
            answer = 2;
        }

        return answer;
    }
}