import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.Arrays;
import java.util.Random;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/**
 * Created by Sergei_Doroshenko on 11/14/2016.
 */
public class TestUtils {

    public static void main( String[] args ) throws IOException {
//        runWrapped( MaxPairwiseProductFixed::getMaxPairwiseProduct4, new int[]{ 1, 2, 3 } );
//        createTestTxt();

        runStressTests();
    }

    public static Object runWrapped( Function f, int[] arr ) {
        long start = System.currentTimeMillis();
        Object result = f.apply( arr );
        long end = System.currentTimeMillis();
        System.out.println( end - start );
        return result;
    }

    public static void createTestTxt() throws IOException {
        Path path = Paths.get( "test_numbers.txt" );
        Files.createFile( path );
        Random random = new Random();
        int n = 100_000;
        String head = n + "";
        String numbers = IntStream.range( 0, n )
                .mapToObj( i -> random.nextInt( i + 10 ) + " " )
                .collect( Collectors.joining( " " ) );

        Files.write( path, Arrays.asList( head, numbers ), StandardOpenOption.WRITE );
    }

    public static void runStressTests() {
        while ( true ) {
            Random random = new Random();
            int n = random.nextInt( 8 ) + 2;
            System.out.println(n);
            int[] numbers = new int[ n ];

            for ( int i = 0; i < n; i++ ) {
//                numbers[ i ] = random.nextInt( Integer.MAX_VALUE );
                numbers[ i ] = random.nextInt( 100_000 );
            }

            System.out.println( Arrays.toString( numbers ) );

            long result1 = MaxPairwiseProduct.getMaxPairwiseProduct( numbers );
            long result2 = MaxPairwiseProductFixed.getMaxPairwiseProduct( numbers );

            if ( result1 != result2 ) {
                System.out.println( "Wrong answer: " + result1 + ", " + result2 );
                break;
            } else {
                System.out.println( "OK" );
            }
        }
    }
}
