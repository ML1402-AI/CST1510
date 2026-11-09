from unittest import result

import pandas as pd

servers = pd.read_csv("servers.csv")
print(servers)
servers["percent"] = (servers["used"]/servers["total"]) * 100

def classify (percent):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

servers["status"] = servers["percent"].apply(classify)
print(servers)
import pandas as pd
marks = pd.Series([40,60,80])
result = marks.apply(lambda x: x + 10)
print(result)