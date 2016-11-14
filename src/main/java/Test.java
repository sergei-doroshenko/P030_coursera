import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.Arrays;
import java.util.Random;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/**
 * Created by Sergei_Doroshenko on 11/14/2016.
 */
public class Test {
    public static void main( String[] args ) throws IOException {
        /*long result = 100_000L * 90_000;
        System.out.println( result );*/

        Path path = Paths.get( "test_numbers.txt" );
        Files.createFile( path );
        Random random = new Random();
        int n = 10;
        String head = n + "";
        String numbers = IntStream.range( 0, n )
                .mapToObj( i -> random.nextInt( i+10 ) + " " )
                .collect( Collectors.joining( " " ) );

        Files.write( path, Arrays.asList(head, numbers), StandardOpenOption.WRITE );
    }
}
