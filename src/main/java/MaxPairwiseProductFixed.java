import java.io.*;
import java.util.StringTokenizer;

public class MaxPairwiseProductFixed {
    // Current implementation operates with numbers
    // another approach is to operate with array's indexes
    static long getMaxPairwiseProduct( int[] numbers ) {

        int n = numbers.length;
        long max1 = 0, max2 = 0;
        // loop through all number
        for ( int i = 0; i < n; ++i ) {
            // If particular number is greater than max1
            // replace max1 value to this number, BUT
            // before to do this - check max2.
            if ( numbers[ i ] > max1 ) {
                // If current max1 value is greater than max2
                // assign max1 to max2.
                if ( max1 > max2 ) {
                    max2 = max1;
                }
                // Assign particular number's value to max1.
                max1 = numbers[ i ];
            } else if ( numbers[ i ] > max2 ) {
                max2 = numbers[ i ];
            }

        }

        // Multiply max1 to max2
        long result = max1 * max2;
        return result;
    }

    static long getMaxPairwiseProductIndexes( int[] numbers ) {

        int maxIndex1 = -1, maxIndex2 = -1;
        // Find max1 index
        for ( int i = 0; i < numbers.length; ++i ) {
            if ( maxIndex1 == -1 || numbers[ maxIndex1 ] < numbers[ i ] ) {
                maxIndex1 = i;
            }
        }

        // Find max2 index
        for ( int i = 0; i < numbers.length; ++i ) {
            // The same as for maxIndex1, just exclude maxIndex1 from comparison
            if ( i != maxIndex1 && ( maxIndex2 == -1 || numbers[ maxIndex2 ] < numbers[ i ] ) ) {
                maxIndex2 = i;
            }
        }

        // Multiply max1 to max2
        long result = ( long ) numbers[ maxIndex1 ] * ( long ) numbers[ maxIndex2 ];
        return result;
    }

    public static void main( String[] args ) throws FileNotFoundException {

//        FastScanner scanner = new FastScanner( System.in );
        FastScanner scanner = new FastScanner( new FileInputStream( "test_numbers.txt" ) );
        int n = scanner.nextInt();
        int[] numbers = new int[ n ];
        for ( int i = 0; i < n; i++ ) {
            numbers[ i ] = scanner.nextInt();
        }

//        System.out.println( getMaxPairwiseProduct( numbers ) );
        System.out.println( TestUtils.runWrapped( MaxPairwiseProductFixed::getMaxPairwiseProduct3, numbers  ) );
        System.out.println( TestUtils.runWrapped( MaxPairwiseProductFixed::getMaxPairwiseProduct4, numbers  ) );
    }

    public static Object getMaxPairwiseProduct4( Object o ) {
        int[] numbers = (int[]) o;
        int maxIndex1 = -1, maxIndex2 = -1;
        // Find max1 index
        for ( int i = 0; i < numbers.length; ++i ) {
            if ( maxIndex1 == -1 || numbers[ maxIndex1 ] < numbers[ i ] ) {
                maxIndex1 = i;
            }
        }

        // Find max2 index
        for ( int i = 0; i < numbers.length; ++i ) {
            // The same as for maxIndex1, just exclude maxIndex1 from comparison
            if ( i != maxIndex1 && ( maxIndex2 == -1 || numbers[ maxIndex2 ] < numbers[ i ] ) ) {
                maxIndex2 = i;
            }
        }

        // Multiply max1 to max2
        long result = ( long ) numbers[ maxIndex1 ] * ( long ) numbers[ maxIndex2 ];
        return result;
    }

    public static Object getMaxPairwiseProduct3( Object o ) {
        int[] numbers = (int[]) o;
        long result = 0;
        int n = numbers.length;
        for ( int i = 0; i < n; ++i ) {
            for ( int j = i + 1; j < n; ++j ) {
                if ( (long) numbers[ i ] * (long) numbers[ j ] > result ) {
                    result = (long) numbers[ i ] * (long) numbers[ j ];
                }
            }
        }
        return result;
    }

    static class FastScanner {

        BufferedReader br;
        StringTokenizer st;

        FastScanner( InputStream stream ) {
            try {
                br = new BufferedReader( new InputStreamReader( stream ) );
            } catch ( Exception e ) {
                e.printStackTrace();
            }
        }

        String next() {
            while ( st == null || !st.hasMoreTokens() ) {
                try {
                    st = new StringTokenizer( br.readLine() );
                } catch ( IOException e ) {
                    e.printStackTrace();
                }
            }

            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt( next() );
        }
    }

}