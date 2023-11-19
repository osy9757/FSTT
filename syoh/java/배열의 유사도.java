import java.util.*;

class Solution {
    public int solution(String[] s1, String[] s2) {
        int answer = 0;
        
        List<String> strs1 = new ArrayList<>(Arrays.asList(s1));
        List<String> strs2 = new ArrayList<>(Arrays.asList(s2));
        for (String s:strs1){
            if (strs2.contains(s))
                answer+=1;
        }
        
        return answer;
    }
}