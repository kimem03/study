class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String A = Integer.toString(a) + Integer.toString(b);
        String B = Integer.toString(b) + Integer.toString(a);
        
        if(Integer.parseInt(A) > Integer.parseInt(B)) {
            answer = Integer.parseInt(A);
        } else {
            answer = Integer.parseInt(B);
        }
        return answer;
    }
}