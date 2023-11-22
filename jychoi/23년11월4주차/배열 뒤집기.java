import java.util.Stack;

class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length];
        Stack<Integer> stackInt = new Stack<>();
        for(Integer e: num_list){
            stackInt.push(e);
        }

        int i = 0;
        while (!stackInt.isEmpty()) {
            answer[i++] = stackInt.pop();
        }
        return answer;
    }
}