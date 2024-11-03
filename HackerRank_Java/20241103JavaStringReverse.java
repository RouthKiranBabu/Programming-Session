// https://www.hackerrank.com/challenges/java-string-reverse/problem?isFullScreen=false
import java.util.Scanner;

public class JavaStringReverse{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String s = scanner.next();
        scanner.close();
        // String s = "madam";
        String t = s.toLowerCase();
        char[] chararr = t.toCharArray();
        String ns = new String();
        for(int i = chararr.length -1 ; i >= 0; i --){
            String sc = Character.toString(chararr[i]);
            ns = ns.concat(sc);
        }
        // System.out.printf("%s\n%s", ns, t);
        if(ns.equals(t)){
            System.out.println("Yes");
        }else{
            System.out.println("No");
        }
    }
}
