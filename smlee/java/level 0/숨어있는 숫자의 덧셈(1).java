class Solution {
    public int solution(String my_string) {
        int answer = 0;
        for (int i=0; i<my_string.length(); i++){
            char s = my_string.charAt(i);
            int s_int = s-'0';
            if (0 <= s_int && s_int <= 9 ){
                answer += s_int;
            }
        }
        return answer;
    }
}