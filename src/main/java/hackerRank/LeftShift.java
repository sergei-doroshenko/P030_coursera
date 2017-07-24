package hackerRank;

import java.util.Scanner;

public class LeftShift {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int a[] = new int[n];

        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }
        int b[] = new int[n];
        for (int i = 0; i < a.length; i++) {
            int ind = calculateIndex(i, k, a.length);
            b[ind] = a[i];
        }
        for (int j = 0; j < b.length; j++) {
            if (j < b.length -1 ) {
                System.out.print(b[j] + " ");
            } else {
                System.out.print(b[j]);
            }
        }
    }

    private static int calculateIndex(int i, int k, int length) {
        if (i > k) {
            return i - k;
        } else {
            int result = length - (k - i);
            return result >= length ? 0 : result;
        }
    }
}
