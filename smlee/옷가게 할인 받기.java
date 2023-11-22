class Solution {
    public int solution(int price) {
        double answer = (double) price;
        if (100000 <= answer && answer < 300000 ){
            answer = (1-0.05)*answer;
        } else if (300000<= answer && answer < 500000){
            answer = (1-0.1)*answer;
        } else if (price >= 500000){
            answer = (1-0.2)*answer;
        }
        return (int) answer;
    }
}