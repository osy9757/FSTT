class Solution {
    public int solution(int order) {
        int answer = 0;
        int length = (int)(Math.log10(order)+1);
        for(int i = 0; i < length; i++){
            if(order % 10 == 3 || order % 10 == 6 || order % 10 == 9) {
                answer ++;
                order = order / 10;
            } else {
                order = order / 10;
            }
        }

        return answer;
    }
}