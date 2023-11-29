class Solution {
  public int[] solution(int n) {
      int[] answer = new int[(n+1)/2];
      for(int idx=0, num=1; num<=n;idx++, num+=2) {
          answer[idx] = num;
      }
      return answer;
  }
}