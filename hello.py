import pandas as pd
from tabulate import tabulate

# Sample athlete data (you can replace this with your data)
data = {
    "Rank": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Athlete Name": ["Usain Bolt", "Michael Phelps", "Serena Williams", "Roger Federer", "LeBron James",
                     "Cristiano Ronaldo", "Lionel Messi", "Kobe Bryant", "Rafael Nadal", "Tom Brady"],
    "Sport": ["Track and Field", "Swimming", "Tennis", "Tennis", "Basketball",
              "Soccer", "Soccer", "Basketball", "Tennis", "American Football"],
    "Country": ["Jamaica", "USA", "USA", "Switzerland", "USA",
                "Portugal", "Argentina", "USA", "Spain", "USA"],
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Sort the DataFrame by Rank
df = df.sort_values(by="Rank")

# Display the top 10 athletes in a table
print(tabulate(df.head(10), headers="keys", tablefmt="pretty", showindex=False))
