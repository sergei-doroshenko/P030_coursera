package hackerRank;

public class MedianHeap {
    public static void main(String[] args) {
        int[] a = new int[]{12, 4, 5, 3, 8, 7};
        double median = 0;
        for (int i = 0; i < a.length; i++) {
            median = (median + a[i])/(i+1);
            System.out.println(median);
        }
    }
}
/*
12.0
8.0
5.0
4.5
5.0
6.0
 */