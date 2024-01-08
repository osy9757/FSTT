class Solution {
    public int solution(int order) {
        int answer = 0;
        for (;order!=0;) {
            if((order%10)==3 || (order%10)==6 || (order%10)==9) {
                answer+=1;
            }
            order /= 10;
        }
        return answer;
    }
}