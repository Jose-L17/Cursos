top_oceania_wines = reviews.loc [(reviews.country.isin(['Australia','New Zealand'])) & (reviews.points>=95)]

# Check your answer
print(top_oceania_wines
)