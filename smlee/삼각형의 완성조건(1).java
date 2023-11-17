import java.util.*;
class Solution {
    public int solution(int[] sides) {
        Arrays.sort(sides);
        int sum = 0;
        for (int i=0; i<sides.length-1; i++){
            sum += sides[i];
        }
        if (sum > sides[sides.length-1]) {
            return 1;
        } else {
            return 2;
        }
    }
}