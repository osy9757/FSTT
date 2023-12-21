class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        if(a*Math.pow(10, (int)(Math.log10(b)+1)) + b > b*Math.pow(10, (int)(Math.log10(a)+1)) + a){
            answer = (int)(a*Math.pow(10, (int)(Math.log10(b)+1))) + b;
        } else{
            answer = (int)(b*Math.pow(10, (int)(Math.log10(a)+1))) + a;
        }
        return answer;
    }
}