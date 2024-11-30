import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Date": [
        "10-01-16",
        "10-02-16",
        "10-03-16",
        "10-04-16",
        "10-05-16",
        "10-06-16",
        "10-07-16",
    ],
    "Open": [
        770.25,
        776.030029,
        774.25,
        776.030029,
        779.3541998,
        776.306698,
        779.659973,
    ],
    "High": [776.075902, 778.730022, 776.065702, 771.710022, 782.073407, 782.46398, 7],
    "Low": [769.5, 780.890015, 766.5, 772.890015, 775.650024, 775.539978, None],
    "Close": [
        782.659998,
        776.429993,
        772.549798,
        776.429993,
        776.469971,
        776.859985,
        756.32,
    ],
}

df = pd.DataFrame(data)
print(df)

# 6.a) Histogram
df["Close"].plot(kind="hist", bins=5, color="grey", edgecolor="black")
plt.title("Histogram - Close Values")
plt.xlabel("Close Value")
plt.ylabel("Frequency")
plt.show()

# b) Bar Chart
df["Close"].value_counts().plot(kind="bar", color="cyan", edgecolor="black")
plt.title("Bar Chart - Close Values")
plt.xlabel("Close Value")
plt.ylabel("Frequency")
plt.show()

# c) Pie Chart
df["Close"].value_counts().plot(kind="pie", autopct="%1.4f%%")
plt.title("Pie Chart - Close Values")
plt.show()
