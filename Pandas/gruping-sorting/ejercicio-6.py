country_variety_counts = reviews.groupby(['country','variety']).size().sort_values(ascending=False)

# Check your answer
print(country_variety_counts
)