class Solution {
    public int solution(int a, int b) {
        int answer = Integer.parseInt(a+""+b) >= Integer.parseInt(b+""+a)?
            Integer.parseInt(a+""+b) : Integer.parseInt(b+""+a);
        return answer;
    }
}