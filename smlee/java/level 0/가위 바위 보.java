class Solution {
    public String solution(String rsp) {
        StringBuffer answer = new StringBuffer();
        char[] charArr = rsp.toCharArray();
        
        for (char c: charArr){
            if (c == '2'){
                answer.append('0');
            } else if (c == '0'){
                answer.append('5');
            } else if (c == '5'){
                answer.append('2');
            }
        }
        
        return answer.toString();
    }
}