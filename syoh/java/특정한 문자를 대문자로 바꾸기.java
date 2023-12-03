class Solution {
    public String solution(String my_string, String alp) {
        String answer = "";
        for(int i=0; i<my_string.length(); i++) {
            if(my_string.charAt(i) == alp.charAt(0))
                answer += (char)((int)(my_string.charAt(i)) - 32);
            else
                answer += my_string.charAt(i);
        }
        return answer;
    }
}