reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)

# Check your answer
print(reviews_per_region)