reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()

# Check your answer
print(reviewer_mean_ratings)
