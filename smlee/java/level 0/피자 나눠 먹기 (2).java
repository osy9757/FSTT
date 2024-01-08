class Solution {
    public int solution(int n) {
        int cnt = 1;
        while (true) { 
            if ((6 * cnt) % n == 0){
                return cnt;
            } else {
                cnt += 1;
            }
        }
    }
}