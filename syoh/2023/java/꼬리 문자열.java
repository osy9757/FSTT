class Solution {
    public String solution(String[] str_list, String ex) {
        String answer = "";
        for (String subStr : str_list) {
            if (!subStr.contains(ex)) {
                answer += subStr;
            }
        }
        return answer;
    }
}