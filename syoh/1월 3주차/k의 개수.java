class Solution {
    public int solution(int i, int j, int k) {
        int count = 0;
        for (int num = i; num <= j; num++) {
            int temp = num;
            while (temp > 0) {
                if (temp % 10 == k) {
                    count++;
                }
                temp /= 10;
            }
        }
        return count;
    }
}