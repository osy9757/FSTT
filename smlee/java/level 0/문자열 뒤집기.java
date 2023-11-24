class Solution {
    public String solution(String my_string) {
        String answer;
        StringBuffer s = new StringBuffer(my_string);
        answer = s.reverse().toString();
        return answer;
    }
}