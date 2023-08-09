import time
import random

import dvc.api
from dvclive import Live

params = dvc.api.params_show()

with Live(dir="system") as live:
    for i in range(params["epochs"]):
        live.log_metric("linux", i + random.random())
        live.log_metric("windows", i + random.random())
        live.log_metric("mac", i + random.random())
        live.next_step()

        time.sleep(5)


live.end()
