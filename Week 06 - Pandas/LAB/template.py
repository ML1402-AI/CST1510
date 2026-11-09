"""
RECORD CHECK  -  my version
===========================

Name  : Maliha
Lane  :  AI     (delete two)
Date  : 28th October, 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== LOAD

import pandas as pd
# opens the data frame file
with open("labfile.csv", "r") as f:
 lab= pd.read_csv("labfile.csv")  # replace with pd.read_csv("your_file.csv")

# ================================================================= PROCESS

lab["percent"] = (lab["value"]/lab["limit"])*100
lab["status"] = lab["percent"].apply(lambda p:
                                   "OVER LIMIT" if p >=100
                                   else "WARNING" if p >=90
                                   else "OK"
                                   )

# ================================================================== OUTPUT
#
print(lab)

not_ok = lab[lab["status"] != "OK"]
print(not_ok)

grouped = lab.groupby("status")
print(lab["status"].value_counts())
lab.to_csv("newlab.csv")

import matplotlib.pyplot as plt
lab["status"].value_counts().plot(kind="bar")
plt.title("Counts per Status")
plt.savefig("lab_count.png")
plt.show()


# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
