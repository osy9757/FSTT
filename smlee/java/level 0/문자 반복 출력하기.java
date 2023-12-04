class Solution {
    public String solution(String my_string, int n) {
        StringBuffer answer = new StringBuffer();
        for (char s: my_string.toCharArray()){
            for (int i=0; i<n; i++){
                answer.append(s);
            }
        }
        return answer.toString();
    }
}