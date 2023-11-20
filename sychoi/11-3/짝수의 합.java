class Solution {
    public int solution(int n) {
        int answer = 0;
        for(int i=0; i <= n; i=i+2){
            answer = answer + i;
        }
        return answer;
    }
}