import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv(
        "./epa-sea-level.csv",
        index_col="year",
        names=["year", "csiro", "lower-error", "upper-error", "noaa"],
        header=0,
    )

    # Create scatter plot
    plt.scatter(x=df.index, y=df["csiro"])

    # Create first line of best fit
    x_all = list(range(min(df.index), 2051))
    res = linregress(df.index, y=df["csiro"])
    y_all = [res.slope * x + res.intercept for x in x_all]
    plt.plot(x_all, y_all)

    # Create second line of best fit
    x1_all = list(range(2000, 2051))
    df_from_2000 = df[(df.index >= 2000)]
    res1 = linregress(df_from_2000.index, y=df_from_2000["csiro"])
    y1_all = [res1.slope * x1 + res1.intercept for x1 in x1_all]
    plt.plot(x1_all, y1_all)

    # Add labels and title
    plt.ylabel("Sea Level (inches)")
    plt.xlabel("Year")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
