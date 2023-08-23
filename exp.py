import time
import random

import dvc.api
from dvclive import Live

params = dvc.api.params_show()

with Live(dir="exp") as live:
    for i in range(params["epochs"]):
        live.log_metric("model/name", i + random.random())
        live.log_metric("model/config/trainer/epochs", i )
        live.log_metric("model/config/trainer/batch_size", i + random.random())
        live.log_metric("model/config/trainer/learning_rate", i + random.random())
        live.log_metric("model/config/optimizer/name", i + random.random())
        live.log_metric("model/config/optimizer/weights/decay", i + random.random())
        live.log_metric("model/config/optimizer/weights/learning_rate", i + random.random())
        live.next_step()

        time.sleep(5)


live.end()
