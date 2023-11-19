class Solution {
    public int[] solution(int money) {
        int americano = (int) money / 5500;
        int left = money - (americano * 5500);
        int[] answer = {americano, left};
        return answer;
    }
}