class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length];
        for (int i = 0, n=num_list.length - 1; n >= 0; n--, i++) {
            answer[i] = num_list[n];
        }
        return answer;
    }
}