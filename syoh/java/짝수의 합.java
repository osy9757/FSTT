class Solution {
    public int solution(int n) {
        int sumNum = 0;
        for (int i=0; i<=n ; i+=2 )
            sumNum+=i;
        return sumNum;
            
    }
}