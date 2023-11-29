class Solution {
    public String solution(String my_string) {
        String answer = my_string;

        answer = answer.replaceAll("a", "");
        answer = answer.replaceAll("e", "");
        answer = answer.replaceAll("i", "");
        answer = answer.replaceAll("o", "");
        answer = answer.replaceAll("u", "");

        return answer;
    }
}