import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Netflix Dataset
data = {
    "Title": [
        "Stranger Things", "Wednesday", "Extraction",
        "Dark", "Money Heist", "The Witcher",
        "Squid Game", "Lucifer", "Breaking Bad",
        "The Crown", "You", "Bridgerton"
    ],

    "Type": [
        "TV Show", "TV Show", "Movie", "TV Show",
        "TV Show", "TV Show", "TV Show", "TV Show",
        "TV Show", "TV Show", "TV Show", "TV Show"
    ],

    "Genre": [
        "Sci-Fi", "Comedy", "Action", "Sci-Fi",
        "Thriller", "Fantasy", "Thriller", "Fantasy",
        "Crime", "Drama", "Thriller", "Romance"
    ],

    "Release_Year": [
        2016, 2022, 2020, 2017, 2017, 2019,
        2021, 2016, 2008, 2016, 2018, 2020
    ],

    "Country": [
        "USA", "USA", "USA", "Germany", "Spain", "USA",
        "South Korea", "USA", "USA", "UK", "USA", "UK"
    ]
}

df = pd.DataFrame(data)

# Display Dataset
print("\n===== NETFLIX DATASET =====")
print(df)

# Dataset Information
print("\n===== DATASET SUMMARY =====")
print(df.info())

# Count Movies and TV Shows
print("\n===== CONTENT TYPES =====")
print(df["Type"].value_counts())

# Most Common Genres
print("\n===== GENRE DISTRIBUTION =====")
print(df["Genre"].value_counts())

# Content by Country
print("\n===== CONTENT BY COUNTRY =====")
print(df["Country"].value_counts())

# Visualization 1: Content Types
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Type")
plt.title("Netflix Content Types")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig("content_types.png")
plt.show()

# Visualization 2: Genre Distribution
plt.figure(figsize=(9, 5))
sns.countplot(data=df, y="Genre",
              order=df["Genre"].value_counts().index)
plt.title("Netflix Genre Distribution")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.tight_layout()
plt.savefig("genre_distribution.png")
plt.show()

# Visualization 3: Releases by Year
plt.figure(figsize=(9, 5))
sns.histplot(data=df, x="Release_Year", bins=8)
plt.title("Content Release Year Distribution")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig("release_years.png")
plt.show()

# Final Insights
print("\n===== KEY INSIGHTS =====")

print("Total Titles:", len(df))
print("Most Common Genre:", df["Genre"].mode()[0])
print("Most Represented Country:", df["Country"].mode()[0])
print("Latest Release Year:", df["Release_Year"].max())

print("\nNetflix Data Analysis Completed!")
