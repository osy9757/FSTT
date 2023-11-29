class Solution {
    public int[] solution(int n) {
        int[] answer;
        if (n % 2 == 0) {
            answer = new int[n/2];
        } else {
            answer = new int[n/2 + 1];
        }
        int j = 0;
        for(int i=0; i<=n; i++){
            if (i % 2 != 0){
                answer[j] = i;
                j++;
            }
        }
        return answer;
    }
}

// 다른 사람 풀이 
import java.util.*;

class Solution {
    public ArrayList solution(int n) {
        ArrayList<Integer> answer = new ArrayList<Integer>();

        for(int i=1; i<=n; i++){
            if(i%2 != 0) {
                answer.add(i);
            } 
        }

        return answer;
    }
}