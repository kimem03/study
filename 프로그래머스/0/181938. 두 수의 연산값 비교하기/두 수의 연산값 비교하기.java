class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String A = Integer.toString(a) + Integer.toString(b);
        int B = 2 * a * b;
        
        if(Integer.parseInt(A) > B) {
            answer = Integer.parseInt(A);
        } else {
            answer = B;
        }
        
        return answer;
    }
}