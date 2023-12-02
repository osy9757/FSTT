class Solution {
    public int solution(int n) {
        if(n%Math.sqrt(n) == 0)
            return 1;
        return 2;
    }
}