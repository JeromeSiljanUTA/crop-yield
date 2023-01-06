"""
crop_yield predicts crop yield using linear regression
"""

import pandas as pd

df = pd.read_csv("FAOSTAT_data_en_1-6-2023.csv")

#               df.describe(include="all")
# shows that "Domain Code", "Domain", "Area Code (M49)", "Area", "Item", "Item Code (CPC)" have the same value for all
# "Flag", "Flag Description" have 2 different values, useless to me
# Picking "Year" instead of "Year Code"
# "Element Code" seems useless

df.drop(
    columns=[
        "Area Code (M49)",
        "Area",
        "Domain Code",
        "Domain",
        "Element Code",
        "Flag Description",
        "Flag",
        "Item Code (CPC)",
        "Item",
        "Year Code",
    ],
    inplace=True,
)

print(df)
