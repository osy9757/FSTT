class Solution {
    public int solution(String[] s1, String[] s2) {
        int answer = 0;
        for (String each1:s1) {
            for (String each2:s2){
                if (each1.equals(each2)){
                    answer++;
                }
            }
        }
        return answer;
    }
}