# noiftimer
Simple timer class to track average elapsed time with optional sub-second precision.<br>
Install with:
<pre>pip install noiftimer</pre>

Usage:
<pre>
from noiftimer import Timer
import time

def very_complicated_function():
    time.sleep(1)

timer = Timer()
for _ in range(10):
    timer.start()
    very_complicated_function()
    timer.stop()
print(f'{timer.average_elapsed_time=}')
print(timer.get_stats(subsecond_resolution=True))
</pre>
produces
<pre>
timer.average_elapsed_time=1.0006019
elapsed time: 1s 836us
average elapsed time: 1s 601us
</pre>
