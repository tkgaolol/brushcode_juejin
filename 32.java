
import java.util.Arrays;
 
public class Main {
 
    static int n;
 
    static int A;
 
    static int B;
 
    static int[] array_a;
 
    static int res;
 
    public static int solution(int n, int A, int B, int[] array_a) {
        // Please write your code here
        Main.n = n;
        Main.A = A;
        Main.B = B;
        Main.array_a = array_a;
        Main.res = 0;
        dg(0,0,0);
        int sum = Arrays.stream(array_a).sum();
        if(sum % 10 == A) Main.res++;
        if(sum % 10 == B) Main.res++;
        return res;
    }
 
    private static void dg(int index,int sum_a,int sum_b) {
        if(index == n){
            if(sum_a % 10 == A && sum_b % 10 == B){
                res++;
            }
            return;
        }
        dg(index+1,sum_a+array_a[index],sum_b);
        dg(index+1,sum_a,sum_b+array_a[index]);
    }
 
    public static void main(String[] args) {
        //  You can add more test cases here
        int[] array1 = {1, 1, 1};
        int[] array2 = {1, 1, 1};
        int[] array3 = {1, 1};
 
        System.out.println(solution(3, 1, 2, array1) == 3);
        System.out.println(solution(3, 3, 5, array2) == 1);
        System.out.println(solution(2, 1, 1, array3) == 2);
    }
}
