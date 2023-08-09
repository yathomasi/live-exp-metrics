import time
import random

import dvc.api
from dvclive import Live

params = dvc.api.params_show()

with Live() as live:
    for i in range(params["epochs"]):
        live.log_metric("dvclive/metrics.json:bar", i + random.random())
        live.log_metric("usage/commands.json:add", i + random.random())
        live.log_metric("usage/commands.json:commit", i + random.random())
        live.log_metric("usage/commands.json:push", i + random.random())
        live.log_metric("usage/commands.json:pull", i + random.random())
        live.log_metric("usage/commands.json:checkout", i + random.random())
        live.log_metric("usage/commands.json:clone", i + random.random())
        live.log_metric("usage/version.json:2.29.2", i + random.random())
        live.log_metric("usage/version.json:2.29.0", i + random.random())
        live.log_metric("dvclive/metrics.json:foo", i + random.random())
        live.log_metric("usage/os.json:linux", i + random.random())
        live.log_metric("usage/os.json:windows", i + random.random())
        live.log_metric("usage/os.json:mac", i + random.random())
        live.next_step()

        time.sleep(5)


live.end()
