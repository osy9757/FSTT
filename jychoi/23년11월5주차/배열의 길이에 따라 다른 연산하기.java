class Solution {
    public int[] solution(int[] arr, int n) {
        int[] answer = new int[arr.length];
        // arr 길이 홀수일 때
        if(arr.length % 2 == 1) {
            for (int i = 0; i < arr.length; i++) {
                if(i % 2 == 0){
                    answer[i] = arr[i] + n;
                } else{
                    answer[i] = arr[i];
                }
            }
        }
        // arr 길이 짝수일 때
        else {
            for(int i = 0; i < arr.length; i++){
                if(i % 2 == 1){
                    answer[i] = arr[i] + n;
                } else{
                    answer[i] = arr[i];
                }
            }
        }
        return answer;
    }
}