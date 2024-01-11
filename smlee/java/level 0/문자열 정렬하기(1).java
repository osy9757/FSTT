import java.util.*;
class Solution {
    public int[] solution(String my_string) {
        List<Integer> answer = new ArrayList<>();
        char[] ch = my_string.toCharArray();
        for (int i=0; i<my_string.length(); i++){
            try {
                String s = Character.toString(ch[i]);
                int n = Integer.parseInt(s);
                answer.add(n);
            } catch(Exception e){}
        }
        // 리스트를 정렬
        Collections.sort(answer);
        // 리스트를 배열로 변환
        return answer.stream().mapToInt(x -> x).toArray();
    }
}
