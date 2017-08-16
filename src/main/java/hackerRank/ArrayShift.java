package hackerRank;

import java.util.Arrays;

public class ArrayShift {
    // shift arr[] of siz n by d
    public void leftShift(int arr[], int d, int n) {
        int i, j, k, temp;

        for (i = 0; i < gcd(d, n); i++) {
            /* move i-th values of blocks */
            temp = arr[i];
            j = i;

            while (1 != 0) {
                k = j + d;
                if (k >= n)
                    k = k - n;
                if (k == i)
                    break;
                arr[j] = arr[k];
                j = k;
            }

            arr[j] = temp;
        }
    }

    public void printArray(int arr[], int size) {
        for (int i = 0; i < size; i++) {
            System.out.print(arr[i] + " ");
        }
    }

    // get gcd of a and b
    public int gcd(int a, int b) {
        return (b == 0) ? a : gcd(b, a % b);
    }

    public static void main(String[] args) {
        ArrayShift rotate = new ArrayShift();
        int arr[] = {1, 2, 3, 4, 5, 6, 7};
        System.out.println(String.format("Before: %s", Arrays.toString(arr)));
        rotate.leftShift(arr, 2, 7);
        System.out.println(String.format("After: %s", Arrays.toString(arr)));
//        rotate.printArray(arr, 7);
        System.out.println("GCD 1000000 and 2000000 is: " + rotate.gcd(1_000_000, 2_000_000));
    }
}
