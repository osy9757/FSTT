class Solution {
    public int solution(int[] dot) {
        // 1사분면
        if(dot[0] > 0 && dot[1] > 0) return 1;
            // 2사분면
        else if(dot[0] < 0 && dot[1] > 0) return 2;
            // 3사분면
        else if(dot[0] < 0 && dot[1] < 0) return 3;
            // 4사분면
        else if(dot[0] > 0 && dot[1] < 0) return 4;
            // 원점
        else return 0;
    }
}