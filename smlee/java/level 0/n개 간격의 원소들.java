class Solution {
    public int[] solution(int[] num_list, int n) {
        int l;
        if (num_list.length%n != 0){
            l = num_list.length/n + 1;
        } else {
            l = num_list.length/n;
        }
        int[] answer = new int[l];
        int j = 0;
        for (int i=0; i <l; i++){
            answer[i] = num_list[j];
            j += n;
        }
        return answer;
    }
}