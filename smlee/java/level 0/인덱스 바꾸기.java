class Solution {
    public String solution(String my_string, int num1, int num2) {
        String answer = "";

        char[] ch = my_string.toCharArray();

        ch[num1] = my_string.charAt(num2);
        ch[num2] = my_string.charAt(num1);

        answer = String.valueOf(ch);
        return answer;
    }
}