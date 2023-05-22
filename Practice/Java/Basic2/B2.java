package Practice.Java.Basic2;
import java.util.Scanner;

public class B2 {
    public static void main(String[] args){
        System.out.println("numの値を入力...");
        //try挟んだらエラー消えたから気にしない。
        try (Scanner scan = new Scanner(System.in)) {
            int num = scan.nextInt();
            //numの2で割った時の商が0=偶数
            if (num%2==0){
                System.out.println(num+"は偶数です。");
            //違う場合は奇数
            }else{
                System.out.println(num+"は奇数です。");
            }
        }
    }
}
