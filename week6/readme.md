TODO: Reflect on what you learned this week and what is still unclear.

jupyter:

import pandas as pd

my_df = pd.read_csv("example.csv")
my_df.head()
my_df.sample(7)
my_df["is"]             #gives u the "is" column
my_df.loc[0]            #gives u "0" row
my_df.loc[0].to_list    #gives u a list of "0" row

def join_up(row):
    return " ".join(row.tp_list())
my_df["joined"] = my_df.apply(join_up, axis=1)
