import time
import random

import dvc.api
from dvclive import Live

params = dvc.api.params_show()

with Live(dir="usage") as live:
    for i in range(params["epochs"]):
        live.log_metric("add", i + random.random())
        live.log_metric("commit", i + random.random())
        live.log_metric("push", i + random.random())
        live.log_metric("pull", i + random.random())
        live.log_metric("checkout", i + random.random())
        live.log_metric("clone", i + random.random())
        live.next_step()

        time.sleep(5)


live.end()
