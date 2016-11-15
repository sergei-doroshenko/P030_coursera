import org.junit.BeforeClass;
import org.junit.Test;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

/**
 * Created by Sergei_Doroshenko on 11/15/2016.
 */
public class MaxPairwiseProductTest extends TimeMeasuredTest {

    private static int[] numbers;

    @BeforeClass
    public static void setUpClass() throws FileNotFoundException {
        numbers = readNumbersFromFile( "test_numbers.txt" );
    }

    @Test
    public void getMaxPairwiseProductIndexesTest1() {
        testName = "getMaxPairwiseProductIndexesTest";
        long result = ( long ) MaxPairwiseProductFixed.getMaxPairwiseProduct3( numbers );
        System.out.println( "result: " + result );
    }

    @Test
    public void getMaxPairwiseProductIndexesTest2() {
        testName = "getMaxPairwiseProductIndexesTest";
        long result = ( long ) MaxPairwiseProductFixed.getMaxPairwiseProduct4( numbers );
        System.out.println( "result: " + result );
    }

    private static int[] readNumbersFromFile(String fileName) throws FileNotFoundException {
        MaxPairwiseProductFixed.FastScanner scanner = new MaxPairwiseProductFixed.FastScanner( new FileInputStream( fileName ) );
        int n = scanner.nextInt();
        int[] numbers = new int[ n ];
        for ( int i = 0; i < n; i++ ) {
            numbers[ i ] = scanner.nextInt();
        }

        return numbers;
    }
}
