class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        if (num_list.length >= 11) {
            for(Integer n: num_list) {
                answer += n;
            }
        } else {
            answer = 1;
            for(Integer n: num_list) {
                answer *= n;
            }
        }
        return answer;
    }
}