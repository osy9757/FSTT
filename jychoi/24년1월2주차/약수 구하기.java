class Solution {
    public int[] solution(int n) {
        int a = 0;
        for(int i = 1; i <= n; i++) {
            if(n%i == 0) {
                a++;
            }
        }
        int[] answer = new int[a];
        int k = 0;
        for(int j = 1; j <= n; j++) {
            if(n % j == 0) {
                answer[k] = j;
                k++;
            }
        }
        return answer;
    }
}