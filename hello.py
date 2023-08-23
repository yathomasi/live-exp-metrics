import time
import random

import dvc.api
from dvclive import Live

params = dvc.api.params_show()

with Live(dir="hello/usage") as live:
    for i in range(params["epochs"]):
        live.log_metric("bar", i + random.random())
        live.log_metric("foo", i + random.random())
        live.next_step()

        time.sleep(5)


live.end()
