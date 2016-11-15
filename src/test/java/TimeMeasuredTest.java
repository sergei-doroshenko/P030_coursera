import org.junit.After;
import org.junit.Before;

import java.util.concurrent.TimeUnit;

/**
 * Created by Sergei_Doroshenko on 11/15/2016.
 */
public class TimeMeasuredTest {

    private long startTime;
    private long endTime;
    protected String testName;

    @Before
    public void setUp() {
        startTime = System.nanoTime();
    }

    @After
    public void shutDown() {
        endTime = System.nanoTime();
        long nanos = endTime - startTime;
        String message = String.format( "Test %s, spent %d microseconds", testName, TimeUnit.NANOSECONDS.toMicros( nanos ) );
        System.out.println( message );
    }

}
