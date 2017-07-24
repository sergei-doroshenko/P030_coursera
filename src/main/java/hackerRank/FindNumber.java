package hackerRank;

import java.util.Arrays;

public class FindNumber {
    static String findNumber(int[] arr, int k) {
        if (k > arr.length) return "NO";
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == k) return "YES";
        }
        return "NO";
    }

    static int[] oddNumbers(int l, int r) {
        int start = l%2==0 ? l : l-1;
        int end = r%2==0 ? r : r+1;
        int[] a = new int[(end-start)/2];
        a[0] = l%2==0 ? l+1 : l;
        for (int i = 1; i < a.length; i++) {
            a[i] = a[i-1]+2;
        }
        return a;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(oddNumbers(2, 5)));
        System.out.println(Arrays.toString(oddNumbers(3, 9)));
    }
}
