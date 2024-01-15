import java.util.*;
class Solution {
    public String solution(String my_string) {
        char[] arr = my_string.toLowerCase().toCharArray();
        Arrays.sort(arr);
        String answer = new String(arr);
        return answer;
    }
}