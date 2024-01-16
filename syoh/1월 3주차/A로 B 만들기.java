import java.util.*;

class Solution {
    public int solution(String before, String after) {
        
        char[] beforeArr = before.toCharArray();
        char[] afterArr = after.toCharArray();
        Arrays.sort(beforeArr);
        Arrays.sort(afterArr);

        if (Arrays.equals(beforeArr, afterArr)) {
            return 1;
        } else {
            return 0;
        }
    }
}