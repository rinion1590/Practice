package Practice.Java.Basic3;
import java.util.Scanner;

public class B3 {
    public static void main(String[] args){
        System.out.println("入力してください");
        //try挟んだけらエラー治って動いたからよしっ
        try (Scanner scan = new Scanner(System.in)) {
            String str = scan.next();
            System.out.println("入力された文字は｢"+str+"｣です。");
        }
    }
}
