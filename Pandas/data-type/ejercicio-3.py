n_missing_prices = reviews.price.isnull().sum()

# Check your answer
print(n_missing_prices)