import pandas as pd

# Load the data
df = pd.read_csv(r"C:\Users\SALOME\Desktop\assignment\python-final-project\owid-covid-data.csv")

# View the first few rows
print("🔍 First 5 rows of the dataset:")
print(df.head())

# View all column names
print("\n📋 Columns in the dataset:")
print(df.columns)

# Check for missing values in each column
print("\n❓ Missing values per column:")
print(df.isnull().sum())

# Look at the first 5 rows
print("First 5 rows:")
print(df.head())

# Show column names
print("\nColumn names:")
print(df.columns)

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Filter for specific countries
countries = ['Kenya', 'India', 'United States']
df = df[df['location'].isin(countries)]

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Drop rows where total_cases or total_deaths is missing
df = df.dropna(subset=['total_cases', 'total_deaths'])

# Fill all other missing numbers with 0
df.fillna(0, inplace=True)

# Preview cleaned data
print("\n✅ Cleaned Data:")
print(df.head())

import matplotlib.pyplot as plt

# Plot total cases over time for each country
plt.figure(figsize=(10, 6))

for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)

plt.title("📈 Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot daily new cases
plt.figure(figsize=(10, 6))

for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['new_cases'], label=country)

plt.title("📊 Daily New COVID-19 Cases")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot total vaccinations
plt.figure(figsize=(10, 6))

for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)

plt.title("💉 Total COVID-19 Vaccinations Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#  INSIGHTS:
# 1. The US had the fastest increase in vaccinations.
# 2. India had the biggest spike in daily cases in mid-2021.
# 3. Kenya had a relatively lower number of total cases and vaccinations.
