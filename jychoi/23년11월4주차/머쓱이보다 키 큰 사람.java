class Solution {
    public int solution(int[] array, int height) {
        int answer = 0;
        for (int e: array){
            if(height < e) answer++;
        }
        return answer;
    }
}