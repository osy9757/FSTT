class Solution {
    public String solution(String my_string) {
        StringBuffer sb = new StringBuffer(my_string);
        String reversedMyString = sb.reverse().toString();
        return reversedMyString;
    }
}