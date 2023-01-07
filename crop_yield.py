"""
crop_yield predicts crop yield using linear regression
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("FAOSTAT_data_en_1-6-2023.csv")

# remove unnecessary columns
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

# shows values over time in line plot
# sns.lineplot(x="Year", y="Value", data=df, hue="Element")

# pivot values
df_pivot = (
    df.pivot(index="Year", columns="Element", values="Value")
    .reset_index()
    .drop(columns=["Production"])
    .rename(
        columns={
            "Area harvested": "Area Harvested (ha)",
            "Yield": "Yield (hg/ha)",
        }
    )
)

# setting X, Y, training and testing sets
X = df_pivot.drop(columns=["Yield (hg/ha)"])
Y = df_pivot["Yield (hg/ha)"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.25, random_state=30
)

# generate and fit model
lin_model = LinearRegression()
lin_model.fit(X_train, Y_train)

# show prediction vs actual data
y_hat = lin_model.predict(X_test)
sns.lineplot(x="Year", y="Yield (hg/ha)", data=df_pivot)
sns.lineplot(x="Year", y=y_hat, data=X_test, color="orange")
plt.show()

# calculate r2 score
r2 = r2_score(Y_test, y_hat)
print(f"R squared score: {r2:.3f}")

# show residual plot
residual = y_hat - Y_test
sns.scatterplot(x="Year", y=residual, data=X_test)
plt.title("Residual Plot")
plt.ylabel("Yield (hg/ha)")
plt.xlabel("Year")
