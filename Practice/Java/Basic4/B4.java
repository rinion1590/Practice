package Practice.Java.Basic4;

public class B4{
    public static void main(String[] args){
    String str = "Hello!World";
    System.out.println("先頭から6文字取り出す -> " + str.substring(0,6));
    System.out.println("先頭から9文字取り出す -> " + str.substring(0,9));
    System.out.println("7文字目から5文字取り出す -> " + str.substring(6,11));

    str = "氏名：西園寺池面";
    //"："のある位置を取得
    int index = str.indexOf("：");
    System.out.println(str);
    System.out.println("：の後の文字列を取り出す ->" + str.substring(index+1));
    }
}
