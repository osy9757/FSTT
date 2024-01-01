class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int odd = 0; // 홀수
        int even = 0; // 짝수
        for(int i = 0; i<num_list.length; i++){
            if(num_list[i]%2 == 0) { // 짝수
                even = even*10 + num_list[i];
            } else { // 홀수
                odd = odd*10 + num_list[i];
            }
        }
        answer = even + odd;
        return answer;
    }
}