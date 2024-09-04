import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String res = "";
        
        for(int i = 0; i < a.length(); i++) {
            char c = a.charAt(i);
            if(Character.isUpperCase(c)) {
                res += Character.toLowerCase(c);
            } else {
                res += Character.toUpperCase(c);
            }
        }
        
        System.out.println(res);
    }
}