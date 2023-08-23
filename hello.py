import time
import random

import dvc.api
from dvclive import Live

params = dvc.api.params_show()

with Live(dir="new/model/config/trainer/optimizer/params") as live:
    for i in range(params["epochs"]):
        live.log_metric("mode1", i + random.random())
        live.log_metric("mode2", i + random.random())
        live.next_step()

        time.sleep(5)


live.end()
