import sys
from time import sleep


def write_progress_bar(number, borders=['[', ']'], timeout=1):
    for i in range(number+1):
        appender = str(i) + borders[0] + ('=' * i + ' ' * (number - i) + borders[1])
        sys.stdout.write("\rInserted: %s" % appender)
        sleep(timeout)
        sys.stdout.flush()

    sys.stdout.write("\n")

write_progress_bar(30, timeout=0.5)
