class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int i=1; ;i++) {
            if (6*i%n == 0)
                return i;
        }
    }
}