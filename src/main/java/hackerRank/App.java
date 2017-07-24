package hackerRank;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;

public class App {
    public static void main(String[] args) {
        System.out.println(4%5);
        System.out.println(2895 % 9787);
        int[] a = new int[] {1, 2, 3, 4};
        System.out.println(IntStream.of(a).sum());
        System.out.println(consSum(1L, 4L));
        System.out.println(consSum(1L, 5L));
        System.out.println(consSum(4L, 6L));
        System.out.println(consSum(7L, 8L));
        System.out.println(consSum(1L, 4L));

        int k = 15;
        List<Integer> dd = getDD(k);
        System.out.println(dd);
        System.out.println(getSums(dd, k));

    }

    public static List<Integer> getDD(int k) {
        int m = k * 2;
        List<Integer> dd = new ArrayList<>();
        for (int i = 2; i < m; i++) {
            if (m % i == 0) {
                dd.add(i);
            }
        }
        return dd;
    }

    public static int getSums(List<Integer> dd, int k) {
        int sums = 0;
        for (Integer integer : dd) {
            int a = getA(integer, k);
            System.out.println(a);
            if (a > 0) {
                sums++;
            }
        }
        return sums;
    }

    public static int getA(int n, int s) {
        int temp = (2*s/n - (n-1));
        return temp % 2 == 0 ? temp/2 : 0;
    }

    public static long consSum(long start, long end) {
        return (end - start + 1) * (start + end) / 2;
    }

    public static int cSum(int a, int n) {
        // S = n * (2 * a_1 + (n - 1)) / 2
        int s = n * (2 * a + (n - 1)) / 2;
        return s;
    }
}
