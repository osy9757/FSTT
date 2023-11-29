class Solution {
  public String solution(String myString) {
      String answer = "";
      int num;        
      
      for (int i=0; i<myString.length(); i++) {
          num = (int)myString.charAt(i);
          if(num<97)
              answer += (char)(num+32);
          else
              answer += (char)(num);
              
      }   
      return answer;
  }
}