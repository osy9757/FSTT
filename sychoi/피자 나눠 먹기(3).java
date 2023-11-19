class Solution {
    public int solution(int slice, int n) {
        int answer = 0;
        if (n % slice == 0) {
            answer = (int) n / slice;
        } else {
            answer = (int) n / slice + 1;
        }
        return answer;
    }
}