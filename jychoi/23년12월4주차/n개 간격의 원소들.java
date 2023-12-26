class Solution {
    public int[] solution(int[] num_list, int n) {
        int len = num_list.length;
        int num = 0;

        if (len % n == 0) {
            num = len / n;
        } else {
            num = len / n + 1;
        }

        int[] answer = new int[num];

        for (int i = 0; i < num; i++) {
            answer[i] = num_list[i * n];
        }

        return answer;
    }
}
