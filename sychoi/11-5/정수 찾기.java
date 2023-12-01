class Solution {
    public int solution(int[] num_list, int n) {
        int answer = 0;
        for (int each:num_list) {
            if (each == n){
                answer = 1;
                break;
            }
        }
        return answer;
    }
}