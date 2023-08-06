# noifTimer
Simple timer class to track average elapsed time with optional sub-second precision.<br>
Install with:
<pre>
python -m pip install noifTimer
</pre>
<br><br>
Usage:<br>
<pre>
from noifTimer import Timer
import time

def veryComplicatedFunction():
    time.sleep(1)

timer = Timer(subsecondFormat=True)
for _ in range(10):
    timer.start()
    veryComplicatedFunction()
    timer.stop()
print(f'{timer.averageElapsedTime=}')
print(timer.getStats())
</pre>
produces
<pre>
timer.averageElapsedTime=1.0005153999999998
elapsed time: 1s 871us
average elapsed time: 1s 515us
</pre>
