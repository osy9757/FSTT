class Solution {
    public String solution(String my_string) {
        String answer = "";
        for (char ch : my_string.toCharArray()) {
            if (Character.isUpperCase(ch)) {
                answer += Character.toLowerCase(ch);
            } else if (Character.isLowerCase(ch)) {
                answer += Character.toUpperCase(ch);
            }
        }
        return answer;
    }
}
