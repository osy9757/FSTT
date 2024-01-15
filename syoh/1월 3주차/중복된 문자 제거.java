import java.util.*;

class Solution {
    public String solution(String my_string) {
        HashSet<Character> seen = new HashSet<>();
        StringBuilder answer = new StringBuilder();

        for (char ch : my_string.toCharArray()) {
            if (!seen.contains(ch)) {
                seen.add(ch);
                answer.append(ch);
            }
        }

        return answer.toString();
    }
}