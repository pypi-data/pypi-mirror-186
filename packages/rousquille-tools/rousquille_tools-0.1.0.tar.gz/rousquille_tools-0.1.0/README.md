# Rousquille's tools

My personal toolbox 🛠

## Python 🐍

<details><summary>Measurement of the time used by a function</summary>
<p>

```py
import time
from rousquille_tools.decorators import time_def


@time_def
def func1():
    time.sleep(5)
```
Result:
```py
>>> func1()
[time_def] Function: func1 Time: 5.0s
```


</p>
</details>


