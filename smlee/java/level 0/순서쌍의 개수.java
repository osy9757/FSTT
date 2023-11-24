// 나의 풀이
class Solution {
    public int solution(int n) {
        int answer = 0;
        for(int i=1; i<n+1; i++){
            for (int j=1; j<n+1; j++){
                if (i*j==n){
                    if (i == j){
                        answer *= 2;
                        answer += 1;
                        return answer;
                    } else if (i > j){
                        answer *= 2;
                        return answer;
                    }
                    answer += 1;
                }
            }
        }
        return answer;
    }
}

// 간단 풀이 
class Solution {
    public int solution(int n) {
        int answer = 0;
        for(int i = 1; i <= n; i++){
            if(n % i == 0){
                answer++;
            }
        }
        return answer;
    }
}
